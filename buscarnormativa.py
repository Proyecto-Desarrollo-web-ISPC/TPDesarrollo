import mysql.connector
from conexion import DatabaseConnection         
                        
def buscar_normativa_por_numero(numero_normativa):
    # Establecer la conexión con la base de datos
    # Crear una instancia de DatabaseConnection
    connection = DatabaseConnection(
        host="localhost",
        user="root",
        password="s1nc0d1f1c4r",
        port="3306",
        database="poderjudicial"
    )

    # Establecer la conexión con la base de datos
    connection.connect()

    # Obtener el cursor de la conexión
    cursor = connection.connection.cursor()

    # Crear la consulta SQL con el número de normativa
    consulta = "SELECT * FROM normativas WHERE nro_normativa = %s"

    try:
        # Ejecutar la consulta con el número de normativa
        cursor.execute(consulta, (numero_normativa,))
        resultado = cursor.fetchall()

        if resultado:
            for row in resultado:
                print(f"ID: {row[0]}, Tipo: {row[1]}, Número: {row[2]}, Fecha: {row[3]}, Descripción: {row[4]},Jurisdiccion: {row[5]}, Palabra Clave: {row[6]}, ID_categoria: {row[7]}, ID_organo legislativo: {row[8]}")  # Ajusta los índices según tu estructura de tabla
        else:
            print("No se encontraron resultados para el número de normativa ingresado")
    except mysql.connector.Error as error:
        print(f"Error al buscar la normativa: {error}")
    finally:
        cursor.close()
        connection.close()

#Ejemplo de uso
numero_normativa_buscar = int(input("Ingrese el número de normativa a buscar: "))

buscar_normativa_por_numero( numero_normativa_buscar)                        
