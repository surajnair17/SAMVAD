import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import whisper
from googletrans import Translator

# -------------------------
# LOAD MODELS (ONLY ONCE)
# -------------------------

print("Loading Whisper model...")
model = whisper.load_model("small")  # good balance

translator = Translator()

fs = 16000
seconds = 5  # shorter = faster

# -------------------------
# MAIN LOOP
# -------------------------

while True:
    print("\n🎤 Speak now (Ctrl+C to stop):")

    # Record audio
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    # Normalize audio
    if np.max(np.abs(audio)) != 0:
        audio = audio / np.max(np.abs(audio))

    # Save file
    write("output.wav", fs, audio)

    print("Processing...")

    # Transcribe + detect language
    result = model.transcribe(
        "output.wav",
        task="transcribe",
        fp16=False
    )

    text = result["text"].strip()
    detected_lang = result["language"]

    print("\n🧠 Detected Language:", detected_lang)
    print("📝 Text:", text)

    # -------------------------
    # SMART TRANSLATION
    # -------------------------

    if detected_lang == "hi":
        try:
            translated = translator.translate(text, src='hi', dest='en')
            print("🌍 English:", translated.text)
        except:
            print("⚠️ Translation failed")

    elif detected_lang == "en":
        print("✅ Already in English")

    else:
        print("⚠️ Unsupported language (for now)")