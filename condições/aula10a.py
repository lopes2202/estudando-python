#import random

#num = int(input("Digite um numero de 0 a 5: "))

#numSorteado = 0, 1, 2, 3, 4, 5

#if num == random.choice(numSorteado):
 #   print("Parabéns, você conseguiu acertar o mesmo número que o computador!!")
#else:
  #  print("Infelizmente, você não conseguiu acertar... ")
   # print("TENTE NOVAMENTE!!!")

from random import randint

num = int(input("Digite um numero de 0 a 5: "))

numSorteado = randint(0,5)


if num == numSorteado:
    print("Parabéns, você conseguiu acertar o mesmo número que o computador!!")
else:
    print("Ganhei!! Eu pensei no numero {} e não no {} ".format(numSorteado, num))
    print("TENTE NOVAMENTE!!!")

