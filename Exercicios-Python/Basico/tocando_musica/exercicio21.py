# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('mu.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#Por causa de algum motivo desconhecido não funciona


