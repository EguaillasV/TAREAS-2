# Clase Calculadora
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero no permitida"


def menu_calculadora():
    while True:
        print("\n--- Calculadora Básica ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion in ['1', '2', '3', '4']:
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
            calculadora = Calculadora(numero1, numero2)

        if opcion == '1':
            print("Suma:", calculadora.sumar())

        elif opcion == '2':
            print("Resta:", calculadora.restar())

        elif opcion == '3':
            print("Multiplicación:", calculadora.multiplicar())

        elif opcion == '4':
            print("División:", calculadora.dividir())

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")


menu_calculadora()
