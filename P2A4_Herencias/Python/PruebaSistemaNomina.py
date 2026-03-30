from EmpleadoAsalariado import EmpleadoAsalariado
from EmpleadoPorHoras import EmpleadoPorHoras
from EmpleadoPorComision import EmpleadoPorComision
from EmpleadoBaseMasComision import EmpleadoBaseMasComision
from TrabajadorPiezas import TrabajadorPiezas

def main():
    empleado_asalariado = EmpleadoAsalariado("John", "Smith", "111-11-1111", 800.00)
    empleado_por_horas = EmpleadoPorHoras("Karen", "Price", "222-22-2222", 16.75, 40)
    empleado_por_comision = EmpleadoPorComision("Sue", "Jones", "333-33-3333", 10000, 0.06)
    empleado_base_mas_comision = EmpleadoBaseMasComision("Bob", "Lewis", "444-44-4444", 5000, 0.04, 300)
    trabajador_piezas = TrabajadorPiezas("Jane", "Doe", "555-55-5555", 2.50, 200)

    print("Empleados procesados por separado:\n")
    print(f"{empleado_asalariado}\ningresos: ${empleado_asalariado.ingresos():,.2f}\n")
    print(f"{empleado_por_horas}\ningresos: ${empleado_por_horas.ingresos():,.2f}\n")
    print(f"{empleado_por_comision}\ningresos: ${empleado_por_comision.ingresos():,.2f}\n")
    print(f"{empleado_base_mas_comision}\ningresos: ${empleado_base_mas_comision.ingresos():,.2f}\n")
    print(f"{trabajador_piezas}\ningresos: ${trabajador_piezas.ingresos():,.2f}\n")

    empleados = [
        empleado_asalariado,
        empleado_por_horas,
        empleado_por_comision,
        empleado_base_mas_comision,
        trabajador_piezas
    ]

    print("Empleados procesados en forma polimorfica:\n")
    for empleado_actual in empleados:
        print(empleado_actual)
        if isinstance(empleado_actual, EmpleadoBaseMasComision):
            empleado_actual.salario_base *= 1.10
            print(f"nuevo salario base con 10% de aumento es: ${empleado_actual.salario_base:,.2f}")
        print(f"ingresos ${empleado_actual.ingresos():,.2f}\n")

    for i, empleado_actual in enumerate(empleados):
        print(f"El empleado {i} es un {empleado_actual.__class__.__name__}")

if __name__ == "__main__":
    main()
