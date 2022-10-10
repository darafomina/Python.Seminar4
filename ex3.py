# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randint as rI

uniqueList = {}
finalStr = ''

listStr = "".join(list(map(str, [rI(0,9) for i in range(20)])))
print(f'Задана последовательность цифр {listStr}')

for c in listStr:
    if uniqueList.get(c):
        uniqueList[c] = uniqueList.get(c) + 1
    else:
        uniqueList[c] = 1

for i in uniqueList.items():
    if i[1] == 1:
        finalStr += str(i[0])

print(f'Уникальные цифры {finalStr}') if finalStr else print ('Уникальных позиций нет')
