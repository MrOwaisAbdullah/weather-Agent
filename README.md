# AI Agent with Chainlit: Weather Info App

This repository contains the code for an AI agent showcased in a YouTube video tutorial, "Developing Your First AI Agent for Free Using OpenAI Agents SDK". This project lets you build a smart assistant that fetches real-time weather information via a chat interface and how to deploy it for free on Hugging Face Spaces. Perfect for beginners and AI enthusiasts, it uses free tools and offers a practical introduction to AI development!

## Folder Structure

```
weather-agent/                  # Main source code
├── agent.py              # Core AI agent logic using OpenAI Agents SDK
├── app.py                # Chainlit frontend for the chat interface
├── tool.py               # Custom tool to fetch weather data
├── README.md             # This file
├── pyprject.toml         # Project dependencies managed by UV
├── .gitignore            # Git ignore file
```

## Project Overview

This app demonstrates how to create an AI agent that answers weather-related queries using the **OpenAI Agents SDK**, fetches data with **WeatherAPI**, and provides an interactive frontend via **Chainlit**. Managed with **UV** for dependency handling, it’s deployable on **Hugging Face Spaces**. Follow the video tutorial to see the step-by-step process, from setup to deployment.

## Prerequisites
- Python 3.8+ installed.
- A free Gemini API key (get it from [Google AI Studio](https://aistudio.google.com/)).
- A free WeatherAPI key (sign up at [WeatherAPI](https://www.weatherapi.com/)).
- UV package manager (`pip install uv`).

## Environment Variables
- GEMINI_API_KEY="your_gemini_api_key"
- WEATHER_API_KEY="your_weather_api_key"

## How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MrOwaisAbdullah/weather-agent.git
   cd AI-Agent-Weather
   ```
2. **Set Up Environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r pyproject.toml
   ```
3. **Add API Keys**:
   - Insert your OpenAI and WeatherAPI keys in `weather_agent.py` or set as environment variables.
4. **Run the Agent**:
   ```bash
   uv run weather_agent.py
   ```
5. **Run the Chainlit Frontend**:
   ```bash
   uv run chainlit run main.py -w
   ```


## Connect with Me
- **YouTube**: [https://www.youtube.com/@MrOwaisAbdullah](https://www.youtube.com/@MrOwaisAbdullah) (Watch the full tutorial here!)
- **GitHub**: [https://github.com/MrOwaisAbdullah](https://github.com/MrOwaisAbdullah) (Explore my other projects)
- **Twitter/X**: [https://x.com/MrOwaisAbdullah](https://x.com/MrOwaisAbdullah) (Follow for tech tips)
- **LinkedIn**: [https://www.linkedin.com/in/mrowaisabdullah/](https://www.linkedin.com/in/mrowaisabdullah/) (Let’s connect professionally)

Star this repo, try the code, and drop your feedback or ideas in the video comments. Let’s build the future of AI together!

## License
This project is licensed under the MIT License.