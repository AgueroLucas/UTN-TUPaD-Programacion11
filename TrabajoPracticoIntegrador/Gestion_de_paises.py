import csv
import os 
import unicodedata # <-- AÑADIDO: Para manejar acentos

# --- FUNCIONES DE VALIDACIÓN Y AUXILIARES ---

def normalizar_texto(texto):
    """
    Normaliza un texto: quita acentos y lo convierte a minúsculas.
    Ej: "América" -> "america"
    """
    # NFD: Normalization Form D (Canonical Decomposition)
    # Esto separa 'á' en 'a' y '´'
    try:
        s = unicodedata.normalize('NFD', texto)
        # 'Mn': Non-Spacing Mark (categoría para los acentos)
        # Se crea un nuevo string solo con los caracteres que NO son acentos
        s_sin_acentos = "".join(c for c in s if unicodedata.category(c) != 'Mn')
    except TypeError:
        # En caso de que el texto sea None o no sea un string
        return ""
    # Devolvemos en minúsculas
    return s_sin_acentos.lower()

def limpiar_pantalla():
    """Limpia la consola (simulado con saltos de línea para compatibilidad)."""
    print("\n" * 20)

def input_entero_positivo(mensaje):
    """Solicita un entero positivo al usuario. Valida la entrada."""
    while True:
        try:
            valor = input(mensaje)
            if valor.lower() == 'c': # Opción para cancelar
                return None
            
            numero = int(valor)
            if numero < 0:
                print("Error: El número debe ser positivo.")
            else:
                return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def mostrar_paises(lista_paises):
    """
    Muestra una lista de países de forma formateada.
    Maneja el caso de listas vacías.
    """
    if not lista_paises:
        print("\n--- No se encontraron países que cumplan con el criterio. ---")
        return

    print("\n--- Resultados de la Búsqueda ---")
    print(f"{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)':<18} | {'Continente':<15}")
    print("-" * 74)
    
    for pais in lista_paises:
        # Formateamos números con separadores de miles para legibilidad
        pob = f"{pais['poblacion']:,}"
        sup = f"{pais['superficie']:,}"
        print(f"{pais['nombre']:<20} | {pob:<15} | {sup:<18} | {pais['continente']:<15}")
    print("-" * 74)
    print(f"Total de países mostrados: {len(lista_paises)}")

# --- FUNCIONES PRINCIPALES (DATOS) ---

def crear_csv_predeterminado(archivo_csv):
    """
    Crea un archivo CSV con una lista predeterminada de países
    si el archivo no existe.
    Devuelve la lista de países creados.
    """
    print(f"Advertencia: Archivo '{archivo_csv}' no encontrado.")
    print("Creando archivo con datos predeterminados...")

    # Lista solicitada
    paises_predeterminados = [
        {'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'},
        {'nombre': 'EEUU', 'poblacion': 331893745, 'superficie': 9833520, 'continente': 'América'},
        {'nombre': 'Rusia', 'poblacion': 145934462, 'superficie': 17098242, 'continente': 'Europa/Asia'},
        {'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'},
        {'nombre': 'Italia', 'poblacion': 59110000, 'superficie': 301340, 'continente': 'Europa'},
        {'nombre': 'México', 'poblacion': 128932753, 'superficie': 1964375, 'continente': 'América'},
        {'nombre': 'Francia', 'poblacion': 65273511, 'superficie': 551695, 'continente': 'Europa'},
        {'nombre': 'Colombia', 'poblacion': 51049498, 'superficie': 1141748, 'continente': 'América'},
        {'nombre': 'España', 'poblacion': 47450795, 'superficie': 505990, 'continente': 'Europa'}
    ]
    
    encabezados = ['nombre', 'poblacion', 'superficie', 'continente']

    try:
        # Usamos 'w' (write) para crear el archivo y 'newline=""' para evitar saltos de línea
        with open(archivo_csv, mode='w', encoding='utf-8', newline='') as archivo:
            # DictWriter escribe diccionarios en el CSV
            escritor_csv = csv.DictWriter(archivo, fieldnames=encabezados)
            
            # Escribir la fila de encabezado
            escritor_csv.writeheader()
            
            # Escribir todos los países de la lista predeterminada
            escritor_csv.writerows(paises_predeterminados)
        
        print(f"Archivo '{archivo_csv}' creado exitosamente con {len(paises_predeterminados)} países.")
        # Devolver la lista para que el programa la use inmediatamente
        return paises_predeterminados
    except IOError as e:
        print(f"Error Crítico: No se pudo crear el archivo '{archivo_csv}'. ¿Permisos insuficientes?")
        print(f"Detalle del error: {e}")
        return [] # Devolver lista vacía en caso de fallo de escritura
    except Exception as e:
        print(f"Error inesperado al crear el archivo: {e}")
        return []

