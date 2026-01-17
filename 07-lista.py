lista1 =["dario",33,9,5,"True","German",20,8]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print (lista1[0:3])
print (lista1[3:])

lista1.append("vargas")
print (lista1)

lista1.insert(2,"Nadia")
print(lista1)

lista1.extend(["Uno", 1.1, False])
print(lista1)

lista1.remove(33)
print(lista1)

lista1.pop()
print(lista1)

lista2=["tres","cuatro"]
lista3=lista1+lista2
print(lista3)


