import requests

# Función para conectarse a la API
def obtener_datos(tipo):
    url = 'https://api.le-systeme-solaire.net/rest/bodies/'
    params = {}

    if tipo == 'cometas':
        params['filter[]'] = 'isComet,eq,true'
    elif tipo == 'planetas':
        params['filter[]'] = 'isPlanet,eq,true'
    elif tipo == 'lunas':
        params['filter[]'] = 'aroundPlanet,ne,null'
    elif tipo == 'estrellas':
        params['filter[]'] = 'isStar,eq,true'
    elif tipo == 'asteroides':
        params['filter[]'] = 'isAsteroid,eq,true'
    elif tipo == 'planetas_enanos':
        params['filter[]'] = 'isDwarfPlanet,eq,true'

    try:
        respuesta = requests.get(url, params=params)
        respuesta.raise_for_status()  # Verificar si hubo algún error
        return respuesta.json()['bodies']
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API: {e}")
        return None

# Función para imprimir los datos de los cuerpos celestes
def mostrar_datos(datos):
    if datos:
        for cuerpo in datos:
            print(f"Nombre: {cuerpo['englishName']}")
            print(f"ID: {cuerpo['id']}")
            print(f"Tipo: {cuerpo['bodyType']}")
            print("-" * 40)
    else:
        print("No se encontraron datos.")

# Menú interactivo
def menu():
    opciones = {
        '1': 'planetas',
        '2': 'lunas',
        '3': 'estrellas',
        '4': 'asteroides',
        '5': 'cometas',
        '6': 'planetas_enanos'
    }

    while True:
        print("\nMenú de opciones:")
        print("1. Visualiza toda la información de planetas.")
        print("2. Visualiza toda la información de lunas.")
        print("3. Visualiza toda la información de estrellas.")
        print("4. Visualiza toda la información de asteroides.")
        print("5. Visualiza toda la información de cometas.")
        print("6. Visualiza toda la información de planetas enanos.")
        print("7. Salir.")

        opcion = input("Elige una opción: ")

        if opcion == '7':
            print("Saliendo del programa...")
            break

        if opcion in opciones:
            tipo = opciones[opcion]
            print(f"Obteniendo información sobre {tipo}...\n")
            datos = obtener_datos(tipo)
            mostrar_datos(datos)
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    menu()
