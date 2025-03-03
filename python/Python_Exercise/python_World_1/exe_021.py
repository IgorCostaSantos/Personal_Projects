import pygame
pygame.init()  '''iniciar o pygame'''
pygame.mixer.music.load('''nome da musica''')
pygame.mixer.music.play()
pygame.event.wait()
