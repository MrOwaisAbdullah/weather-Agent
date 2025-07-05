from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, set_tracing_disabled
from dotenv import load_dotenv
import os
import asyncio
from tools import get_weather

set_tracing_disabled(True)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=API_KEY,
)

model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash",
)

weather_agent = Agent(
    name="Weather Assistant",
    instructions="You are a weather assistant, response in scanable text, with relevant emojis, and in a way that is easy to understand. with proper spaces and line breaks.",
    model=model,
    tools=[get_weather],
)
