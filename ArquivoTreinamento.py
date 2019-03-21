from random import randint
import string

arrayTimes = ['Grêmio','Flamengo','Botafogo','São Paulo','Vasco']
arrayEstadios = ['Arena do Grêmio', 'Maracanã', 'Engenhão', 'Morumbi', 'São Januário']

timeMandante  = randint(0,4)
timeVisitante = randint(0,4)
golsMandante  = str(randint(0,3))
golsVisitante = str(randint(0,3))

while timeMandante == timeVisitante:
    timeVisitante = randint(0,4)

print ("Estádio: " + arrayEstadios[timeMandante])
print (arrayTimes[timeMandante] + " " + golsMandante + " x " + golsVisitante + " " + arrayTimes[timeVisitante])
