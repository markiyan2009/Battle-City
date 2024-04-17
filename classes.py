 from config import*
from time import time as timer
from abc import abstractmethod

import math
#PATH - місце розташування папки на компі
PATH = os.path.dirname(__file__) + os.path.sep



brick_list = sprite.Group()
iron_list = sprite.Group()

iron_block = PATH +"img/iron.jpg"
brick_img = PATH +"img/brick.jpg"
def draw_map(map_list):
    
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
                brick_list.add(brick)
                print(last_x)
                last_x += size_object
            elif block == 0:
                print(last_x)
                last_x+=size_object
            elif block == "i":
                iron = GameSprite(iron_block,last_x,last_y)
                iron_list.add(iron)
                print(last_x)
                last_x += size_object
            
    #max_width = 18; heioght = 12
    
    def closure():
        nonlocal last_line, last_x, last_y
        brick_list.draw(main_win)
        iron_list.draw(main_win)
        last_x = 0
        last_y = 0
    return closure
# клас спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self,sprite_image : str, x : int, y : int):
        super().__init__()
        
        self.hp = 5
        self.last_time = timer()
        self.current_time = None
        self.shoot_time = random.randint(2,4)
        self.image = transform.scale(image.load(sprite_image),(size_object,size_object))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_x = self.rect.x
        self.last_y = self.rect.y
        self.bullets = sprite.Group()
        # куда повернена картинка
        self.direction = "down"
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
        
        bullet = Bullet(self)
        self.bullets.add(bullet)
        
    def calculate_image_rotate(self,future_direction):
        if self.last_direction == "up" and future_direction == "right":
           self.image = transform.rotate(self.image, -90)
        if self.last_direction == "up" and future_direction == "left":
           self.image = transform.rotate(self.image, 90)
        if self.last_direction == "up" and future_direction == "down":
           self.image = transform.rotate(self.image, 180)
        if self.last_direction == "down" and future_direction == "right":
           self.image = transform.rotate(self.image, 90)
        if self.last_direction == "down" and future_direction == "left":
           self.image = transform.rotate(self.image, -90)
        if self.last_direction == "down" and future_direction == "up":
           self.image = transform.rotate(self.image, -180)
        if self.last_direction == "right" and future_direction == "up":
           self.image = transform.rotate(self.image, 90)
        if self.last_direction == "right" and future_direction == "down":
           self.image = transform.rotate(self.image, -90)
        if self.last_direction == "right" and future_direction == "left":
           self.image = transform.rotate(self.image, 180)
        if self.last_direction == "left" and future_direction == "right":
           self.image = transform.rotate(self.image, 180)
        if self.last_direction == "left" and future_direction == "up":
           self.image = transform.rotate(self.image, -90)
        if self.last_direction == "left" and future_direction == "down":
           self.image = transform.rotate(self.image, 90)

            
# клас гравця
class PlayerTank(Tank):
    
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_a]:
            self.last_x = self.rect.x
            self.rect.x -=speed
            self.calculate_image_rotate("left")
            self.last_direction = "left"
            
        elif keys_pressed[K_d]:
            self.last_x = self.rect.x
            self.rect.x +=speed
            self.calculate_image_rotate("right")
            self.last_direction = "right"
            
        elif keys_pressed[K_w]:
            self.last_y = self.rect.y
            self.rect.y -=speed
            self.calculate_image_rotate("up")
            self.last_direction = "up"
            
        elif keys_pressed[K_s]:
            self.last_y = self.rect.y
            self.rect.y +=speed
            self.calculate_image_rotate("down")
            self.last_direction = "down"
        if sprite.spritecollide(self,iron_list, False) or sprite.spritecollide(self,brick_list, False):

            self.rect.x = self.last_x
            self.rect.y = self.last_y
            
        
        
class EnemyTank(Tank):
    def set_direction(self,target):
        if self.rect.y > target.rect.y:
            
            self.direction = self.last_direction  = "up"
        elif self.rect.y < target.rect.y:
            self.direction = self.last_direction  ="down"
        elif self.rect.x > target.rect.x:
                
            self.direction = self.last_direction  = "left"

        elif self.rect.x < target.rect.x:
            self.direction = self.last_direction  = "right"
    def update(self, target):
        if sprite.spritecollide(self,iron_list,False) or sprite.spritecollide(self,brick_list,False):

            print("collide")
            self.direction = None
            if self.rect.x > target.rect.x and self.last_direction != "left":
                self.direction = "left"
            elif self.rect.x < target.rect.x and self.last_direction != "right":
                self.direction = "right"
            elif self.rect.y > target.rect.y and self.last_direction != "up":
                self.direction = "up"
            elif self.rect.y < target.rect.y and self.last_direction != "down":
                self.direction = "down"
        else:   
            self.set_direction(target)
            
    
            

        if self.direction == "down":
            self.rect.y += speed
        elif self.direction == "up":
            self.rect.y -= speed
        elif self.direction == "right":
            self.rect.x += speed
        elif self.direction == "left":
            self.rect.x -= speed
        self.current_time = timer()
        if int(self.current_time) - int(self.last_time) == self.shoot_time:
            self.shoot()
            self.shoot_time = random.randint(2,4)
            self.last_time = timer()


class Bullet(sprite.Sprite):
    def __init__(self,owner):
        super().__init__()
        self.image = transform.scale(image.load(PATH + "img/bullet.png"),(30,30))
        self.rect = self.image.get_rect()
        self.direction = owner.last_direction
        self.rect.x = owner.rect.x
        self.rect.y = owner.rect.y
        if self.direction == "right":
            self.image = transform.rotate(self.image,-90)
            
        elif self.direction == "left":
            self.image = transform.rotate(self.image,90)
        if self.direction == "down":
            self.image = transform.rotate(self.image,180)
    def update(self):
        if self.rect.x <=0 or self.rect.x >= win_width or self.rect.y<=0 or self.rect.y >=win_heigth:
            self.kill()
            print("no bullet")
        if self.direction == "up":
            self.rect.y -= bullet_speed
        elif self.direction == "right":
            self.rect.x += bullet_speed
        elif self.direction == "left":
            self.rect.x -= bullet_speed
        elif self.direction == "down":
            self.rect.y += bullet_speed
        if sprite.spritecollide(self,brick_list,True) or sprite.spritecollide(self,iron_list,False):
            self.kill()


