# Demuestra cómo definir y llamar funciones desde un agente.
# Uso : configura un agente que puede responder con información meteorológica para una ubicación determinada.
from swarm import Swarm, Agent
from dotenv import load_dotenv

load_dotenv()
client = Swarm()


def get_weather(location) -> str:
    return "{'temp':67, 'unit':'F'}"


agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
    functions=[get_weather],
)

messages = [{"role": "user", "content": "What's the weather in NYC?"}]

response = client.run(agent=agent, messages=messages)
print(response.messages[-1]["content"])
