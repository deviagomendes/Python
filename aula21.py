import pygame
pygame.init()

pygame.mixer.music.load('motivacional.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()