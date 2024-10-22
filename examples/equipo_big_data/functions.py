import pandas as pd

def ingest_data(context_variables, file_path):
    """
    Carga un archivo CSV y lo guarda en las variables de contexto.
    """
    try:
        data = pd.read_csv(file_path)
        context_variables['data'] = data  # Guardar el DataFrame en el contexto
        print(f"Datos cargados desde {file_path}")
        
        return data
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def clean_data(context_variables):
    """
    Limpia el DataFrame eliminando duplicados y filas con valores nulos.
    """
    data = context_variables.get('data')

    if data is None:
        print("No se proporcionaron datos para limpiar.")
        return None

    # Eliminar duplicados y filas nulas
    data = data.drop_duplicates().dropna()
    
    context_variables['data'] = data  # Guardar el DataFrame en el contexto
    print("Datos limpiados: \n", data)
    print(data)
    return data

def analyze_data(context_variables, column):
    """
    Realiza un análisis estadístico básico de la columna especificada del DataFrame.
    Calcula la media, mediana y moda.
    """
    data = context_variables.get('data')

    if data is None or column not in data.columns:
        print(f"Error: No se encontraron los datos o la columna '{column}' no existe.")
        return None

    mean = data[column].mean()
    median = data[column].median()
    mode = data[column].mode().values[0] if not data[column].mode().empty else None

    print(f"Análisis de la columna '{column}':")
    print(f"Media: {mean}, Mediana: {median}, Moda: {mode}")

    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }
