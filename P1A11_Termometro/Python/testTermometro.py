from Termometro import Termometro

def main():
    # 1. Instancia con constructor por defecto (aleatorio)
    print("--- Termómetro 1 (Aleatorio) ---")
    t1 = Termometro()
    t1.mostrarTemperaturas()
    print("-" * 30)

    # 2. Instancia con constructor parametrizado (usuario)
    print("--- Termómetro 2 (Usuario) ---")
    try:
        temp_usuario = float(input("Ingrese la temperatura en Celsius: "))
        t2 = Termometro(temp_usuario)
        t2.mostrarTemperaturas()
        print("-" * 30)
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
