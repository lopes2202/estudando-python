numero = input("Digite um numero de 0 a 9999: ")

numero = numero.zfill(4)

print("Milhar:", numero[0])
print("Centena:", numero[1])
print("Dezena:", numero[2])
print("Unidade:", numero[3])