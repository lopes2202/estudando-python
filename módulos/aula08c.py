import math

catetoOPOSTO = float(input("Qual o valor do cateto oposto? "))
catetoADJACENTE = float(input("Qual o valor do cateto adjacente? "))
hipotenusa = catetoOPOSTO ** 2 + catetoADJACENTE ** 2

print("A hipotenusa desse triangula é {:.2f}".format(math.sqrt(hipotenusa)))

