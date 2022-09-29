def calculo_salario(horas, tarifa):
    MAX_HORAS_SEMANALES =40
    horas_extra = 0
    if (horas > MAX_HORAS_SEMANALES):
        horas_extra = horas - MAX_HORAS_SEMANALES
        horas = MAX_HORAS_SEMANALES
        calculo = (horas * tarifa) + (horas_extra * (tarifa * 1.5))
    else:
        calculo = (horas * tarifa)
    return calculo

try:
    horas = int(input("Ingrese el número de horas: "))
    tarifa = int(input("Ingrese la tarifa: "))
    pago = calculo_salario(horas,tarifa)
    print (pago)
except:
    print ("Error, ingresar un valor numérico")