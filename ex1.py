# 1.Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

num = (input("Введите d от 0.1 до 0.0000000001: "))

pi = 3.1415926535
count = 0

def get_precision(num):
    str_f = str(num)
    if '.' not in str_f:
        return 0
    return len(str_f[str_f.index('.') + 1:])  # Получение строки после точки и возвращение ее длины
count = int(get_precision(num))
print(count)

res = float(int(pi * (10**count)))/(10**count)

print(res)