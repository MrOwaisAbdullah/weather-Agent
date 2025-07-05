import chainlit as cl
from agents import Runner
from weather_agent import weather_agent

@cl.on_chat_start
def chat_start():
    cl.user_session.set("conversation_history", [])


@cl.on_message
async def main(message: cl.message):
    history = cl.user_session.get("conversation_history", [])

    history.append({"role": "user", "content": message.content })

    thinking_msg = await cl.Message(content="Thinking...").send()

    result = await Runner.run(
        weather_agent,
        history
    )

    history.append({"role": "system", "content": result.final_output })

    await thinking_msg.remove()
    await cl.Message(content=result.final_output).send()