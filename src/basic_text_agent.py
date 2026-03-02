from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv(override=True)
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic()
model = "claude-sonnet-4-0"
max_tokens = 100

while True:
    message = input("You: ")
    if (message == "exit"):
        break
    reply = client.messages.create(
        model = model,
        max_tokens = max_tokens,
        messages = [
                {
                "role": "user",
                "content": message
            }
        ]
    )
    print("Claude:", reply.content[0].text)
