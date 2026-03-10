

public class Ballena : Mamifero 
{
    public Ballena(string n, double p) : base(n, p)
    {
    }

    public override string ToString()
    {
        return base.ToString() + "[Ballena]";
    }
}
