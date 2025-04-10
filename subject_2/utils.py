import os
import requests
from typing import List


def get_re_rank_data_by_jina(query: str, datas: List[str], relevance_score: float = 75.0, top_n: int = 3) -> List[str]:
    url = 'https://api.jina.ai/v1/rerank'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("JINA_API_KEY")}',
    }

    payload = {
        "model": "jina-reranker-v2-base-multilingual",
        "query": query,
        "top_n": top_n,
        "documents": datas,
        "return_documents": True
    }

    response = requests.post(url, headers=headers, json=payload)

    return [tmp["document"]["text"] for tmp in response.json()["results"] if tmp["relevance_score"] >= relevance_score]
