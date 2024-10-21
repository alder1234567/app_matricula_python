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
