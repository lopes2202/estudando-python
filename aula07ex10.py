produto = float(input("Digite o preço do produto: R$ "))

pagamentoaVista = produto - (produto * 10/100)
pagamentoParcelado = produto + (produto * 10/100)

print("O produto custa {}R$ e pagando a vista tem um desconto de 10% e começará a custar: {}R$.".format(produto, pagamentoaVista))
print("O produto custa {}R$ e pagando parcelado tem um aumento de 10% e começará a custar {}R$.".format(produto, pagamentoParcelado))