n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2
print('A soma vale é {},  o produto é {},  a divisão é {:.2f}' .format(n1 + n2, m, d), end=">>>")
print('Divisão inteira {} e potencia {}'.format(di,exp))