nome = str(input("Digite seu nome: ")).strip()


print("Seu nome maisculo é: {}".format(nome.upper()))
print("Seu nome minusculo é: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))

primeiroNome = nome.split()

print("Seu primeiro nome é {} e tem {} letras ".format(primeiroNome[0], len(primeiroNome[0])))