def cargar_datos(archivo_csv):
    """
    Carga los datos de los países desde un archivo CSV.
    Si el archivo no existe, lo crea con datos predeterminados.
    Valida que 'poblacion' y 'superficie' sean enteros al leer.
    Omite filas con datos inválidos o faltantes.
    """
    
    # --- COMPROBACION DE ARCHIVO ---
    # Comprobar si el archivo existe ANTES de intentar leerlo
    if not os.path.exists(archivo_csv):
        # Si no existe, llamamos a la función para crearlo y
        # devolvemos la lista predeterminada que genera.
        return crear_csv_predeterminado(archivo_csv)
    # --- FIN DE COMPROBACION DE ARCHIVO  ---

    # Si el archivo SÍ existe, continuamos con la lógica de lectura original
    paises = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
            # DictReader usa la primera fila como claves del diccionario
            lector_csv = csv.DictReader(archivo)
            
            num_fila = 1 # Para reportar errores
            for fila in lector_csv:
                num_fila += 1
                try:
                    # Validar y convertir datos numéricos
                    poblacion = int(fila['poblacion'])
                    superficie = int(fila['superficie'])
                    
                    # Validar datos de texto
                    nombre = fila['nombre'].strip()
                    continente = fila['continente'].strip()

                    if not nombre or not continente:
                        print(f"Advertencia: Fila {num_fila} ignorada (nombre o continente vacío).")
                        continue

                    if poblacion < 0 or superficie < 0:
                         print(f"Advertencia: Fila {num_fila} ignorada (datos numéricos negativos).")
                         continue

                    # Si todo es válido, se añade el diccionario a la lista
                    paises.append({
                        'nombre': nombre,
                        'poblacion': poblacion,
                        'superficie': superficie,
                        'continente': continente
                    })

                except (ValueError, TypeError):
                    # Error si 'poblacion' o 'superficie' no son números
                    print(f"Advertencia: Fila {num_fila} ignorada (datos numéricos inválidos: '{fila['poblacion']}', '{fila['superficie']}').")
                except KeyError:
                    # Error si faltan columnas en el CSV
                    print(f"Error: Faltan columnas esperadas en el CSV (ej. 'poblacion'). Abortando carga.")
                    return [] # Devolver lista vacía si la estructura es incorrecta

    except FileNotFoundError:
        # Esta excepción ahora es menos probable, pero se deja por seguridad
        print(f"Error Crítico: Archivo '{archivo_csv}' no encontrado (a pesar de la verificación).")
        print("Por favor, no elimine el archivo mientras el programa se ejecuta.")
        return [] # Devolver lista vacía
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return []

    print(f"\nSe cargaron exitosamente {len(paises)} países desde '{archivo_csv}'.")
    return paises

# --- FUNCIONES DE FILTRADO Y BÚSQUEDA ---

