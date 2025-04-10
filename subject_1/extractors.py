from collections import Counter
from utils import clean_text, tokenize


def extract_top_keywords(docs: list[str], top_k: int = 5) -> list[dict]:
    words = []
    for doc in docs:
        clean = clean_text(doc)
        tokens = tokenize(clean)
        words.extend(tokens)
    counter = Counter(words)
    top = counter.most_common(top_k)
    return [{"word": w, "count": c} for w, c in top]
