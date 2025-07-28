# ai_provider.py

import os
from openai import OpenAI

class AIProvider:
    def __init__(self):
        # 初始化 OpenAI 客户端
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com/v1"  # DeepSeek 的接口地址
        )

    def chat(self, user_input):
        # 发起对话请求
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=100,
            temperature=0.3
        )
        return response.choices[0].message.content

# 示例用法
if __name__ == "__main__":
    ai_provider = AIProvider()
    user_input = "用 Python 写一行代码计算 1+1"
    response = ai_provider.chat(user_input)
    print(response)