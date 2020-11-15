# Made by Pranshu Aggarwal

# Spin wheel in python

import pygame


#initialization
pygame.init()
dis = pygame.display.set_mode((800, 800))

white = [255,255,255]

f = []
for i in range(6):
    x  =input()
    f.append(x)

colors = ['orange', 'yellow', 'green', 'blue', 'purple', 'red']

pygame.display.set_caption("Spin Wheel")
image = pygame.image.load('wheel.png')
pointer = pygame.image.load('pointer.png')

#displaying the commands

green = (0, 255, 0) 
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 30) 
text = font.render('Press Space to stop', True, green, blue) 
text2 = font.render('Welcome to the spin wheel', True, green, blue) 


textRect = text.get_rect()  
textRect.center = (500, 500)

textrect = text2.get_rect()
textrect.center = (600,50)


angle = 0
run = True
while run :
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if keys[pygame.K_SPACE]:
        run = False
    else:
        angle+=90
    dis.fill((0,0,0))
    dis.blit(pygame.transform.rotate(image, angle), (100,100))
    dis.blit(pointer, (250,70))
    dis.blit(text, textRect)
    dis.blit(text2, textrect)
    pygame.display.update()


#color detection code
final = angle
while final>360:
    final-=360

if final>=0 and final<45:
    print(f[0])
elif final>=45 and final<90:
    print(f[1])
elif final>=90 and final<140:
    print(f[2])
elif final>=140 and final<200:
    print(f[3])
elif final>=200 and final<280:
    print(f[4])
elif final>=280 and final<=360:
    print(f[5])


pygame.quit()
