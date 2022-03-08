#programa para reproduzir mp3

import pygame
pygame.init()
pygame.mixer.music.load('mario.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Teste')

