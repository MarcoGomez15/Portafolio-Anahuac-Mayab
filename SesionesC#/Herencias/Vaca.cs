

public class Vaca : Mamifero 
{
    private double litrosLeche;

    public Vaca(string n, double p, double l) : base(n, p)
    {
        this.litrosLeche = l;
    }

    public void CalcularCantidadComida()
    {
        Console.WriteLine($"{peso * 0.03}kg de alimento");
    }

    public override string ToString()
    {
        return base.ToString() + $"[litros de leche: {litrosLeche}]";
    }
}
