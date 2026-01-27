import re

def preprocess_text(text: str, max_chars: int = 300) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            punct_pos = max(
                text.rfind(".", start, end),
                text.rfind("!", start, end),
                text.rfind("?", start, end)
            )
            if punct_pos != -1 and punct_pos > start:
                end = punct_pos + 1
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end
    return chunks
