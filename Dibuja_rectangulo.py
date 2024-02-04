print("Dibuja rectangulo")
def dibujar_rectangulo(anchura, altura, caracter):
    for i in range(altura):
        print(caracter * anchura)

def main():
    # Solicitar al usuario la anchura, altura y caracter
    anchura = int(input("Introduce la anchura del rectángulo: "))
    altura = int(input("Introduce la altura del rectángulo: "))
    caracter = input("Introduce el carácter para el dibujo: ")

    # Llamar a la función para dibujar el rectángulo
    dibujar_rectangulo(anchura, altura, caracter)

if __name__ == "__main__":
    main()
    input("Presione Enter para cerrar el programa.") 
