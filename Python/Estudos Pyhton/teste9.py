#Manipulação da tupla////tuplas são imutáveis
lanche = ("Hamburgues", "Suco", "Pizza", "Pudim")

print(lanche)
print(lanche[::-1])
print(sorted(lanche))
lanche.sort(reverse=True)


a = (2,5,4)
b = (5,8,1,2)
c = a + b

print(c)
print(len(c))
print(c.count(5))
print(c.index(2))