h = int(input("Ingrese el valor de las horas: "))
m = int(input("Ingrese el valor de las minutos: "))
s = int(input("Ingrese el valor de las segundos: "))

lapso = int(input("Ingrese el valor del lapso en segundos"))

# Indicar la nueva hora

en_segundos = h *3600 + m*60 + s + lapso

h = en_segundos //3600
en_segundos %= 3600
m = en_segundos //60
en_segundos %=60

s = en_segundos

print("la nueva hora es: ")

print(h,m,s)

              
