import pygame, sys
from pygame.locals import QUIT
from pygame import *

init()

clock = time.Clock()
min_time = 0

careca_img = image.load('f-01.png')

curr_frame = 0
careca_walk_list = []

for i in range(4):
    careca_walk_list.append(image.load(f'f-0{i+1}.png'))

run_animation = False

curr_frame_mg = 0
amin_time_mg = 0

demon_spritesheet = image.load('rundemon_spritesheet.png')

screen = display.set_mode((1200,700))

while True:

    for ev in event.get():

        if ev.type == QUIT:
            quit()
            sys.exit()

    keys = key.get_pressed()

    if keys[K_SPACE]:
        run_animation = True
    else:
        run_animation = False
        curr_frame_mg = 0

    clock.tick(60)

    dt = clock.get_time()

    min_time += dt

    if min_time > 150:

        curr_frame += 1

        if curr_frame > len(careca_walk_list) - 1:
            curr_frame = 0

        min_time = 0

    amin_time_mg += dt

    if run_animation == True:

        if amin_time_mg > 200:
            curr_frame_mg += 1

            if curr_frame_mg > 7:
                curr_frame_mg = 0

            amin_time_mg = 0

    screen.fill((255,255,255))

    screen.blit(careca_walk_list[curr_frame],(100,250))
    #frame = 

    #screen.blit(demon_spritesheet,(400,200),((curr_frame_mg % 5) * 100,(curr_frame_mg // 5) * 100,96,100))

    frame = demon_spritesheet.subsurface(((curr_frame_mg % 8) * 96, 0, 96, 96))

    frame = pygame.transform.scale(frame,(192,192))

    screen.blit(frame,(400,200))

    display.update()