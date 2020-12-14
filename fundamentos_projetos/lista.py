lista = ['Leonardo', 5.5, 'Rodrigues']
lista.append(5)

x = 0
num_elemento = len(lista)

while (x < num_elemento):
    print(lista[x])
    x+=1


lista2 = [1,2,3,4,5,6,7,8,9]
for index in lista2:
    print(lista2)


lista_nums = [1,2,3,4,5,6,7,]
for index, item in enumerate(lista_nums):
    lista_nums[index] +=1000
print(lista_nums)
