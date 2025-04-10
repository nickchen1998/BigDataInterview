import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"cookie": "over18=1"}


def fetch_articles_from_page(index_url: str) -> list[str]:
    res = requests.get(index_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select("div.title a")

    contents = []
    for a in links:
        href = a.get("href")
        full_url = f"https://www.ptt.cc{href}"
        content = fetch_single_post(full_url)
        if content:
            contents.append(content)
        sleep(0.3)

    return contents


def fetch_single_post(post_url: str) -> str:
    res = requests.get(post_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    main_content = soup.find(id="main-content")
    # 移除 meta 與留言
    for tag in main_content.select("div.article-metaline") + main_content.select("div.push"):
        tag.decompose()
    text = main_content.get_text()
    return text.strip()
