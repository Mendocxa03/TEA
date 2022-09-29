def calcula_calificacion(nota):
   
    if (nota >= 0.9 and nota <= 1.0):
        calif = "Sobresaliente"
    elif (nota>= 0.8 and nota < 0.9):
        calif = "Notable"
    elif (nota >= 0.7 and nota <= 0.8):
        calif = "Bien"
    elif (nota >= 0.6 and nota <= 0.7):
        calif = "Suficiente"
    elif (nota >=0 and nota < 0.6):
        calif = "Insuficiente"
    else:
        calif =  "Nota no válida"
    return calif

try:
    nota = float(input("Introduzca puntuación (0.01 - 1.00): "))
    calif = calcula_calificacion(nota)
    print ("El grado de su calificación es:", calif)
except:
    print ("Error, debe ingresar un valor numérico")


