from classes import *
player_img = PATH +"img/player_tank.png"
tank = PlayerTank(player_img,win_heigth,win_width/2)
iron_block = PATH +"img/iron.jpg"
brick_img = PATH +"img/brick.jpg"
map_list = """0000bbbbiiiibbb000"""
def draw_map(map_list):
    last_x = 0
    last_y = 0
    brick =  GameSprite(brick_img,last_x,last_y)
    iron = GameSprite(iron_block,last_x,last_y)
    #max_width = 18; heioght = 12
    max_width = 18
    max_height = 12
    n = 0
    for block in map_list:
        brick =  GameSprite(brick_img,last_x,last_y)
        iron = GameSprite(iron_block,last_x,last_y)
        if int(last_x / size_object) == max_width:
            last_y += size_object
        if block == 'b':
            brick.reset()
            last_x += size_object
        elif block == "0":
            last_x+=size_object
        elif block == "i":
            iron.reset()
            last_x += size_object


       
   
while run:
    for even in event.get():
        if even.type == K_DOWN:
            if even.key == K_ESCAPE:
                run = False
    
  
    main_win.fill(BLACK)
    tank.update()
    tank.reset()
    draw_map(map_list)
    
    display.update()
    clock.tick(fps)
