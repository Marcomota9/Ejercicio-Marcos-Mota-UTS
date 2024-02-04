print("CALCULADORA DE CIRCUNFERENCIAS BIENVENIDO.") 
import math

def calcular_area_perimetro_circunferencia(radio):
    # Calcular área y perímetro de la circunferencia
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def main():
    # Solicitar al usuario el radio de la circunferencia
    radio = float(input("Introduce el radio de la circunferencia: "))

    # Calcular área y perímetro utilizando la función
    area, perimetro = calcular_area_perimetro_circunferencia(radio)

    # Mostrar resultados
    print(f"Área de la circunferencia: {area:.2f}")
    print(f"Perímetro de la circunferencia: {perimetro:.2f}")

if __name__ == "__main__":
    main()
input("Presione Enter para cerrar el programa.")