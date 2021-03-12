# Найдите сколько  чисел от 0 до 1000 делятся на 17 (количество и какие числа)

quantity = 0

for i in range(0, 1000):
    if i % 17 == 0:
        quantity += 1
        print(i)
        
print("Количество :", quantity)