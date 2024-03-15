from math import radians, sin , cos , tan

angulo = int(input("Fale um angulo qualquer: "))
seno = sin(radians(angulo))
print("O seno do angulo {}° é {:.2f}".format(angulo,seno))
cos = cos(radians(angulo))
print("O cosseno do angulo {}° é {:.2f}".format(angulo,cos))
tan = tan(radians(angulo))
print("A tangente do angulo {}° é {:.2f}".format(angulo, tan))
