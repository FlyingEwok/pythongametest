import pygame


pygame.init()



screen = pygame.display.set_mode((800,600))



#title and icon

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load('space-ship.png')

pygame.display.set_icon(icon)



#Player



playerImg = pygame.image.load('ship2.png')

playerX = 60				#initial positions

playerY = 500

playerX_change = 0

playerY_change = 0



def player(x,y):

    screen.blit(playerImg,(x,y))

    

running = True

while running:			#Main Code



  screen.fill((45,90,0))

     

  for event in pygame.event.get():

    if event.type== pygame.QUIT:

      running = False

  

    if event.type == pygame.KEYDOWN:		#left and right controls

        if event.key == pygame.K_LEFT:

            playerX_change = -0.1



        if event.key == pygame.K_RIGHT:

            playerX_change = 0.1





    if event.type == pygame.KEYUP:

        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

            playerX_change = 0



  playerX += playerX_change

  player(playerX,playerY)  



  pygame.display.update()