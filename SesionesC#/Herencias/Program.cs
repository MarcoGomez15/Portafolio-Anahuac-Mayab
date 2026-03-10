using System;

class testMamifero{
    public static void Main()
    {
        Gato Michi = new Gato("Michi", 5, 12);
        Vaca Lola = new Vaca("Lola", 500, 20);
        Ballena Willy = new Ballena("Willy", 5000);   

        Console.WriteLine(Michi);
        Console.WriteLine("");
        Console.WriteLine(Lola);
        Lola.CalcularCantidadComida();
        Console.WriteLine("");
        Console.WriteLine(Willy);
    }
}


