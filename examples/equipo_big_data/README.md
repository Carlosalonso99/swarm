# Contenido del README explicando el flujo de agentes y el cambio de contexto
readme_content = """
# Sistema de Análisis de Datos con Agentes en Swarm

Este proyecto utiliza agentes orquestados con **Swarm** para realizar tareas relacionadas con la ingesta, limpieza y análisis de datos. Los agentes se comunican entre sí y transfieren tareas según las solicitudes del usuario. Las variables de contexto se utilizan para compartir el estado de los datos a lo largo del flujo de trabajo.

## Descripción de los agentes:

1. **Agente de Ingesta (Ingest Agent)**: 
   - Carga un archivo CSV y lo convierte en un DataFrame. 
   - Guarda el DataFrame en las `context_variables` para que otros agentes puedan acceder a él.

2. **Agente de Limpieza (Clean Agent)**: 
   - Elimina duplicados y valores nulos del DataFrame.
   - Actualiza el DataFrame limpio en las `context_variables`.

3. **Agente de Análisis (Analyze Agent)**: 
   - Realiza un análisis estadístico básico (media, mediana, moda) sobre una columna especificada del DataFrame.

4. **Agente CDO (Chief Data Officer)**: 
   - Determina qué agente debe manejar la solicitud del usuario y transfiere la conversación según el caso.

## Flujo de trabajo:

1. El usuario ingresa un archivo CSV mediante el **Agente de Ingesta**, que convierte el archivo en un DataFrame.
2. Si se solicita, la conversación se transfiere al **Agente de Limpieza**, que limpia los datos.
3. Finalmente, el **Agente de Análisis** se encarga de realizar cálculos estadísticos en una columna específica.
4. El flujo entre los agentes se gestiona mediante **context_variables**, lo que permite compartir el estado de los datos.

## Ejecución

Para ejecutar el sistema, asegúrate de tener un archivo CSV disponible. Aquí un ejemplo de cómo puedes interactuar con los agentes:

```bash
# Ejecutar ingesta de datos
python run.py

```