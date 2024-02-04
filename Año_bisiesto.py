print("Ayuda para años bisiestos.")
def es_bisiesto(anio):
    # Función para determinar si un año es bisiesto
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Solicitar al usuario ingresar un año
anio_usuario = int(input("Ingrese un año: "))

# Verificar si el año es bisiesto utilizando la función
if es_bisiesto(anio_usuario):
    print(f"{anio_usuario} es un año bisiesto.")
else:
    print(f"{anio_usuario} no es un año bisiesto.")
input("Presione Enter para cerrar el programa.") 
