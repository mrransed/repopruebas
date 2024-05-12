lista = [1,2,3,4]
lista2 = [3,"z","d",4]


print(lista[0:])
print(lista[:3])


#agregaar listas 

lista.append("sad")
lista.insert(1,"sad")
lista.extend(lista2)
lista.remove(4)
lista.remove(4)
del lista[1]

print(lista)
lista.clear()
print(lista)
print(len(lista))