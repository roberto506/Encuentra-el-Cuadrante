import numpy as np
import matplotlib.pyplot as plt
from random import randint

levels = int(input("Ingrese cuantos niveles deseas?(min 1/ 20 por defecto) ") or 20)
position = []
if levels >= 1:
    lanes = [0]*(levels)
else:
    print("El valor de los niveles no puede ser menor a 1.")
    exit()

for h in range((levels)**2*100):
    stored = -1
    for j in range(levels):
        stored += randint(0, 1)
    lanes[stored] += 1
print((levels)**2*3000, "pelotas usadas en total")
print(lanes)

if len(lanes)%2==0:
    X = np.arange(-((len(lanes)/2)-1), (len(lanes)/2)+1)
else:
    X = np.arange(-((len(lanes)/2)-.5), (len(lanes)/2)+.5)
plt.suptitle('Maquina de Galton')
plt.hist(position, bins=2,cumulative=True)
plt.bar(X + 0.00, lanes, width=0.25)
plt.show()
