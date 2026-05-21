from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch
import time


from app.config import *
from app.utils.preprocess import preprocess_text
from app.utils.chunking import chunk_text
from functools import lru_cache
from langdetect import detect


class MultilingualSummarizer:
    
    # Language mapping
    language_codes = {
            "bn": "ben_Beng",
            "en": "eng_Latn",
            "hi": "hin_Deva"
        }

    def __init__(self):
        
        print("Initializing summarizer...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")

        # Translation model
        self.translator = pipeline(
            "translation",
            model="facebook/nllb-200-distilled-600M",
            device=0 if torch.cuda.is_available() else -1
        )

        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        
        print("Tokenizer loaded")

        print("Loading summarization model (this may take time)...")

        start = time.time()  # start timing

        try:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(self.device)
        
        
        except Exception as e:
            print(f"Model load failed: {e}")
            raise RuntimeError("Model loading failed. Please restart the app.")
        
        self.model.eval()
        
        end = time.time()  # end timing

        print(f"Model loaded successfully in {end - start:.2f} seconds")


    # Translation
    def translate_text(self, text, target_language, source_language="eng_Latn"):

        target_code = self.language_codes.get(
            target_language,
            "eng_Latn"
        )

        translated = self.translator(
            text,
            src_lang=source_language,
            tgt_lang=target_code,
            max_length=512
        )

        return translated[0]["translation_text"]

    detect_map = {
        "bn": "ben_Beng",
        "en": "eng_Latn",
        "hi": "hin_Deva"
        }

    # Summarize single chunk
    def summarize_chunk(self, text, max_len):

        prompt = f"summarize: {text}"

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )
        inputs = {k: v.to(self.device, non_blocking=True) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_len,
                min_new_tokens=20,
                num_beams=4,
                temperature=0.7,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

     # Main summarization flow
    def summarize(self, text: str, target_language="bn", length="medium"):

        # Skip empty input
        text = text.strip()
        
        if not text:
            return ""
        
        text = preprocess_text(text)

        # Detect the language
        try:
            input_lang = detect(text)
        except:
            input_lang = "en"

        source_code = self.detect_map.get(
            input_lang,
            "eng_Latn"
        )
        
        # Step 1: Translate input to English if needed
        if input_lang != "en":
            text = self.translate_text(
                text, 
                "en", 
                source_language=source_code
            ) 

        # Limit text size
        text = text[:3000]
        
        chunks = chunk_text(text)
        
        if not chunks:
            return ""

        # Length control
        if length == "short":
            max_length = 60
        elif length == "long":
            max_length = 200
        else:
            max_length = 120

        # Summarize in ORIGINAL language
        summaries = [ 
            self.summarize_chunk(chunk, max_length)
            for chunk in chunks
            ]

        final_text = " ".join(summaries)

        # Re-summarize combined chunks
        if len(summaries) > 1:
            final_text = final_text[:1000]
            final_text = self.summarize_chunk(final_text, max_length)

        # Step 2: Translate summary to target language
        if target_language != "en":
            final_text = self.translate_text(
                final_text,
                target_language,
                source_language="eng_Latn"
            )

        return final_text


summarizer = None

def get_summarizer():
    global summarizer
    if summarizer is None:
        print("⚡ Loading model for first time...")
        summarizer = MultilingualSummarizer()
    return summarizer

@lru_cache(maxsize=100)
def cached_summarize(text, language, length):
    text = text.strip()

    if not text:
        return""
    
    summarizer = get_summarizer()
    return summarizer.summarize(text, language, length)

