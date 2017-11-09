import numpy as np

prize = np.array([200,100,50,20,10,5,2,1])
combinacion = 0
all_coins = []

for c0 in range(int(200/prize[0]) + 1) :
    for c1 in range(int(200/prize[1]) +1) :
        for c2 in range(int(200/prize[2]) +1) :
            for c3 in range(int(200/prize[3]) +1) :
                for c4 in range(int(200/prize[4]) +1) :
                    for c5 in range(int(200/prize[5]) +1) :
                        for c6 in range(int(200/prize[6]) +1) :
                            for c7 in range(int(200/prize[7]) +1) :
                                if np.sum(np.array([c0,c1,c2,c3,c4,c5,c6,c7])*prize) == 200 :
                                    combinacion = combinacion + 1
                                    if combinacion % 30 == 0 : # Nos vale para saber el progreso del proceso
                                        print("Calculando ... Llevamos " + str(combinacion) + " y seguimos con el cálculo.")
                                    #all_coins.append(coins)
                                    break
print("El numero de combinaciones de monedas es : " + str(combinacion))
#print("Combinaciones")
#print(all_coins)
