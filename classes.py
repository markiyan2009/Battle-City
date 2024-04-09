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
block_list = sprite.Group()
iron_block = PATH +"img/iron.jpg"
brick_img = PATH +"img/brick.jpg"
def draw_map(map_list):
    global block_list 
    last_x = 0
    last_y = 0
    n = 0
    
    
    max_width = 18
    max_height = 12
    last_line = 0
    for line in map_list:
        for block in line: 
            if int(last_x / size_object) == max_width:
                last_x = 0
                last_y += size_object
            if int(last_y / size_object) == max_height:
                last_y = 0
                last_x = 0
            if block == 'b':
                brick =  GameSprite(brick_img,last_x,last_y)
                block_list.add(brick)
                print(last_x)
                last_x += size_object
            elif block == 0:
                print(last_x)
                last_x+=size_object
            elif block == "i":
                iron = GameSprite(iron_block,last_x,last_y)
                block_list.add(iron)
                print(last_x)
                last_x += size_object
            
    #max_width = 18; heioght = 12
    
    def closure():
        nonlocal last_line, last_x, last_y
        block_list.draw(main_win)
        
        last_x = 0
        last_y = 0
    return closure
# клас спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self,sprite_image : str, x : int, y : int):
        super().__init__()
        
        
        
        self.image = transform.scale(image.load(sprite_image),(size_object,size_object))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_x = self.rect.x
        self.last_y = self.rect.y
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
            self.last_x = self.rect.x
            self.rect.x -=speed
            
            
        elif keys_pressed[K_d]:
            self.last_x = self.rect.x
            self.rect.x +=speed
             
        elif keys_pressed[K_w]:
            self.last_y = self.rect.y
            self.rect.y -=speed
        elif keys_pressed[K_s]:
            self.last_y = self.rect.y
            self.rect.y +=speed
        if sprite.spritecollide(self,block_list, False):

            self.rect.x = self.last_x
            self.rect.y = self.last_y
class EnemyTank(GameSprite):
    def update(self):
        pass
class Bullet(sprite.Sprite):
    def __init__(self,x,top):
        self.image = transform.scale(image.load(PATH + "img/bullet.png"),(30,30))
        
        
