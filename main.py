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


lista_alumnos=()
def mensaje_menu();
menu_opciones=unput("""
---Bienvenido al Sistema-------

-----Regitra tu alumno-----

1. Escribe (s) si deseas agregar un nuevo alumno

2. Escribe (n) si deseas salir del sistema Escribe la Accion que desea realiza: """)
return(menu_opciones)

def ingresar_datos_alumno():
id-len(lista_alumnos)+1
cui-int(input("Ingrese el numero de su dni: "))
nombre input("Ingrese el nombre del alumno: ")
apellido-input("Ingrese el apeliido del alumno: ")
numero_celular-int(input("Ingrese su numero de celular: "))
programa_estudio=input("Ingrese el programa de estudio: ")
ciclo_academico input("Ingrese su ciclo academico: ")
email-input("Ingrese su correo electronico: ")

  