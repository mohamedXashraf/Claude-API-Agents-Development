from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv(override=True)
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic()
model = "claude-sonnet-4-0"
max_tokens = 100
