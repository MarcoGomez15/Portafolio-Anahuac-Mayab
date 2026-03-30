using System;

public class EmpleadoPorComision : Empleado
{
    private double ventasBrutas;
    private double tarifaComision;

    public EmpleadoPorComision(string nombre, string apellido, string nss, double ventas, double tarifa)
        : base(nombre, apellido, nss)
    {
        VentasBrutas = ventas;
        TarifaComision = tarifa;
    }

    public double VentasBrutas
    {
        get { return ventasBrutas; }
        set { ventasBrutas = (value >= 0.0) ? value : 0.0; }
    }

    public double TarifaComision
    {
        get { return tarifaComision; }
        set { tarifaComision = (value > 0.0 && value < 1.0) ? value : 0.0; }
    }

    public override double Ingresos()
    {
        return VentasBrutas * TarifaComision;
    }

    public override string ToString()
    {
        return $"empleado por comision: {base.ToString()}\nventas brutas: {VentasBrutas:C}; tarifa de comision: {TarifaComision:F2}";
    }
}
