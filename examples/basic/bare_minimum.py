# Un ejemplo mínimo que muestra la configuración básica de un agente.
# Uso : configura un agente que responde a un mensaje de usuario simple.
from swarm import Swarm, Agent
from dotenv import load_dotenv

load_dotenv()
client = Swarm()

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
