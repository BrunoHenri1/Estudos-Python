from random import randint

num = (randint (0,10), randint (0,10), randint (0,10), randint (0,10), randint (0,10))

print("Os valores Sorteados foram")
for n in num:
    print(f"{n}", end=' ')
print(f"\nO maior Sorteado foi {max(num)}")
print(f"o Menor sorteado foi {min(num)}")