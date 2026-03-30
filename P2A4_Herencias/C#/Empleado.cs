using System;

public abstract class Empleado
{
    public string PrimerNombre { get; private set; }
    public string ApellidoPaterno { get; private set; }
    public string NumeroSeguroSocial { get; private set; }

    public Empleado(string nombre, string apellido, string nss)
    {
        PrimerNombre = nombre;
        ApellidoPaterno = apellido;
        NumeroSeguroSocial = nss;
    }

    public abstract double Ingresos();

    public override string ToString()
    {
        return $"{PrimerNombre} {ApellidoPaterno}\nnumero de seguro social: {NumeroSeguroSocial}";
    }
}
