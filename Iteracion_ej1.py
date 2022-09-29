contador = 0
sumatoria = 0

while True:
    numero=input('Ingrese un número: ')
    try: 
        if (numero == 'done'):
            break
        else:
            contador= contador + 1
            sumatoria= sumatoria + int(numero)
            promedio = sumatoria/contador
    except:
        print("Error, debe ingresar un número")
        continue
print ("Contador:", contador)
print ("Sumatoria:", sumatoria)
print("Promedio", promedio)

