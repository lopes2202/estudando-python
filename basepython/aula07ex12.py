diasAlugados = int(input("Quantos dias alugado? "))
kmRodados = float(input("Quantos km rodados? "))

totalPagamento = (diasAlugados * 60) + (kmRodados * 0.15)

print("O total a pagar é de R${:.2f}" .format(totalPagamento))