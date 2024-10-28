from empleados import EmpleadoVentas, EmpleadoSoporte

empleado_ventas = EmpleadoVentas("Luis", 50000, 90, 20000)
print(empleado_ventas.mostrar_informacion())
print(empleado_ventas.verificar_metas())
print("Bono:", empleado_ventas.calcular_bono())

empleado_soporte = EmpleadoSoporte("Ana", 45000, ["Redes", "Linux"], 120)
print(empleado_soporte.mostrar_informacion())
print(empleado_soporte.listar_certificaciones())
print("Bono:", empleado_soporte.calcular_bono())
