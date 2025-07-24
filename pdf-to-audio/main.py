import os
import fitz  # PyMuPDF
import pyttsx3
from gtts import gTTS
import datetime

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        page_text = page.get_text()
        if page_text.strip():
            text += page_text + "\n"
    return text

# Speak text out loud
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# Save text to MP3
def save_as_mp3(text, output_folder):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"audio_{timestamp}.mp3"
    filepath = os.path.join(output_folder, filename)

    tts = gTTS(text=text, lang='en')
    tts.save(filepath)
    print(f"✅ MP3 saved to: {filepath}")

# Main logic
if __name__ == "__main__":
    pdf_path = os.path.join(
        os.path.expanduser("~"),
        "Documents",
        "python developer internship",
        "pdf-to-audio",
        "sample.pdf"
    )

    if not os.path.exists(pdf_path):
        print("❌ File not found:", pdf_path)
    else:
        print("✅ File found:", pdf_path)
        text = extract_text_from_pdf(pdf_path)
        print("\n📄 PDF Content Preview:\n")
        print(text[:500])
        
        print("\n🔊 Speaking the text...\n")
        speak_text(text)

        output_dir = os.path.join(
            os.path.expanduser("~"),
            "Documents",
            "python developer internship",
            "pdf-to-audio",
            "output_audio"
        )
        os.makedirs(output_dir, exist_ok=True)

        save_as_mp3(text, output_dir)
