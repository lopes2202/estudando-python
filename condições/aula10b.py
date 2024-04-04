velocidade = float(input("Com qual velocidade esse veiculo estava: "))


if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido de 80 Km/h")
    multa = (velocidade-80) * 7
    print("Voce deve pagar uma multa de {} R$".format(multa))
else:
    print("Tenha um Bom Dia, dirija com cuidado!")
