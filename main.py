from empleados import EmpleadoVentas, EmpleadoSoporte

empleado_ventas = EmpleadoVentas("Danny", 50000, 70, 77777)
print(empleado_ventas.mostrar_informacion())
print(empleado_ventas.verificar_metas())
print("Bono:", empleado_ventas.calcular_bono())

empleado_soporte = EmpleadoSoporte("David", 45000, ["Python", "C++"], 120)
print(empleado_soporte.mostrar_informacion())
print(empleado_soporte.listar_certificaciones())
print("Bono:", empleado_soporte.calcular_bono())

