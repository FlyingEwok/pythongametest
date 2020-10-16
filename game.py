import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))



#title and icon

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load('computer.png')

pygame.display.set_icon(icon)

 

running = True

while running:			#Main Code



  for event in pygame.event.get():

    if event.type== pygame.QUIT:

      running = False