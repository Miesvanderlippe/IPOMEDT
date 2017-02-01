import pygame

song = "siren.mp3"

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
