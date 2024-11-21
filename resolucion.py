def analizar_lista_reproduccion(top5, lista_reproduccion):
    # Validación de listas
    if not isinstance(top5, list) or not isinstance(lista_reproduccion, list):
        raise ValueError("Ambos parámetros deben ser listas.")
    
    # Tarea 1: Imprimir canciones con su orden
    print("Tarea 1: Canciones con orden:")
    for i, cancion in enumerate(lista_reproduccion, start=1):
        print(f"Se está escuchando {cancion} en orden {i}")
    
    # Tarea 2: Mensaje publicitario
    canciones_vistas = set()
    contador_no_repetidas = 0
    print("\nTarea 2: Mensaje publicitario:")
    for cancion in lista_reproduccion:
        if cancion not in canciones_vistas:
            contador_no_repetidas += 1
            canciones_vistas.add(cancion)
            if contador_no_repetidas % 3 == 0:
                print("Espacio publicitario")
    
    # Tarea 3: Canción más repetida
    from collections import Counter
    conteo_canciones = Counter(lista_reproduccion)
    cancion_mas_repetida = max(conteo_canciones, key=conteo_canciones.get)
    print("\nTarea 3: Canción más repetida:")
    print(f"La canción más escuchada es: {cancion_mas_repetida}")
    
    # Tarea 4: Porcentaje de canciones del TOP5
    canciones_en_top5 = [cancion for cancion in lista_reproduccion if cancion in top5]
    porcentaje_top5 = (len(set(canciones_en_top5)) / len(top5)) * 100
    print("\nTarea 4: Porcentaje de canciones del TOP5:")
    print(f"Porcentaje de canciones del TOP5: {porcentaje_top5}%")
    
    return porcentaje_top5


