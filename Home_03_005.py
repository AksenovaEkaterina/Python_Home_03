# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def Fibonacci(n):
#     if n<= 0:
#         print("Incorrect input")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)

 
# print(Fibonacci(10))

# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a(-1*n)=(-1)**(n+1)

# data = list(fibonacci(10))
# print(data)

# fib1 = 1
# fib2 = 1 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
# i = 0
# fibonacci1 = []
# while i < n - 3:
#     fib_sum = fib2 - fib1
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#     fibonacci1.append(fib2)
    
 
 
# print(fibonacci1,',' "Значение этого элемента:", fib2)

n= int(input("-->"))
def fib(n):
    if n in range(2):
        return 1
    else:
        return n*fib(n-1)
print({fib(n)})