a = float(input())
b = float(input())

op = input()
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '//':
    print(a // b)
elif op == '%':
    print(a % b)
elif op == '**' or op == '^':
    print(a ** b)
elif op == '=' or op == '==':
    print(a == b)
elif op == '<':
    print(a < b)
elif op == '>':
    print(a > b)
elif op == '<=':
    print(a <= b)
elif op == '>=':
    print(a >= b)
elif op == '!=':
    print(a != b)
else:
    print('Incorrect operation')
