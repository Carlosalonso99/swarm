from swarm import Agent
from functions import ingest_data, clean_data, analyze_data


def instructions(context_variables):
    data = context_variables.get("data")
    return f"Determina qué agente es el más adecuado para gestionar la solicitud del usuario y transfiere la conversación a ese agente."

context_variables = {"data":""}

# Agente CDO (Chief Data Officer)
cdo_agent = Agent(
    name="CDO Agent",
    instructions=instructions,
    functions=[]  # Las funciones de transferencia se añaden más adelante
    
)

# Agente de Ingesta de Datos
ingest_agent = Agent(
    name="Ingest Agent",
    instructions="Ayuda al usuario a ingestar los datos convirtiendo un CSV en un DataFrame. Cuando realices tu tarea vuelve al CDO Agent",
    functions=[ingest_data]  # Añadir la función de ingesta de datos
)

# Agente de Limpieza de Datos
clean_agent = Agent(
    name="Clean Agent",
    instructions="Ayuda al usuario a limpiar los datos eliminando duplicados y filas con valores nulos.Cuando realices tu tarea vuelve al CDO Agent",
    functions=[clean_data]  # Añadir la función de limpieza de datos
)

# Agente de Análisis de Datos
analyze_agent = Agent(
    name="Analyze Agent",
    instructions="Ayuda al usuario a analizar los datos de una columna especificada (Calcula la media, mediana y moda).Cuando realices tu tarea vuelve al CDO Agent",
    functions=[analyze_data]  # Añadir la función de análisis de datos
)

# Funciones para transferir la conversación entre los agentes
def transfer_back_to_cdo(context_variables):
    """Cuando el agente no tiene en sus instrucciones deallada la tarea que le pide el usuario, transfiere de vuelta al agente CDO cuando ."""
    return cdo_agent

def transfer_to_ingest(context_variables):
    """Transfiere al agente de ingesta de datos si el usuario da una instruccion de ingesta."""
    return ingest_agent

def transfer_to_clean(context_variables):
    """Transfiere al agente de limpieza de datos si el usuario da una instruccion de limpieza."""
    return clean_agent

def transfer_to_analyze(context_variables):
    """Transfiere al agente de análisis de datos si el usuario da una instruccion de analisis."""
    return analyze_agent

# Asignar las funciones de transferencia al agente CDO
cdo_agent.functions = [transfer_to_ingest, transfer_to_clean, transfer_to_analyze]

# Asegurarse de que los agentes pueden transferir de vuelta al CDO si no pueden manejar la tarea
ingest_agent.functions.append(transfer_back_to_cdo)
clean_agent.functions.append(transfer_back_to_cdo)
analyze_agent.functions.append(transfer_back_to_cdo)

