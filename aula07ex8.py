produto = float(input("Informe o preço do produto? R$ "))

novopreco = produto - (produto * 5 / 100)

print("O produto que custava {:.2f}, agora custa {:.2f} com a promoção de 5 %" .format(produto, novopreco))
