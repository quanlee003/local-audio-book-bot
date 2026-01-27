# Local Audiobook Chatbot

This project is a **personal TTS chatbot** that can:

* Scrape story chapters from a given URL.
* Convert text to audio using **VieNeu TTS** (Vietnamese + English proper nouns).
* Output a **WAV file** playable on any device.
* Accept either a URL input or use a pre-scraped `text.txt`.

---

## 📂 Folder Structure

```
AudioBookChatbot/
│
├─ main.py                # Main chatbot script
├─ output/                # Folder to save output audio files
├─ scraper/
│   ├─ scrape.py          # Script to scrape text from web pages
│   └─ text.txt           # Saved text from scraping
├─ tts/
│   ├─ tts_engine.py      # VieNeu TTS engine
├─ text/
│   └─ text_preprocess.py # Split text into chunks for TTS
└─ README.md
```

---

## ⚙️ Requirements

* Python >= 3.10
* Required Python packages:

```bash
pip install requests beautifulsoup4
pip install numpy soundfile
pip install pydub
pip install gTTS
pip install vieneu
```

* **Optional** (for advanced proper noun detection):

```bash
pip install spacy
python -m spacy download vi_core_news_lg
```

---

## 🏃‍♂️ How to Run

1. Run the chatbot:

```bash
python main.py
```

2. Enter the URL of the chapter you want to listen to. Example:

```
https://bapstory.net/tro-choi-vuong-quyen-1a-soi-tuyet-thanh-winterfell/12/
```

* Or leave it blank to use the pre-scraped `scraper/text.txt`.

3. The program will:

   * Split the text into small chunks.
   * Use VieNeu TTS to generate audio for each chunk.
   * Merge all chunks into a single audio file.

4. The final audio file will be saved at:

```
output/audiobook.wav
```

---

## 📝 File Descriptions

* `scraper/scrape.py` → Scrapes text from a URL and filters unnecessary lines like "Chapter" or "Source".
* `text/text_preprocess.py` → Splits long text into smaller chunks for smooth TTS processing.
* `tts/tts_engine.py` → Loads VieNeu TTS and converts text into numpy arrays representing audio.
* `main.py` → Main chatbot script: input URL → scrape → preprocess → TTS → merge WAV.

---

## 💡 Notes

* VieNeu TTS works well with Vietnamese text; English words in stories are reasonably pronounced.
* Audio chunks are merged directly to avoid noise issues.
* To improve proper noun pronunciation, you can integrate **NER** and use gTTS for English proper nouns (advanced version).

---

## ⚡ Next Steps

* Support multiple chapters consecutively to produce a full audiobook.
* Advanced version: detect **proper nouns, locations, names** → pronounce them accurately with gTTS.
* Add a GUI or web interface for easier URL input.

---
