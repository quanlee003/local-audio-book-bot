from pathlib import Path
from vieneu import Vieneu
import numpy as np
import soundfile as sf

BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

print("📢 Loading VieNeu TTS model...")
tts = Vieneu(
    backbone_repo="pnnbao-ump/VieNeu-TTS",
    backbone_device="cuda",
    codec_device="cuda"
)
print("✅ Model loaded!")

def tts_chunks(chunks, output_filename="chapter.wav", sample_rate=22050):
    all_audio = []
    chunks = [c for c in chunks if c.strip()]
    print(f"Generating TTS for {len(chunks)} chunks...")
    for i, chunk in enumerate(chunks, 1):
        print(f"  Chunk {i}/{len(chunks)} ({len(chunk)} chars)")
        wav = tts.infer(chunk)
        wav = np.asarray(wav, dtype=np.float32).flatten()
        all_audio.append(wav)
    final_audio = np.concatenate(all_audio)
    output_path = OUTPUT_DIR / output_filename
    sf.write(output_path, final_audio, samplerate=sample_rate)
    print(f"✅ Audio saved: {output_path}")
    return output_path
