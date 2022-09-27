import time

ti = 10
tf = -1

print ('Iniciando contagem regressiva para a detonação...')
print("")
for d in range (ti, tf, -1):
    print(d)

    time.sleep(1)

print("BUM!!!")