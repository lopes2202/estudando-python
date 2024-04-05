r1 = float(input("informe o comprimento da primeira reta: "))
r2 = float(input("informe o comprimento da segunda reta: "))
r3 = float(input("informe o comprimento da terceira reta: "))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("pode montar um triangulo")
else:
    print("Não pode montar um triangulo")

