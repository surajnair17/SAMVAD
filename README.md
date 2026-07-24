# SAMVAD — Real-Time Hindi→English Speech Translator

Speak Hindi, hear English. SAMVAD runs one continuous loop:

```
microphone (SoundDevice) → transcription + language detection (OpenAI Whisper)
→ translation (Google Translate API) → spoken English output (Pyttsx3)
```


## Features

- Speech-to-text with OpenAI Whisper
- Automatic language detection
- Hindi → English translation
- Voice output (text-to-speech)
- Runs as a single continuous listen → translate → speak loop

## Tech stack

Python · OpenAI Whisper · Google Translate API · Pyttsx3 · SoundDevice

## Run it

```bash
pip install -r requirements.txt
python main.py
```

Requires a working microphone. First run downloads the Whisper model.

## Roadmap

- Real-time streaming for lower latency
- Web UI (Streamlit)
- Multi-language support

## Author

**Suraj** — [GitHub](https://github.com/surajnair17) · [LinkedIn](https://www.linkedin.com/in/suraj-ss2038)
