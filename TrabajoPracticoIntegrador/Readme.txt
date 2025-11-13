Gestión de Datos de Países (TPI Programación I)

Este proyecto es una aplicación de consola desarrollada en Python como parte del Trabajo Práctico Integrador de la materia Programación I.

1. Descripción del Programa

gestion_paises.py es un script de Python 3 que permite gestionar una base de datos de países almacenada en un archivo paises.csv. La aplicación ofrece un menú interactivo para realizar las siguientes operaciones:

Carga de Datos Automática: Al iniciar, el script comprueba si existe paises.csv.

Si el archivo no existe, lo crea automáticamente con una lista predeterminada de 9 países.

Si el archivo sí existe, carga los datos contenidos en él.

Gestión de Entradas: El sistema es flexible y robusto:

Ignora mayúsculas y minúsculas en todas las búsquedas de texto.

Ignora acentos (ej: "América" es igual a "america").

Valida que las entradas numéricas (población, superficie) sean enteros positivos.

Funcionalidades del Menú:

Buscar país por nombre: Permite una búsqueda por coincidencia exacta o parcial.

Filtrar países: Ofrece un sub-menú para filtrar por continente, rango de población o rango de superficie.

Ordenar países: Permite ordenar la lista completa por nombre (alfabéticamente), población o superficie (ascendente o descendente).

Mostrar estadísticas: Calcula y muestra el país con mayor/menor población, el promedio de población y superficie, y un conteo de países por continente.

Mostrar todos: Imprime la lista completa de países cargados.

2. Instrucciones de Uso

Prerrequisitos

Tener instalado Python 3.x.

Ejecución

Guarde el archivo gestion_paises.py en una carpeta.

Abra una terminal o consola en esa misma carpeta.

Ejecute el script con el siguiente comando:

python gestion_paises.py


Primera Ejecución: La primera vez que lo ejecute, verá un mensaje indicando que paises.csv no se encontró y que se ha creado uno nuevo con datos predeterminados.

Ejecuciones Siguientes: El programa leerá el paises.csv existente. Usted puede modificar este archivo (añadir/eliminar/editar países) y el programa leerá los nuevos datos al iniciarse.

Una vez en el menú, simplemente ingrese el número de la opción deseada y presione Enter. Siga las instrucciones en pantalla.

3. Ejemplos de Entradas y Salidas

(Basado en los datos predeterminados que genera el script)

Ejemplo 1: Búsqueda Parcial (Ignora mayúsculas)

El usuario quiere buscar todos los países que contengan "ia".

Seleccione una opción (0-5): 1
Limpiando pantalla...
Ingrese el nombre del país a buscar: ia
¿Buscar coincidencia Exacta (E) o Parcial (P)?: p
Limpiando pantalla...

--- Resultados de la Búsqueda ---
Nombre               | Población       | Superficie (km²)   | Continente     
--------------------------------------------------------------------------
Rusia                | 145,934,462     | 17,098,242         | Europa/Asia    
Italia               | 59,110,000      | 301,340            | Europa         
Colombia             | 51,049,498      | 1,141,748          | América        
--------------------------------------------------------------------------
Total de países mostrados: 3

Presione Enter para volver al menú...


Ejemplo 2: Filtrar por Continente (Ignora acentos)

El usuario quiere buscar todos los países de América, pero escribe "america" sin acento.

Seleccione una opción (0-5): 2
Limpiando pantalla...

--- Sub-menú de Filtros ---
1. Filtrar por Continente
2. Filtrar por Rango de Población
3. Filtrar por Rango de Superficie
0. Volver al menú principal
Seleccione una opción de filtro: 1
Limpiando pantalla...
Ingrese el nombre del continente: america

--- Resultados de la Búsqueda ---
Nombre               | Población       | Superficie (km²)   | Continente     
--------------------------------------------------------------------------
Argentina            | 45,376,763      | 2,780,400          | América        
EEUU                 | 331,893,745     | 9,833,520          | América        
México               | 128,932,753     | 1,964,375          | América        
Colombia             | 51,049,498      | 1,141,748          | América        
--------------------------------------------------------------------------
Total de países mostrados: 4

Presione Enter para continuar...


Ejemplo 3: Mostrar Estadísticas

Seleccione una opción (0-5): 4
Limpiando pantalla...

--- Estadísticas Globales ---

[Población]
País con mayor población: EEUU (331,893,745)
País con menor población: Argentina (45,376,763)
Población promedio: 116,360,309.89 habitantes

[Superficie]
Superficie promedio: 3,741,617.56 km²

[Continentes]
Cantidad de países por continente:
- América: 4 país(es)
- Europa/Asia: 1 país(es)
- Asia: 1 país(es)
- Europa: 3 país(es)
------------------------------

Presione Enter para volver al menú...


4. Participación de los Integrantes

[Chirino Pamela: Módulo de carga/creación de CSV, funciones de filtrado, informe teórico.]

[Agüero Lucas: Módulos de búsqueda y ordenamiento, normalización de texto, módulo de estadísticas, README.md.]