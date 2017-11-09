salida = 0

for x in range(1000) :
    if x % 3 == 0 :
        print(x)
        salida = salida + x
    elif x % 5 == 0 :
        print(x)
        salida = salida + x
print("Suma Total: " + str(salida))
