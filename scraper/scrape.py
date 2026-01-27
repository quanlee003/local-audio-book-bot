import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def scrape_chapter(url: str) -> str:
    res = requests.get(url, headers=HEADERS, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, "html.parser")
    article = soup.find("article")
    if not article:
        raise RuntimeError("Article not found")
    paragraphs = []
    for p in article.find_all("p"):
        text = p.get_text(strip=True)
        if not text:
            continue
        if "Chương" in text and len(text) < 30:
            continue
        if "Nguồn" in text:
            continue
        paragraphs.append(text)
    return "\n\n".join(paragraphs)
