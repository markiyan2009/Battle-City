from pygame import*
from abc import abstractmethod
import os
#PATH - місце розташування папки на компі
PATH = os.path.dirname(__file__) + os.path.sep

WHITE = (255,255,255)
BLACK = (0,0,0)
fps = 30
size_object = 50
win_width = 900
win_heigth = 600
main_win = display.set_mode((win_width,win_heigth))
clock = time.Clock()

run = True
speed = 5
# клас спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self,sprite_image : str, x : int, y : int):
        super().__init__()
        
        
        
        self.image = transform.scale(image.load(sprite_image),(size_object,size_object))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # куда повернена картинка
        self.angle = 0
        self.last_direction = "up"
    # поява спрайта
    def reset(self):
        
        main_win.blit(self.image,(self.rect.x,self.rect.y ))
#загальний клас танків
class Tank(GameSprite):
    #рух
    @abstractmethod
    def update(self):
        pass
    def shoot(self):
        pass
# клас гравця
class PlayerTank(Tank):
    
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_a]:

            self.rect.x -=speed
            
            
        elif keys_pressed[K_d]:
            self.rect.x +=speed
             
        elif keys_pressed[K_w]:
            self.rect.y -=speed
        elif keys_pressed[K_s]:
            self.rect.y +=speed
            
        
