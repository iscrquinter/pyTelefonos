#Telefonos.py --Agenda telefónica -------------

import os
os.system("cls")

print("AGENDA TELEFÓNICA")
print("=================")

t1=input("Telefono 1:")
t2=input("Telefono 2:")
t3=input("Telefono 3:")
t4=input("Telefono 4:")
t5=input("Telefono 5:")

tels=[t1,t2,t3,t4,t5]

print(tels)

t3 = input("Dame otro telefono 3:")
tels[2]=t3

print(tels)

t6=input("Dame un teléfono 6:")
t7=input("Dame un teléfono 7:")

tels.extend([t6,t7])

print(tels)

tels.insert(1,'6675896529')
print(tels)

tels.pop()
print(tels)

tels.sort()
print(tels)

tels.reverse()
print(tels)

print("Total de numeros telefónicos: {0:4}".format(len(tels)))

print("Gracias")