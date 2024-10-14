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