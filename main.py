"""
- registrar alumnos.🧑🏿‍🤝‍🧑🏾
- generar ficha de matricula.🧧
- mostrar las listas de todos las matriculas. 📇
- filtrar matriculaspor programa de estudios.📋
"""

lista_alumnos = []

while True:
    opcion = input("Elije lo que deseas hacer: \n"
                   "escribe (s) si deseas registrar un alumno\n"
                   "escribe (n) si deseas salir del programa\n"
                   "escribe tu respuesta: ")
    if opcion.lower() == "s":
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        alumno = {
            "nombre": nombre,
            "apellido": apellido
        }
        lista_alumnos.append(alumno)
    elif opcion.lower() == "n":
        break

print(lista_alumnos)


# - registrar alumnos
# - generar fiches de matricula
# - mostrar la lista de todos los matriculados
# - filtrar matriculados por programa de estudio
lista_alumnos = []

def mensaje_menu():
    menu_opciones="""" 
    ----------BIENVENIDO AL SISTEMA----------
    ----------REGISTRA  TU  ALUMNO---------
    1.ESCRIBE(s) SI DESEAS AGREGAR UN NUEVO ALUMNO
    2.ESCRIBE(n) SI DESEAS SALIR DEL SISTEMA
    ESCRIBE LA ACCION QUE DESEA REALIZAR :"""
    return menu_opciones

def ingresar_datos_alumno():
    id=len(lista_alumnos)+1
    cui=int(input("ingrese el numero de dni:"))
    nombre=input("ingrese su nombre:")
    apellido=input("ingrese su apellido:")
    numero_celular=int(input("ingrese su celular:"))
    programa_estudio=input("ingrese programa de estudio")
    ciclo_academico=input("ingrese ciclo academico")
    email=input("ingrese su correo electronico")
    guardar_datos_alumnos(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumnos(id,cui,nombre,apellido,numero_celular,pograma_estudio,ciclo_academico,email):
    alumnos={
        "id":id,
        "cui":cui,
        "nombre":nombre,
        "apellido":apellido,
        "numero_celular":numero_celular,
        "programa_estudio":pograma_estudio,
        "ciclo_academico":ciclo_academico,
        "email":email,
    }




while True:
    menu_opciones=input(mensaje_menu())
    if menu_opciones.lower() == "n":
        print("saliendo del sistema")
        break
    elif menu_opciones.lower() == "s":
        print("ingrese sus datos")
    else:
        print("codigo erroneo")
print(lista_alumnos)