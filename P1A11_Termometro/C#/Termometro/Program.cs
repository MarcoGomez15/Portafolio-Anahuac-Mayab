using System;

namespace Termometro
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1. Crear instancia con constructor por defecto (aleatorio)
            Console.WriteLine("--- Termómetro con valor aleatorio ---");
            Termometro t1 = new Termometro();
            t1.MostrarTemperaturas();

            Console.WriteLine();

            // 2. Pedir temperatura al usuario
            Console.Write("Introduce una temperatura en Celsius: ");
            if (double.TryParse(Console.ReadLine(), out double tempUsuario))
            {
                // 3. Crear instancia con constructor parametrizado
                Console.WriteLine("\n--- Termómetro con valor del usuario ---");
                Termometro t2 = new Termometro(tempUsuario);
                t2.MostrarTemperaturas();
            }
            else
            {
                Console.WriteLine("Entrada no válida. Se esperaba un número.");
            }
        }
    }
}
