import numpy as np

monedas = {"2£":200, "1£":100, "50p":50, "20p":20, "10p":10, "5p":5, "2p":2, "1p":1}
np_monedas = np.array(monedas)

print(monedas)

prize = np.array([200,100,50,20,10,5,2,1])
combinacion = 0
all_coins = []
for c0 in range(2) :
    for c1 in range(3) :
        for c2 in range(5) :
            for c3 in range(11) :
                for c4 in range(21) :
                    for c5 in range(41) :
                        for c6 in range(101) :
                            for c7 in range(201) :
                                coins = [c0,c1,c2,c3,c4,c5,c6,c7]
                                if np.sum(coins*prize) == 200 :
                                    combinacion = combinacion + 1
                                    all_coins = np.append(all_coins,coins)
print("El numero de combinaciones de monedas es : " + str(combinacion))
