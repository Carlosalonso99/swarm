# Un ejemplo de un bucle de interacción simple sin utilizar funciones auxiliares.
# Uso : Configura un bucle donde el usuario puede interactuar continuamente con el agente, imprimiendo la conversación.
from swarm import Swarm, Agent
from dotenv import load_dotenv

load_dotenv()
client = Swarm()

my_agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)


def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")


messages = []
agent = my_agent
while True:
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(agent=agent, messages=messages)
    messages = response.messages
    agent = response.agent
    pretty_print_messages(messages)
