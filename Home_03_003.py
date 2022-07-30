# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01]
def NewList (list1):
    DelPoint = []
    for i in range(len(list1)):
        b = list1[i] * 10
        c = b % 10
        d = c / 10
        DelPoint.append (round(d, 10))
    return DelPoint

def MaxMinNum(DelPoint):
    MaxNum = 0
    MinNum = 1
    for i in range(1,(len(DelPoint))):
        if DelPoint[i]>MaxNum:
            MaxNum=DelPoint[i]
        if DelPoint[i]>MinNum or DelPoint[i] !=0.00:
            MinNum=DelPoint[i]
    print ('Max = ',MaxNum)
    print ('Min = ',MinNum)
    print (MaxNum-MinNum)

print(NewList (list1))
MaxMinNum(NewList(list1)) 
