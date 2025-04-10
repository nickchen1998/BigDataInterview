from langchain.tools import tool
from crawlers import fetch_articles_from_page
from extractors import extract_top_keywords


@tool
def analyze_ptt_keywords(board_name: str) -> dict:
    """
    截取並分析 PTT 指定版面的最新消息並輸出熱門關鍵字。
    目前支援的版面有：八卦、電影、股票、旅遊、遊戲。
    若不指定版面，預設為八卦版。
    :param board_name: 版面名稱
    """
    bord_url_dict = {
        "八卦": "https://www.ptt.cc/bbs/Gossiping/index.html",
        "電影": "https://www.ptt.cc/bbs/movie/index.html",
        "股票": "https://www.ptt.cc/bbs/Stock/index.html",
        "旅遊": "https://www.ptt.cc/bbs/Travel/index.html",
        "遊戲": "https://www.ptt.cc/bbs/game/index.html",
    }

    articles = fetch_articles_from_page(bord_url_dict.get(board_name, bord_url_dict["八卦"]))
    top_keywords = extract_top_keywords(articles, top_k=5)
    return {
        "top_keywords": top_keywords,
        "total_articles": len(articles),
        "summary": f"共分析 {len(articles)} 篇文章，熱門關鍵字為：" +
                   "、".join([kw["word"] for kw in top_keywords])
    }
