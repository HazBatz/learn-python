import pygame as p

p.init()

SCREEN_HEIGHT = 2000
SCREEN_WIDTH = 4000

screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = p.Rect(300, 250, 50, 50)

run = True
while run:

    screen.fill((0, 0, 0))

    p.draw.rect(screen, (255, 0, 0), player)

    key = p.key.get_pressed()
    if key[p.K_q] == True:
        player.move_ip(-1, 0)
    elif key[p.K_d] == True:
      player.move_ip(1, 0)
    elif key[p.K_z] == True:
        player.move_ip(0, -1)
    elif key[p.K_s] == True:
        player.move_ip(0, 1)

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()

p.quit()



