import pygame
import random
import sys


pygame.init()

# Розміри екрану
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Кольори і в майбутньому шрифти
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# назва гри і екран
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Battle City")


background_image = pygame.image.load('background.jpg') # задній фон
# tank_image = pygame.image.load('tank.png') лого танка 


def draw_main_menu():
    screen.blit(background_image, (0, 0))
    # screen.blit(tank_image, (WIDTH/2 - tank_image.get_width()/2, HEIGHT/8)) виводить лого 
    draw_text("Battle City", pygame.font.Font(None, 100), WHITE, (WIDTH/2, HEIGHT/8 + 50), center=True) # назва гри
    draw_text("Грати", pygame.font.Font(None, 60), BLACK, (WIDTH/2, HEIGHT/4 + 90), center=True) # кнопка грати
    draw_text("Настройки", pygame.font.Font(None, 60), BLACK, (WIDTH/2, HEIGHT/3 + 110), center=True) # кнопка настройки
    draw_text("Вихід", pygame.font.Font(None, 36), WHITE, (WIDTH/2, HEIGHT/2 + 150), center=True) # кнопка вихід
    pygame.display.flip()

# Функція відображення тексту
def draw_text(text, font, color, pos, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = pos
    else:
        text_rect.topleft = pos
    screen.blit(text_surface, text_rect)

# Основний цикл програми
def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Вихід з гри
                if WIDTH/2 - 50 < event.pos[0] < WIDTH/2 + 50 and HEIGHT/2 + 150 - 18 < event.pos[1] < HEIGHT/2 + 150 + 18:
                    pygame.quit()
                    sys.exit()

        draw_main_menu()

# Запуск головного меню
if __name__ == '__main__':
    main_menu()