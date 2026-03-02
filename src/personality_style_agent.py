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

# Messages history list
messages = []

# System prompt => Tell Claude how to answer, personality, style of answers, ...etc.
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

# Continous chat loop with history context
while True:
    message = input("You: ")
    if (message == "exit"):
        break

    # Add user input message in to the history list
    messages.append({"role": "user", "content": message})

    # Request Claude API with Parameters and Message
    reply = client.messages.create(
        model = model,
        max_tokens = max_tokens,
        system = system_prompt,
        messages = messages
    ).content[0].text

    # Add assistant reply message in to the history list
    messages.append({"role": "assistant", "content": reply})
    print("Claude:", reply)
