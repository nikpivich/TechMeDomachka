from math import *

sample = input('Введите пример:').replace(' ', '')

def operation(a, b, op):
    try:
        if op == '+':
            return int(a) + int(b)
        elif op == '-':
            return int(a) - int(b)
        elif op == '*':
            return int(a) * int(b)
        elif op == '/':
            return int(a) / int(b)
        elif op == '^':
            return pow(int(a), int(b))
        elif op == '!':
            return factorial(int(a))
    except ValueError:
        print('Операция не осуществляется')



for i in '+-/^*!':
    if i in sample:
        z= sample.index(i)

try:
    a = sample[:z]
    b = sample[(z + 1):]
    print(operation(a, b, sample[z]))
except NameError:
    print('Операция не осуществляется')