def buscar_por_nombre(paises):
    """
    Busca países por nombre (coincidencia exacta o parcial).
    """
    if not paises:
        print("No hay datos cargados para buscar.")
        return

    # Usamos la nueva función de normalización
    nombre_buscar = normalizar_texto(input("Ingrese el nombre del país a buscar: ").strip())
    if not nombre_buscar:
        print("Búsqueda cancelada.")
        return

    tipo_busqueda = input("¿Buscar coincidencia Exacta (E) o Parcial (P)?: ").strip().lower()

    resultados = []
    if tipo_busqueda == 'e':
        # Comparamos textos normalizados
        resultados = [pais for pais in paises if normalizar_texto(pais['nombre']) == nombre_buscar]
    elif tipo_busqueda == 'p':
        # Comparamos textos normalizados
        resultados = [pais for pais in paises if nombre_buscar in normalizar_texto(pais['nombre'])]
    else:
        print("Tipo de búsqueda no válido. Intente nuevamente.")
        return

    mostrar_paises(resultados)

def filtrar_por_continente(paises):
    """Filtra la lista de países por un continente específico."""
    if not paises:
        print("No hay datos cargados para filtrar.")
        return
        
    # Usamos la nueva función de normalización
    continente_buscar = normalizar_texto(input("Ingrese el nombre del continente: ").strip())
    if not continente_buscar:
        print("Filtro cancelado.")
        return

    resultados = [
        pais for pais in paises 
        # Comparamos textos normalizados
        if normalizar_texto(pais['continente']) == continente_buscar
    ]
    
    mostrar_paises(resultados)

def filtrar_por_rango_poblacion(paises):
    """Filtra países por un rango de población (mínimo y máximo)."""
    if not paises:
        print("No hay datos cargados para filtrar.")
        return
    
    print("Ingrese el rango de población (presione 'c' para cancelar).")
    min_pop = input_entero_positivo("Población mínima (ej: 0): ")
    if min_pop is None: return # Cancelado por el usuario
    
    max_pop = input_entero_positivo("Población máxima (ej: 10000000): ")
    if max_pop is None: return # Cancelado por el usuario
    
    if min_pop > max_pop:
        print("Error: La población mínima no puede ser mayor que la máxima.")
        return

    resultados = [
        pais for pais in paises 
        if min_pop <= pais['poblacion'] <= max_pop
    ]
    
    mostrar_paises(resultados)

def filtrar_por_rango_superficie(paises):
    """Filtra países por un rango de superficie (mínimo y máximo)."""
    if not paises:
        print("No hay datos cargados para filtrar.")
        return

    print("Ingrese el rango de superficie (presione 'c' para cancelar).")
    min_sup = input_entero_positivo("Superficie mínima (ej: 0): ")
    if min_sup is None: return

    max_sup = input_entero_positivo("Superficie máxima (ej: 100000): ")
    if max_sup is None: return
    
    if min_sup > max_sup:
        print("Error: La superficie mínima no puede ser mayor que la máxima.")
        return

    resultados = [
        pais for pais in paises 
        if min_sup <= pais['superficie'] <= max_sup
    ]
    
    mostrar_paises(resultados)

# --- FUNCIÓN DE ORDENAMIENTO ---

