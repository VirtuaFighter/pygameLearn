import pygame
pygame.init()

screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("First Game")


x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True  #GameLoop
while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #setup a list...
        keys = pygame.key.get_pressed()

        #note python 0,0 = top left
        if keys[pygame.K_LEFT] and x > vel:  #adding the and clause, so if there isn't enough pixels left on the left, it won't subtract anymore (per vid..)
            x -= vel
        if keys[pygame.K_RIGHT] and x < (screenWidth - width): 
            x += vel
        if not(isJump):  
            if keys[pygame.K_UP] and y > vel:
                y -= vel
            if keys[pygame.K_DOWN] and y < (screenHeight - height):
                y += vel
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                        neg = -1 #to move it down
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        win.fill((0,0,0))
        
        pygame.draw.rect(win, (255,0,0), (x,y,width,height))
        pygame.display.update()

pygame.quit()
