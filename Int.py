import numpy as np
print("El maximo y el minimo de una lista de temperatura")
lista = []
Dias_encima_promedio = []
Suma = 0
def IngresoDatos():
    for i in range(0,7):
        Temperatura = float(input("Ingrese las temperaturas de los 7 dias uno por uno: ")) 
        lista.append(Temperatura)

def diasep():
    for C in lista:
        if C > Promedio:
            Dias_encima_promedio.append(C)
            dias =  lista.index(C)
            print("los dias encima del promedio son el dia:", dias+1)
            
def temperaturasextremas():
    for temperatura in lista:
        if temperatura > 40:
            extrema = lista.index(temperatura)
            print("Alerta, en estos dias se detectaron temperaturas extremas:", extrema+1)
        if temperatura < 0:
            extrema = lista.index(temperatura)
            print("Alerta, en estos dias se detectaron temperaturas extremas:", extrema+1)
for t in lista:
    Suma += t
Promedio = Suma / len(lista) 
maxima_temperatura = np.max(lista)
DiaMaxima = lista.index(maxima_temperatura)
minima_temperatura = np.min(lista)
DiaMinima = lista.index(minima_temperatura)

IngresoDatos()
print("La temperatura maxima semanal es:", maxima_temperatura," El dia: ",DiaMaxima+1)
print("La temperatura minima semanal es:", minima_temperatura," El dia: ",DiaMinima)
diasep()
print("Dias encima del promedio son", Dias_encima_promedio)
print(lista)
print("El promedio es:", Promedio)
temperaturasextremas()
