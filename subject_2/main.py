import utils
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.docstore.document import Document
from langchain_openai.chat_models import ChatOpenAI
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

# 專案 init
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
target_file = Path(__file__).resolve().parent / "KEYPO功能手冊文件.md"
with open(target_file, "r", encoding="utf-8") as f:
    markdown_content = f.read()

# 切割文件並寫入向量資料庫
documents = [Document(page_content=markdown_content)]
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=10)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = InMemoryVectorStore.from_documents(
    text_splitter.split_documents(documents),
    embedding=embeddings
)

# 搜尋相關段落
query = "什麼是熱門 Hashtag？"
references = vectorstore.similarity_search(query=query, k=3)
re_ranked_references = utils.get_re_rank_data_by_jina(
    query=query,
    datas=[doc.page_content for doc in references],
    relevance_score=0.4,
)

# 製作 Prompt
system_message = SystemMessage(content=f"""你是一個操作手冊小幫手，請根據以下文件內容回答問題，回答問題時請注意下列規則：
1. 你只能根據文件內容回答問題，不能使用其他資料來源。
2. 你只能回答與文件內容相關的問題，不能回答其他問題。
3. 你必須使用繁體中文回答問題。
4. 如果參考資料不足以回答問題，或是沒有參考資料的話，請回答「抱歉，我無法回答這個問題。」。

下方為參考資料列表：
{'---'.join(re_ranked_references)}
""")
human_message = HumanMessage(content=query)

# 進行對話
llm = ChatOpenAI(model="gpt-4o")
ai_message = llm.invoke([system_message, human_message])
print(ai_message.content)
