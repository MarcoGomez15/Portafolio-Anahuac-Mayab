

public class Mamifero 
{
    private string nombre;
    protected double peso;

    public Mamifero(string n, double p)
    {
        this.nombre = n;
        this.peso = p;
    }

    public string Nombre
    {
        get { return nombre; }
        set { nombre = value; }
    }
    
    public override string ToString()
    {
        return $"Mamifero\n [{nombre},{peso} kg]";
    }
}
