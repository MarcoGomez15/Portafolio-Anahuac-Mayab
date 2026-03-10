

public class Gato : Mamifero 
{
    private int nBigotes;

    public Gato(string n, double p, int b) : base(n, p)
    {
        this.nBigotes = b;
    }

    public override string ToString()
    {
        return base.ToString() + $"[Bigotes: {nBigotes}]";
    }
}
