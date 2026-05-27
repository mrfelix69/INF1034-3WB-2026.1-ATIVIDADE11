import pygame, sys
from pygame.locals import QUIT
from pygame import *

init()

clock = time.Clock()
min_time = 0

careca_img = image.load('f-01.png')
#scale_careca = careca_img((500,250))

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
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                if K_SPACE == key.get_pressed():
                    run_animation = True


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

        if amin_time_mg > 100:
            curr_frame_mg += 1
            if curr_frame_mg > 4:
                curr_frame_mg = 0
                run_animation = False
            amin_time_mg = 0

    screen.fill((255,255,255))

    screen.blit(careca_walk_list[curr_frame],(100,250))

    screen.blit(demon_spritesheet,(400,200),(100 * curr_frame_mg, 100, 100, 100))

    screen.blit(demon_spritesheet,(400,200),((curr_frame_mg % 5) * 100,(curr_frame_mg // 5) * 100,100,100))

    display.update()