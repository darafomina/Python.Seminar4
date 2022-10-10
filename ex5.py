# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

def readEquation(path):
    file = open (path, "r")
    firstEquation =  file.read()
    file.close()
    eqation = {}


    firstEquation = firstEquation.replace(" + ", " +").replace(" - ", " -").split()[:-2]
    for i in range(len(firstEquation)):
        firstEquation[i] = firstEquation[i].replace("+", "").split("x^")
        if firstEquation[i][0] == "":
           firstEquation[i][0] = '1' 
        if len(firstEquation[i]) < 2:
            firstEquation[i].append('0')
          
        eqation[int(firstEquation[i][1])] = int(firstEquation[i][0])

    return eqation

finalWord = {}

word1 = readEquation(r"numbers1.txt")
word2 = readEquation(r"numbers2.txt")


for i in range(max(len(word1), len(word2)) + 1, -1, -1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0)

finalString = ""
First = True
for item in finalWord:
    symbol = "+ "
    last = "x^"
    degree = item

    if finalWord[item] < 0:
        symbol = "- "
    if First and finalWord[item] >= 0:
        symbol = ""
    if First and finalWord[item] < 0:
        symbol = "-"
    finalWord[item] = abs(finalWord[item])
    if finalWord[item] == 1:
        finalWord[item] = ""
    
    if item == 1:
        last = "x"
        degree = ""
    if item < 1:
        last = ""
        degree = ""
    finalString += symbol+str(finalWord[item])+last+str(degree)+" "
    First = False

finalString += "= 0"
data = open (r"numbers3.txt", "w")
data.write(finalString)
data.close()  
print (finalString)