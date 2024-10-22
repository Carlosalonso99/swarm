
# Swarm básico

Esta carpeta contiene ejemplos básicos que demuestran las capacidades principales de Swarm. Estos ejemplos muestran las implementaciones más sencillas de Swarm, con un mensaje de entrada y una salida correspondiente. El archivo `simple_loop_no_helpers` contiene un bucle `while` para demostrar cómo crear una sesión interactiva con Swarm.

### Ejemplos

1. **agent_handoff.py**

   - Demuestra cómo transferir una conversación de un agente a otro.
   - **Uso**: Transfiere usuarios de habla hispana de un agente en inglés a un agente en español.

2. **bare_minimum.py**

   - Un ejemplo mínimo que muestra la configuración básica de un agente.
   - **Uso**: Configura un agente que responde a un mensaje simple del usuario.

3. **context_variables.py**

   - Muestra cómo usar variables de contexto dentro de un agente.
   - **Uso**: Utiliza variables de contexto para saludar a un usuario por su nombre e imprimir detalles de la cuenta.

4. **function_calling.py**

   - Demuestra cómo definir y llamar funciones desde un agente.
   - **Uso**: Configura un agente que puede responder con información meteorológica para una ubicación dada.

5. **simple_loop_no_helpers.py**
   - Un ejemplo de un bucle de interacción simple sin utilizar funciones de ayuda.
   - **Uso**: Configura un bucle donde el usuario puede interactuar continuamente con el agente, imprimiendo la conversación.

## Ejecutar los ejemplos

Para ejecutar cualquiera de los ejemplos, utiliza el siguiente comando:

```shell
python3 <nombre_del_ejemplo>.py
```
