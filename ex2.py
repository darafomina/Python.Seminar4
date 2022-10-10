# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

numbers = int(input("Введите число: "))

devList = []
dev = 2
while numbers > 2:
    if numbers%dev != 0:
        dev += 1   
    else:
        numbers //= dev
        devList.append(dev)
print(devList)