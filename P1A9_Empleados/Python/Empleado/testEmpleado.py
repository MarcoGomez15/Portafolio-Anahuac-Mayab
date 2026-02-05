from Empleado import Empleado

def main():
    # Objeto 1 - constructor vacio (usando valores por defecto)
    print("--- Empleado 1 (Vacio) ---")
    emp1 = Empleado()
    print(emp1)

    # Objeto 2 - constructor con parametros
    print("--- Empleado 2 (Parametros) ---")
    emp2 = Empleado("Donald Trump", 2025, 400000.99)
    print(emp2)

    # Parte 2 - Solicitar datos al usuario
    print("\n--- Empleado 3 (Usuario) ---")
    
    try:
        nom = input("Ingresa el nombre del empleado:\n")
        
        anio_str = input("Ingrese el año de contratacion:\n")
        anio = int(anio_str)
        
        sal_str = input("Ingrese el salario: \n")
        sal = float(sal_str)
        
        emp3 = Empleado(nom, anio, sal)
        print(emp3)
        
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para año y salario.")

if __name__ == "__main__":
    main()
