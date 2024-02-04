print("Calculadora de vector")
import math

def calcular_modulo_vector(vector):
    # Calcular la suma de los cuadrados de las componentes del vector
    suma_cuadrados = sum(x**2 for x in vector)

    # Calcular la raíz cuadrada de la suma de los cuadrados
    modulo = math.sqrt(suma_cuadrados)

    return modulo

# Solicitar al usuario ingresar las componentes del vector
entrada_usuario = input("Ingrese las componentes del vector separadas por espacios: ")
componentes_vector = [float(x) for x in entrada_usuario.split()]

# Calcular el módulo utilizando la función
modulo_resultante = calcular_modulo_vector(componentes_vector)

# Mostrar el resultado
print(f"El módulo del vector {componentes_vector} es: {modulo_resultante}")
input("Presione Enter para cerrar el programa.") 

