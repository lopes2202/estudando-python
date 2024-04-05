num1 = int(input("informe um número: "))
num2 = int(input("Informe outro numero: "))
num3 = int(input("Informe outro numero: "))
menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print("O menor valor é {}".format(menor))
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print("O maior valor é {}".format(maior))







