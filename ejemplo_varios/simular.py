# hacer un simulación de lanzar un moneda  contar cuantas veces sale cara usa Simpy
# para simular el tiempo entre lanzamientos

import simpy
import random

cara = 0
sello = 0

def lanzar_moneda(env):
    global cara, sello
    while True:
        yield env.timeout(random.expovariate(1.0/0.5))
     
        #lanzar moneda
        if random.randint(0,1) == 0:
            cara += 1
            print("cara")
        else:
            sello += 1
            print("sello")
        
        


env = simpy.Environment()
env.process(lanzar_moneda(env))
env.run(until=10)

#estadisticas
print("="*30)
print("cara: ", cara)
print("sello: ", sello)
print("total: ", cara + sello)
print("porcentaje de cara: ", (cara/(cara+sello))*100)
print("porcentaje de sello: ", (sello/(cara+sello))*100)
print("="*30)

