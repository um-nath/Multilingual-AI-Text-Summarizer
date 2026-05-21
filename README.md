# Multilingual-AI-Text-Summarizer
An AI-powered multilingual text summarization system built using Transformer models, capable of summarizing and translating text across **Bengali, English, and Hindi**.

---
Built using:

* Transformers
* Gradio
* Hugging Face Models
* PyTorch
* Translation Pipelines
* NLP Preprocessing

---

# 🚀 Features

✅ Multilingual Summarization

✅ Bengali ↔ English ↔ Hindi Support

✅ AI-powered Translation Pipeline

✅ Intelligent Language Detection

✅ Chunk-based Long Text Processing

✅ Download Generated Summary

✅ GPU Acceleration Support

✅ Caching for Faster Responses

✅ Interactive Gradio UI

---

# 🧠 Workflow Architecture

```text
User Input
    ↓
Language Detection
    ↓
Translate Input → English (if needed)
    ↓
Text Preprocessing
    ↓
Chunking Long Text
    ↓
mT5 Multilingual Summarization
    ↓
Merge Chunk Summaries
    ↓
Translate Summary → Target Language
    ↓
Final Output Summary
```

---

# 🏗️ Tech Stack

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Backend Development   |
| Gradio       | UI Interface          |
| Transformers | NLP Models            |
| PyTorch      | Deep Learning Runtime |
| mT5 XLSum    | Summarization Model   |
| NLLB-200     | Translation Model     |
| Langdetect   | Language Detection    |

---

# 🤖 Models Used

## Summarization Model

`csebuetnlp/mT5_multilingual_XLSum`

Used for multilingual abstractive text summarization.

## Translation Model

`facebook/nllb-200-distilled-600M`

Used for high-quality multilingual translation.

---

# 📂 Project Structure

```text
multi-language-summarizer/
│
├── app/
│   ├── services/
│   │   └── summarizer.py
│   ├── utils/
│   │   ├── preprocess.py
│   │   └── chunking.py
│   ├── config.py
│
├── ui.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/um-nath/multilingual-ai-text-summarizer.git
cd multilingual-ai-text-summarizer
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python ui.py
```

Open in browser:

```text
http://127.0.0.1:7860
```

---

# 🌐 Supported Language Combinations

| Input Language | Output Language |
| -------------- | --------------- |
| Bengali        | Bengali         |
| Bengali        | English         |
| Bengali        | Hindi           |
| English        | English         |
| English        | Bengali         |
| English        | Hindi           |
| Hindi          | Hindi           |
| Hindi          | English         |
| Hindi          | Bengali         |

---

# 📸 Demo Showcase
<img width="1433" height="840" alt="Screenshot 2026-05-21 at 2 29 07 AM" src="https://github.com/user-attachments/assets/278d5a89-dbd0-42cb-804f-91f22bc1780e" />

<img width="1267" height="786" alt="Screenshot 2026-05-21 at 2 29 59 AM" src="https://github.com/user-attachments/assets/66c50a90-dc1a-460b-ad55-bf66ee6a4f2f" />

<img width="1319" height="791" alt="Screenshot 2026-05-21 at 2 33 00 AM" src="https://github.com/user-attachments/assets/5caa520f-419c-42ad-99c4-ee2362c0b224" />

---

# 💡 Example Use Cases

* News Summarization
* Educational Content Summaries
* Cross-language Information Access
* AI Translation + Summarization
* Multilingual NLP Research

---

# 🔥 Key Engineering Highlights

* Lazy Model Loading
* GPU/CPU Auto Detection
* Translation Bridge Architecture
* Efficient Chunk Processing
* LRU Caching for Faster Inference
* Hugging Face Transformers Integration
* Interactive AI UI using Gradio

---

# 📈 Future Improvements

* Add More Languages
* Speech-to-Text Support
* PDF Upload Support
* Deploy using Docker & AWS
* User Authentication
* API Endpoints using FastAPI

---

# 👨‍💻 Author

Ujjwal Manikya Nath
