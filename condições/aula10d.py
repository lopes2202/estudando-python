distancia = float(input("Qual é a distancia da viagem? "))

if distancia > 200:
    print("Você está prestes a começar uma viagem de {:.1f}Km.".format(distancia))
    dinheiro = distancia * 0.45
    print("A viagem custará: R${:.2f}".format(dinheiro))
else:
    print("Você está prestes a começar uma viagem de {:.1f}km".format(distancia))
    dinheiro = distancia * 0.50
    print("A viagem custará: R${:.2f}".format(dinheiro))
