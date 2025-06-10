import random

# --- Algoritmo de Ordenamiento: Selection Sort (Ordenamiento por Selección) ---
# Fácil de entender: encuentra el más chico y lo pone en su lugar.

def ordenar_notas_por_seleccion(lista_notas):
    """
    Ordena una lista de notas de menor a mayor usando el ordenamiento por selección.
    Es como buscar la nota más baja y moverla al principio de la lista.
    """
    n = len(lista_notas)
    for i in range(n):
        # Suponemos que el elemento actual es el más pequeño
        indice_minimo = i
        # Recorremos el resto de la lista para encontrar el verdadero mínimo
        for j in range(i + 1, n):
            if lista_notas[j] < lista_notas[indice_minimo]:
                indice_minimo = j
        # Intercambiamos el elemento actual con el más pequeño encontrado
        lista_notas[i], lista_notas[indice_minimo] = lista_notas[indice_minimo], lista_notas[i]
    return lista_notas

# --- Algoritmo de Búsqueda: Binary Search (Búsqueda Binaria) ---
# ¡Solo funciona si la lista YA está ordenada!

def buscar_nota_binario(lista_ordenada, nota_buscada):
    """
    Busca una nota en una lista que ya está ordenada usando la búsqueda binaria.
    Cada vez, se descarta la mitad de las opciones, haciendo la búsqueda muy eficiente.
    """
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        # Comparamos la nota del medio con la que buscamos
        if lista_ordenada[medio] == nota_buscada:
            return medio  # ¡Encontrada! Devolvemos su posición (índice)
        elif lista_ordenada[medio] < nota_buscada:
            izquierda = medio + 1  # La nota buscada está a la derecha del medio
        else:
            derecha = medio - 1  # La nota buscada está a la izquierda del medio
            
    return -1  # La nota no se encontró en la lista

# --- Función principal para mostrar el funcionamiento ---

def main_notas():
    print("--- Mi Pequeño Gestor de Notas de Alumnos ---")

    # 1. Generamos una lista de notas de ejemplo (entre 1 y 10)
    notas_clase_originales = [random.randint(1, 10) for _ in range(12)] # 12 notas para ver bien
    print(f"\nNotas de la clase (desordenadas): {notas_clase_originales}")

    # 2. Ordenamos las notas con el Algoritmo de Selección
    print("\n--- Paso 1: Ordenando las notas (Usando Selection Sort) ---")
    # Hacemos una copia para no cambiar la lista original
    notas_para_ordenar = list(notas_clase_originales) 
    
    notas_ordenadas = ordenar_notas_por_seleccion(notas_para_ordenar)
    
    print(f"Notas ordenadas (de menor a mayor): {notas_ordenadas}")

    # 3. Buscamos una nota específica usando Búsqueda Binaria
    print("\n--- Paso 2: Buscando una nota (Usando Búsqueda Binaria) ---")

    # Elegimos una nota que sabemos que existe en la lista ordenada
    nota_a_buscar_existente = notas_ordenadas[random.randint(0, len(notas_ordenadas) - 1)]
    # Elegimos una nota que seguramente no existe (fuera del rango 1-10)
    nota_a_buscar_inexistente = 77

    print(f"\nIntentando buscar la nota: {nota_a_buscar_existente}")
    posicion_encontrada = buscar_nota_binario(notas_ordenadas, nota_a_buscar_existente)

    if posicion_encontrada != -1:
        print(f"¡Genial! La nota {nota_a_buscar_existente} SÍ está. La encontramos en la posición (índice) {posicion_encontrada}.")
    else:
        print(f"Ups... La nota {nota_a_buscar_existente} NO se encontró en la lista.")

    print(f"\nIntentando buscar una nota que no existe: {nota_a_buscar_inexistente}")
    posicion_no_encontrada = buscar_nota_binario(notas_ordenadas, nota_a_buscar_inexistente)

    if posicion_no_encontrada != -1:
        print(f"¡Ups! Se encontró una nota {nota_a_buscar_inexistente} que no debería existir en la posición {posicion_no_encontrada}.")
    else:
        print(f"Como esperábamos, la nota {nota_a_buscar_inexistente} NO se encontró en la lista.")
    
    print("\n--- ¡Hemos terminado la demostración! ---")

if __name__ == "__main__":
    main_notas()