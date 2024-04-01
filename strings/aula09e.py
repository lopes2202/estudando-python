frase_tosca = str(input("Digite uma frase: ")).strip()


print("A letra A aparece {} vezes na frase".format(frase_tosca.lower().count("a")))

print("A primeira letra A aparece na posição : {} ".format(frase_tosca.lower()[1:].find("a")))

print("A ultima letra A aparece na posição: {}".format(frase_tosca.lower().rfind("a")+1))

