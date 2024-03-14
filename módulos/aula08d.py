import math

angulo = int(input("Fale um angulo qualquer: "))

print("O seno do angulo {}° é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))