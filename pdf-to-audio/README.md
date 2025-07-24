# PDF to Audiobook Converter 🎧

## 📌 Overview
This Python app converts the text content of a PDF into spoken audio. It uses a GUI-less setup for file handling and speech generation, with an option to save the audio as an MP3 file.

## 🛠 Tools Used
- Python
- PyMuPDF (`fitz`) – PDF text extraction
- pyttsx3 – Offline text-to-speech
- gTTS – MP3 export (Google Text-to-Speech)

## 🚀 How It Works
1. Loads and reads text from a PDF
2. Speaks it using the system voice
3. Saves the audio as `output_audio/audio_<timestamp>.mp3`

## ▶️ How to Run
```bash
python main.py
