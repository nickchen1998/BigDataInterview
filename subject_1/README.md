# 題目要求

### 🎯 目標

開發一個專門回答舆情分析相關問題的聊天機器人，並確保其具備適當的資訊檢索與分析能力。

### ✅ 任務要求

1. **回應範圍**
    - 機器人應僅回答與舆情分析相關的問題，對於無關問題應適當拒答。
    - 可使用任何 AI Agent 框架（如 LangChain、LangFlow、PydanticAI 等）。

2. **網路新聞分析**
    - 機器人應能根據使用者的問題爬取網路新聞，並對新聞內容進行分析。
    - 根據使用者的問題，查詢 1～10 則網路新聞。
    - 回應內容應包含：新聞標題、發布時間、內文、摘要、情緒分析結果、NER（命名實體識別）結果。

# 專案說明

## 專案結構

subject_1/

├── `__init__.py`

├── `crawlers.py   `    # 👉 爬蟲：爬取最新文章清單 & 抓主文內容

├── `extractors.py`     # 👉 關鍵字提取模組 with jieba

├── `main.py`     # 👉 主程式，呼叫 tools 進行 demo

├── `README.md`     # 👉 專案說明文件

├── `tools.py`          # 👉 將爬蟲與關鍵字提取模組結合，並透過 LangChain 的 Tool 物件建立一個 Tool

├── `utils.py`     # 👉 文字清洗、斷詞等輔助工具

## 成果說明

- 相關問題可成功調用爬蟲，並獲取熱門關鍵字

   ![成功結果](https://github.com/nickchen1998/BigDataInterview/blob/main/assests/subject_1_success_call_tools.png?raw=true)

- 無關問題可略過並直接回答使用者問題

   ![無關問題](https://github.com/nickchen1998/BigDataInterview/blob/main/assests/subject_1_failed_call_tools.png?raw=true)