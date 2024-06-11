import pygame
import math

pygame.init()

screen_h, screen_w = 540, 960
screen = pygame.display.set_mode((screen_w, screen_h))
font = pygame.font.SysFont(None, 50, False, False)

collision_time = 0
n = 1
v1, v2 = 0, -1
m1, m2 = 1, 1
v = [(v1, v2)]
p = [m1*v1 + m2*v2]
e = m2/2

blcok1 = pygame.Surface((100, 100))
blcok2 = pygame.Surface((125, 125))
wall = pygame.rect.Rect(25,0,15,500)

blcok1.fill((255,255,255))
blcok2.fill((255,255,255))

block1_x = 200
block2_x = 650
fps = 200

running = True
while running:
    pygame.time.Clock().tick(fps)

    n_text = font.render(str(n), False, (255,255,255))
    collision_time_text = font.render(str(collision_time), False, (255,255,255))

    block1_x += v1
    block2_x += v2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if 0 <= v1 <= v2:
        print(m2, collision_time)
        n += 1
        m2 += 1
        collision_time = 0
        block1_x = 200
        block2_x = 650
        v1, v2 = 0, -1
        v = [(v1, v2)]
        p = [m1*v1 + m2*v2]
        e = m2/2

    else:
        if block1_x + blcok1.get_size()[0] >= block2_x:
            a = m1 +m1**2/m2
            b = -(2*p[len(p)-1]*m1/m2) 
            c = p[len(p)-1]**2/m2 -2*e
            print((b**2)/4 - a*c)
            v1 = (-b -math.sqrt((b**2) - 4*a*c))/2*a    
            v2 = (v[len(v)-1])[0] - (v[len(v)-1])[1] + v1           
        if block1_x <= wall.bottomright[0]:
            v1 *= -1

        if block1_x + blcok1.get_size()[0] >= block2_x or block1_x <= wall.bottomright[0]:
            collision_time += 1
            p.append(m1*v1 + m2*v2)
            v.append((v1, v2))
            print((v1, v2))

    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (0,500), (screen_w, 500), 4)
    pygame.draw.rect(screen, (255,255,255), wall)
    screen.blit(n_text, (screen_w-n_text.get_size()[0],0))
    screen.blit(collision_time_text, (screen_w-collision_time_text.get_size()[0],50))
    screen.blit(blcok1, (block1_x, 500 - blcok1.get_size()[1]))
    screen.blit(blcok2, (block2_x, 500 - blcok2.get_size()[1]))
    pygame.display.update()

pygame.quit()