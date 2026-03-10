from Persona import PacienteExterno, PacienteHospitalizado, Medico

def main():
    while True:
        print("\n--- MENÚ DEL SISTEMA DE HOSPITAL ---")
        print("1. Registrar un paciente externo")
        print("2. Registrar un paciente hospitalizado")
        print("3. Registrar un médico")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        print("")
        
        if opcion == "1":
            print("--- Registro de Paciente Externo ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            genero = input("Género: ")
            try:
                edad = int(input("Edad: "))
                altura = float(input("Altura (m): "))
                peso = float(input("Peso (kg): "))
                noConsultorio = int(input("No. de Consultorio: "))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos (edad, altura, peso, consultorio).")
                continue
            horario = input("Horario: ")
            fecha = input("Fecha (ej. DD/MM/AAAA): ")
            
            paciente = PacienteExterno(nombre, apellido, genero, edad, altura, peso, noConsultorio, horario, fecha)
            print("\n--- Datos del Paciente Registrado ---")
            paciente.printPacienteExterno()
            print(f"IMC: {paciente.imc():.2f}")
            paciente.examenFisico()
            
        elif opcion == "2":
            print("--- Registro de Paciente Hospitalizado ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            genero = input("Género: ")
            try:
                edad = int(input("Edad: "))
                altura = float(input("Altura (m): "))
                peso = float(input("Peso (kg): "))
                habitacion = int(input("Habitación: "))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos (edad, altura, peso, habitación).")
                continue
            tipoCirugia = input("Tipo de Cirugía: ")
            
            paciente = PacienteHospitalizado(nombre, apellido, genero, edad, altura, peso, habitacion, tipoCirugia)
            print("\n--- Datos del Paciente Registrado ---")
            paciente.printPacienteHospitalizado()
            print(f"IMC: {paciente.imc():.2f}")
            paciente.indicaciones()
            
        elif opcion == "3":
            print("--- Registro de Médico ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            genero = input("Género: ")
            especialidad = input("Especialidad: ")
            try:
                edad = int(input("Edad: "))
                cedula = int(input("Cédula Profesional: "))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para edad y cédula.")
                continue
            
            medico = Medico(nombre, apellido, genero, edad, especialidad, cedula)
            print("\n--- Datos del Médico Registrado ---")
            medico.printMedico()
            
        elif opcion == "4":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
