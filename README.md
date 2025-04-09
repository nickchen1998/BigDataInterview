# AI 軟體工程師面試考題：舆情分析 Agent 開發

- 請根據以下題目要求完成任務，技術框架不限，但需確保功能正常可運行。
- 完成後請推上 GitHub，並分享連結，及撰寫完整清楚的 README 文件方便我們測試運行。

---

## 題目 1：舆情分析聊天機器人

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

---

## 題目 2：文件檢索聊天機器人（RAG 知識庫整合）

### 🎯 目標
開發一個能檢索 KEYPO 功能手冊（詳見附件）的聊天機器人，確保其能基本相關資料提供準確的回答。

### ✅ 任務要求

1. **文件檢索與回答**
   - 機器人應能檢索 KEYPO 功能手冊以回答相關問題。
   - 建立 RAG（Retrieval-Augmented Generation）流程，確保機器人能根據功能手冊內容進行準確回應。
   - 若知識庫內無相關內容，機器人應避免產生幻覺（Hallucination），不得提供不實或無依據的回答。
