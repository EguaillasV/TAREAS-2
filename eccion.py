
#Calcular Area

import math


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2



class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto



class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2



class Circunferencia:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


# Menú de opciones
def menu_areas():
    while True:
        print("\n--- Calculadora de Áreas ---")
        print("1. Área del Cuadrado")
        print("2. Área del Rectángulo")
        print("3. Área del Triángulo")
        print("4. Área de la Circunferencia")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            lado = float(input("Ingresa el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print("Área del Cuadrado:", cuadrado.area())

        elif opcion == '2':
            ancho = float(input("Ingresa el ancho del rectángulo: "))
            alto = float(input("Ingresa el alto del rectángulo: "))
            rectangulo = Rectangulo(ancho, alto)
            print("Área del Rectángulo:", rectangulo.area())

        elif opcion == '3':
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            triangulo = Triangulo(base, altura)
            print("Área del Triángulo:", triangulo.area())

        elif opcion == '4':
            radio = float(input("Ingresa el radio de la circunferencia: "))
            circunferencia = Circunferencia(radio)
            print("Área de la Circunferencia:", circunferencia.area())

        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")


menu_areas()






