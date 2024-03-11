altura = float(input('Informe a altura da parede em M: '))
largura = float(input('Informe a largura da parede em M: '))

algura = altura * largura

print("Sua parede tem a dimensão de {} x {} e sua área é de {}m².".format(altura, largura, algura))
print("A quantidade de tinta que sera utilizada será de {} litros. ".format(algura / 2))