a = input('Digite algo: ')

print("O tipo primitivo desse valor é:" , type(a))

print("É um número? {}".format(a.isnumeric()))
print("Faz parte do alfabeto? {}".format(a.isalpha()))
print("Tem letra minuscula {}".format(a.islower()))
print("Tem letra maiscula {}" .format(a.isupper()))
print("Tem letra e numero {} " .format(a.isalnum()))
print("É decimal {}".format(a.isdecimal()))
print("Só tem espaços {}".format(a.isspace()))
print("Está capitalizada {} " .format(a.istitle()))


