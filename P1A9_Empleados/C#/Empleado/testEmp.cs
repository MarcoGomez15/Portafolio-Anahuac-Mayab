using System;

class testEmpleado
{
    static void Main()
    {
        // Objeto 1 - constructor vacio
        Console.WriteLine("--- Empleado 1 (Vacio) ---");
        Empleado emp1 = new Empleado();
        Console.WriteLine(emp1.ToString());

        // Objeto 2 - constructor con parametros
        Console.WriteLine("--- Empleado 2 (Parametros) ---");
        Empleado emp2 = new Empleado("Donald Trump", 2025, 400000.99);
        Console.WriteLine(emp2.ToString());

        // Parte 2 - Solicitar datos al usuario
        Console.WriteLine("\n--- Empleado 3 (Usuario) ---");
        
        Console.WriteLine("Ingresa el nombre del empleado:");
        string nom = Console.ReadLine();

        Console.WriteLine("Ingrese el año de contratacion:");
        int anio = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("Ingrese el salario: ");
        double sal = Convert.ToDouble(Console.ReadLine());

        Empleado emp3 = new Empleado(nom, anio, sal);
        Console.WriteLine(emp3.ToString());
    }
}
