from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Loading ANTHROPIC_API_KEY from .env file
load_dotenv(override=True)
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# Creating Anthropic SDK Client
client = Anthropic()

# Define the model to use
model = "claude-sonnet-4-0"

# Defining the maximum tokens length of answers
max_tokens = 50

# Continous chat loop
while True:
    message = input("You: ")
    if (message == "exit"):
        break

    # Request Claude API with Parameters and Message
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
