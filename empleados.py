from bonos import CalculadorBonosVentas, CalculadorBonosSoporte
from Empleado import Empleado

class EmpleadoConMetas(Empleado):
    def __init__(self, nombre, salario, metas):
        super().__init__(nombre, salario)
        self.metas = metas

    def verificar_metas(self):
        return f"{self.nombre} ha cumplido {self.metas}% de sus metas."


class EmpleadoTecnico(Empleado):
    def __init__(self, nombre, salario, certificaciones):
        super().__init__(nombre, salario)
        self.certificaciones = certificaciones

    def listar_certificaciones(self):
        return f"{self.nombre} tiene certificaciones en: {', '.join(self.certificaciones)}."


class EmpleadoVentas(EmpleadoConMetas):
    def __init__(self, nombre, salario, metas, ventas):
        super().__init__(nombre, salario, metas)
        self.calculador_bono = CalculadorBonosVentas(ventas)

    def calcular_bono(self):
        return self.calculador_bono.calcular()


class EmpleadoSoporte(EmpleadoTecnico):
    def __init__(self, nombre, salario, certificaciones, incidencias_resueltas):
        super().__init__(nombre, salario, certificaciones)
        self.calculador_bono = CalculadorBonosSoporte(incidencias_resueltas)

    def calcular_bono(self):
        return self.calculador_bono.calcular()
