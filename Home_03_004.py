# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def BinaryNumber (Num1):
    BinaryNum = ''
    while Num1//2 >0:
        Num2 = Num1//2
        Num3 = Num1-(Num2*2)
        Num1 = Num2
        a=str(Num3)
        BinaryNum+=a
    b=str(Num2)
    BinaryNum+=b
    def reverse_string1(BinaryNum):
        return BinaryNum[::-1]
    print(reverse_string1(BinaryNum))
  
BinaryNumber (2)