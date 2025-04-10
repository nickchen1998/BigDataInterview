import json

from langchain_openai import ChatOpenAI
from tools import analyze_ptt_keywords
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage

if __name__ == '__main__':
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    llm = ChatOpenAI(model="gpt-4o").bind_tools([analyze_ptt_keywords])

    messages = []
    # human_message = HumanMessage(content="請幫我分析 PTT 八卦版的熱門關鍵字")  # 會成功調用的例子
    human_message = HumanMessage(content="你好，你是誰？")  # 不會調用的例子
    ai_message = llm.invoke([human_message])

    if ai_message.tool_calls:
        for tool_call in ai_message.tool_calls:
            if tool_call["name"] == "analyze_ptt_keywords":
                tool_result = analyze_ptt_keywords.invoke(tool_call.get("args"))
                messages.append(ai_message)
                messages.append(ToolMessage(
                    content=json.dumps(tool_result),
                    tool_call_id=tool_call["id"],
                ))
                messages.append(human_message)
        print(llm.invoke(messages).content)

    else:
        print(ai_message.content)