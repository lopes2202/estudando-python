salario = float(input("Informe seu salário: "))

novoSalario = salario + (salario * 15 /100 )

print("O salário antigo desse funcionário era de: {:.2f}R$ e agora com 15% de aumento passará a ser : {:.2f}R$" .format(salario, novoSalario))
