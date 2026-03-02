from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv(override=True)
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic()
model = "claude-sonnet-4-0"
max_tokens = 50
messages = []

while True:
    message = input("You: ")
    if (message == "exit"):
        break
    messages.append({"role": "user", "content": message})
    reply = client.messages.create(
        model = model,
        max_tokens = max_tokens,
        messages = messages
    ).content[0].text
    messages.append({"role": "assistant", "content": reply})
    print("Claude:", reply)
