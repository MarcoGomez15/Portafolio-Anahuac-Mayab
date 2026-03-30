using System;

public class TrabajadorPiezas : Empleado
{
    private double salario;
    private int piezas;

    public TrabajadorPiezas(string nombre, string apellido, string nss, double salario, int piezas)
        : base(nombre, apellido, nss)
    {
        Salario = salario;
        Piezas = piezas;
    }

    public double Salario
    {
        get { return salario; }
        set { salario = (value >= 0.0) ? value : 0.0; }
    }

    public int Piezas
    {
        get { return piezas; }
        set { piezas = (value >= 0) ? value : 0; }
    }

    public override double Ingresos()
    {
        return Salario * Piezas;
    }

    public override string ToString()
    {
        return $"trabajador por piezas: {base.ToString()}\nsalario por pieza: {Salario:C}; piezas producidas: {Piezas}";
    }
}
