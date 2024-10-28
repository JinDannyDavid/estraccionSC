class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return f"{self.nombre}, Salario: {self.salario}"


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
        self.ventas = ventas

    def calcular_bono(self):
        return self.ventas * 0.1


class EmpleadoSoporte(EmpleadoTecnico):
    def __init__(self, nombre, salario, certificaciones, incidencias_resueltas):
        super().__init__(nombre, salario, certificaciones)
        self.incidencias_resueltas = incidencias_resueltas

    def calcular_bono(self):
        return self.incidencias_resueltas * 5
