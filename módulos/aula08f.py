from random import shuffle

nome1 = str(input("Qual o nome do primeiro aluno: "))
nome2 = str(input("Qual o nome do segundo aluno: "))
nome3 = str(input("Qual o nome do terceiro aluno: "))
nome4 = str(input("Qual o nome do quarto aluno: "))


lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print("O primeiro a apresentar o trabalho vai ser e a ordem será:", lista)