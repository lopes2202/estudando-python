dinheiro = float(input("Quantos R$ você possui? "))
transformaEuro = dinheiro / 5.44
transforma = dinheiro / 3.27
print("Com {:.2f} R$ você pode comprar {:.2f} US$ " .format(dinheiro, transforma))

print("Com {:.2f} R$, você pode comprar {:.2f} €".format(dinheiro,transformaEuro))