def ordenar_paises(paises):
    """
    Ordena la lista de países por un criterio seleccionado (nombre, poblacion, superficie)
    en orden ascendente o descendente. Muestra la lista ordenada.
    """
    if not paises:
        print("No hay datos cargados para ordenar.")
        return

    print("\nSeleccione el criterio de ordenamiento:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    criterio = input("Opción (1-3): ").strip()

    if criterio not in ('1', '2', '3'):
        print("Criterio no válido.")
        return

    orden = input("Seleccione el orden: Ascendente (A) o Descendente (D): ").strip().lower()
    if orden not in ('a', 'd'):
        print("Orden no válido.")
        return

    # Determinar la clave (key) para la función sorted()
    if criterio == '1':
        # Normalizamos el nombre para que ordene sin considerar mayúsculas o acentos
        clave_orden = lambda pais: normalizar_texto(pais['nombre'])
    elif criterio == '2':
        clave_orden = lambda pais: pais['poblacion']
    else: # criterio == '3'
        clave_orden = lambda pais: pais['superficie']

    # Determinar si el orden es reverso
    es_reverso = (orden == 'd')

    # Usar sorted() crea una *nueva* lista ordenada sin modificar la original
    paises_ordenados = sorted(paises, key=clave_orden, reverse=es_reverso)

    mostrar_paises(paises_ordenados)

# --- FUNCIÓN DE ESTADÍSTICAS ---

def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas clave sobre el dataset de países."""
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    # 1. País con mayor y menor población
    # Usamos 'key' para decirle a min/max qué valor comparar
    pais_max_pop = max(paises, key=lambda p: p['poblacion'])
    pais_min_pop = min(paises, key=lambda p: p['poblacion'])

    # 2. Promedio de población y superficie
    total_poblacion = sum(p['poblacion'] for p in paises)
    total_superficie = sum(p['superficie'] for p in paises)
    cantidad_paises = len(paises)
    
    promedio_poblacion = total_poblacion / cantidad_paises
    promedio_superficie = total_superficie / cantidad_paises

    # 3. Cantidad de países por continente
    conteo_continentes = {}
    for pais in paises:
        continente = pais['continente']
        # .get(continente, 0) obtiene el valor actual o 0 si la clave no existe
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    # Mostrar resultados
    print("\n--- Estadísticas Globales ---")
    print("\n[Población]")
    print(f"País con mayor población: {pais_max_pop['nombre']} ({pais_max_pop['poblacion']:,})")
    print(f"País con menor población: {pais_min_pop['nombre']} ({pais_min_pop['poblacion']:,})")
    print(f"Población promedio: {promedio_poblacion:,.2f} habitantes")
    
    print("\n[Superficie]")
    print(f"Superficie promedio: {promedio_superficie:,.2f} km²")
    
    print("\n[Continentes]")
    print("Cantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"- {continente}: {cantidad} país(es)")
    print("-" * 30)

# --- MENÚS Y FLUJO PRINCIPAL ---

def mostrar_menu():
    """Imprime el menú principal de opciones."""
    print("\n--- Sistema de Gestión de Datos de Países ---")
    print("1. Buscar país por nombre")
    print("2. Filtrar países (por continente, población o superficie)")
    print("3. Ordenar países (por nombre, población o superficie)")
    print("4. Mostrar estadísticas")
    print("5. Mostrar todos los países cargados")
    print("0. Salir")

def menu_filtrar(paises):
    """Muestra el sub-menú de opciones de filtrado."""
    while True:
        print("\n--- Sub-menú de Filtros ---")
        print("1. Filtrar por Continente")
        print("2. Filtrar por Rango de Población")
        print("3. Filtrar por Rango de Superficie")
        print("0. Volver al menú principal")
        
        opcion = input("Seleccione una opción de filtro: ").strip()
        
        limpiar_pantalla()
        if opcion == '1':
            filtrar_por_continente(paises)
        elif opcion == '2':
            filtrar_por_rango_poblacion(paises)
        elif opcion == '3':
            filtrar_por_rango_superficie(paises)
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
        if opcion in ('1', '2', '3'):
            input("\nPresione Enter para continuar...")
            limpiar_pantalla()

def main():
    """Función principal que orquesta la aplicación."""
    
    # 1. Cargar los datos al iniciar
    # El nombre del archivo está fijo según los requisitos
    archivo_origen = "paises.csv" 
    lista_paises = cargar_datos(archivo_origen)
    
    if not lista_paises:
        print("\nNo se pudieron cargar los datos iniciales. El programa puede no funcionar correctamente.") 
    
    input("\nPresione Enter para continuar al menú principal...")
    
    # 2. Iniciar bucle del menú
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción (0-5): ").strip()

        limpiar_pantalla() 
        
        if opcion == '1':
            buscar_por_nombre(lista_paises)
        elif opcion == '2':
            menu_filtrar(lista_paises)
            continue 
        elif opcion == '3':
            ordenar_paises(lista_paises)
        elif opcion == '4':
            mostrar_estadisticas(lista_paises)
        elif opcion == '5':
            mostrar_paises(lista_paises)
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
        
        # Pausa para que el usuario pueda leer los resultados
        input("\nPresione Enter para volver al menú...")

# --- Punto de entrada del script ---
if __name__ == "__main__":
    main()