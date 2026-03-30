using System;

public class EmpleadoAsalariado : Empleado
{
    private double salarioSemanal;

    public EmpleadoAsalariado(string nombre, string apellido, string nss, double salario)
        : base(nombre, apellido, nss)
    {
        SalarioSemanal = salario;
    }

    public double SalarioSemanal
    {
        get { return salarioSemanal; }
        set { salarioSemanal = (value >= 0.0) ? value : 0.0; }
    }

    public override double Ingresos()
    {
        return SalarioSemanal;
    }

    public override string ToString()
    {
        return $"empleado asalariado: {base.ToString()}\nsalario semanal: {SalarioSemanal:C}";
    }
}
