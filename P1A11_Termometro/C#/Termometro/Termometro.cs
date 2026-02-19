using System;

namespace Termometro
{
    public class Termometro
    {
        private double temperatura;

        // Constructor por defecto: temperatura aleatoria entre 0 y 100
        public Termometro()
        {
            Random random = new Random();
            temperatura = random.NextDouble() * 100;
        }

        // Constructor parametrizado: recibe temperatura en Celsius
        public Termometro(double temp)
        {
            temperatura = temp;
        }

        public double TemperaturaC()
        {
            return temperatura;
        }

        public double TemperaturaF()
        {
            return (temperatura * 9 / 5) + 32;
        }

        public double TemperaturaK()
        {
            return temperatura + 273.15;
        }

        public void MostrarTemperaturas()
        {
            Console.WriteLine($"Temperatura en Celsius:    {TemperaturaC():F2} °C");
            Console.WriteLine($"Temperatura en Fahrenheit: {TemperaturaF():F2} °F");
            Console.WriteLine($"Temperatura en Kelvin:     {TemperaturaK():F2} K");
        }
    }
}
