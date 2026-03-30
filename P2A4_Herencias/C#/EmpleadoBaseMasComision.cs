using System;

public class EmpleadoBaseMasComision : EmpleadoPorComision
{
    private double salarioBase;

    public EmpleadoBaseMasComision(string nombre, string apellido, string nss, double ventas, double tarifa, double salario)
        : base(nombre, apellido, nss, ventas, tarifa)
    {
        SalarioBase = salario;
    }

    public double SalarioBase
    {
        get { return salarioBase; }
        set { salarioBase = (value >= 0.0) ? value : 0.0; }
    }

    public override double Ingresos()
    {
        return SalarioBase + base.Ingresos();
    }

    public override string ToString()
    {
        return $"con salario base {base.ToString()}; salario base: {SalarioBase:C}";
    }
}
