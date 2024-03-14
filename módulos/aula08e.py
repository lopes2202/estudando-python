import random

apagar = ["Carlos", "Victor", "Gabriel", "Vitor"]
print("Quem vai ser o sorteado que irá apagar o quadro para o professor, {}".format(apagar))


sorteado = random.choice(apagar)

print("O sorteador da vez é: {}".format(sorteado))