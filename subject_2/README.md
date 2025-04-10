# 題目要求

### 🎯 目標

開發一個能檢索 KEYPO 功能手冊（詳見附件）的聊天機器人，確保其能基本相關資料提供準確的回答。

### ✅ 任務要求

**文件檢索與回答**
- 機器人應能檢索 KEYPO 功能手冊以回答相關問題。
- 建立 RAG（Retrieval-Augmented Generation）流程，確保機器人能根據功能手冊內容進行準確回應。
- 若知識庫內無相關內容，機器人應避免產生幻覺（Hallucination），不得提供不實或無依據的回答。

# 專案說明

若需要執行請務必於此專案根目錄之外建立 `.env` 檔案，並在其中加入以下環境變數：

```dotenv
OPENAI_API_KEY="your_openai_api_key"
JINA_API_KEY="your_jina_api_key"
```

JINA 的部分主要會使用到其提供的 Rerank 服務，若無則直接將 `main.py` 當中的 28 ~ 32 行註解掉即可。

## 專案結構

subject_2/

├── `__init__.py`

├── `README.md`     # 👉 專案說明文件

├── `main.py`    # 👉 專案主程式

├── `utils.py`     # 👉 主要存放 Rerank 函式

## 成果說明

- 為節省資源，使用 InMemoryVectorStore 直接將向量儲存在記憶體當中。
- 使用 Jina 的 Rerank 服務進行向量檢索，並將設定門檻值剔除較無關聯之段落，以提升回答精確度。

下方為問答結果：

```python
query = "什麼是熱門 Hashtag？"
answer = "熱門Hashtag是指在相關文章中統計每個Hashtag的出現次數，然後按照次數排序，並以直方圖展示每個Hashtag的熱門程度的一種分析工具。它可以透過篩選文章的情感類別（如全部、僅正面、僅中立、僅負面）和文章類型（如全部、僅主文、僅回文）來進行進階篩選，並且可以手動編輯分析結果。"
```