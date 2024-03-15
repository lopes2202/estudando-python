import pygame

pygame.mixer.init()
pygame.mixer.music.load('coldplaaay2.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
x = input('Digite algo para parar... ')
