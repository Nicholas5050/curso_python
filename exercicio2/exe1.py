x= 42
y= 0
print()

try:
    print(x/y)
except ZeroDivisionError as e:
    print('Nao pode dividir por zero')
else:
    print('Alguma coisa esta errada')
finally:
    print('O codigo esta limpo')
print()