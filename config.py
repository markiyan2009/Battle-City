from pygame import*
import os
WHITE = (255,255,255)
BLACK = (0,0,0)

fps = 30
size_object = 50
win_width = 900
win_heigth = 600
main_win = display.set_mode((win_width,win_heigth))
clock = time.Clock()
bullet_speed = 15
run = True
speed = 5