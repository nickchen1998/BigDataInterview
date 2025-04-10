import re
import jieba


def clean_text(text: str) -> str:
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9]", " ", text)
    return text


def tokenize(text: str) -> list[str]:
    tokens = jieba.lcut(text)
    return [t for t in tokens if len(t) > 1]
