from pathlib import Path
import numpy as np
import soundfile as sf

from scraper.scrape import scrape_chapter
from text.text_preprocess import preprocess_text
from tts.tts_engine import tts

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def synthesize_chunk(chunk: str, sample_rate=22050) -> np.ndarray:
    """
    Export 1 audio chunk VieNeu TTS
    """
    if not chunk.strip():
        return np.array([], dtype=np.float32)
    
    wav = tts.infer(chunk)  # VieNeu return np.ndarray
    wav = np.asarray(wav, dtype=np.float32).flatten()
    return wav

def main():
    print("=== Local Audiobook Chatbot (VieNeu only) ===")
    url = input("Enter URL: ").strip()

    if url:
        try:
            text = scrape_chapter(url)
        except Exception as e:
            print(f"[ERROR] Can't scrape: {e}")
            return
        Path("scraper/text.txt").write_text(text, encoding="utf-8")
        print("[INFO] Save text scrape successful!")
    else:
        text_file = Path("scraper/text.txt")
        if not text_file.exists():
            print("[ERROR] File scraper/text.txt does not exist!")
            return
        text = text_file.read_text(encoding="utf-8")
        print("[INFO] Reading text from scraper/text.txt")

    # Split text into small chunks
    chunks = preprocess_text(text, max_chars=300)
    print(f"[INFO] Total chunks: {len(chunks)}")

    all_audio = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}/{len(chunks)} ({len(chunk)} chars)")
        wav_chunk = synthesize_chunk(chunk)
        all_audio.append(wav_chunk)

    if all_audio:
        final_audio = np.concatenate(all_audio)
        output_file = OUTPUT_DIR / "audiobook.wav"
        sf.write(output_file, final_audio, samplerate=22050)
        print(f"[INFO] Done! File audio at {output_file}")
    else:
        print("[ERROR] No audio file being created!")

if __name__ == "__main__":
    main()
