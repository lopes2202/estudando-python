from math import hypot

catetoOPOSTO = float(input("Qual o valor do cateto oposto? "))
catetoADJACENTE = float(input("Qual o valor do cateto adjacente? "))
hipotenusa = hypot(catetoOPOSTO, catetoADJACENTE)

print("A hipotenusa desse triangulo vai medir {:.2f}".format(hipotenusa))

