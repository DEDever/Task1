import random
r=1
yes=0
N=int(input("Введіть кількість точок: "))
for i in range(N):
    x=random.random()           # Генерация случайных чисел
    y=random.random()
    if x*x+y*y <= r:
        yes+=1
result = yes/N*4
print(result)
