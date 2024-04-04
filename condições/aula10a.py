import random

num = int(input("Digite um numero de 0 a 5: "))

numSorteado = 0, 1, 2, 3, 4, 5

if num == random.choice(numSorteado):
    print("Parabéns, você conseguiu acertar o mesmo número que o computador!!")
else:
    print("Infelizmente, você não conseguiu acertar... ")
    print("TENTE NOVAMENTE!!!")

