class CalculadorBonos:
    def calcular(self):
        raise NotImplementedError("")


class CalculadorBonosVentas(CalculadorBonos):
    def __init__(self, ventas):
        self.ventas = ventas

    def calcular(self):
        return self.ventas * 0.1


class CalculadorBonosSoporte(CalculadorBonos):
    def __init__(self, incidencias_resueltas):
        self.incidencias_resueltas = incidencias_resueltas

    def calcular(self):
        return self.incidencias_resueltas * 5
