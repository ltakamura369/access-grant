import os
from anthropic import Anthropic

# APIキーを環境変数から取得
client = Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

# Claudeにリクエスト
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "こんにちは。日本語で自己紹介してください。"
        }
    ]
)

# Claudeの回答を表示
print(response.content[0].text)
