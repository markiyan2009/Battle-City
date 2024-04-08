from classes import *
player_img = PATH +"img/player_tank.png"
tank = PlayerTank(player_img,win_heigth,win_width/2)
iron_block = PATH +"img/iron.jpg"
brick_img = PATH +"img/brick.jpg"
map_list = [
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0],
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0],
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0],
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0]
]

def draw_map(map_list):
    
    last_x = 0
    last_y = 0
    n = 0
    
    
    last_line = 0
    
            
    #max_width = 18; heioght = 12
    max_width = 18
    max_height = 12
    def closure():
        nonlocal last_line, last_x, last_y
        brick =  GameSprite(brick_img,last_x,last_y)
        iron = GameSprite(iron_block,last_x,last_y)
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
                    brick.reset()
                    print(last_x)
                    last_x += size_object
                elif block == 0:
                    print(last_x)
                    last_x+=size_object
                elif block == "i":
                    iron = GameSprite(iron_block,last_x,last_y)
                    iron.reset()
                    print(last_x)
                    last_x += size_object
        last_x = 0
        last_y = 0
    return closure

       
draw_Map = draw_map(map_list)
while run:
    for even in event.get():
        if even.type == K_DOWN:
            if even.key == K_ESCAPE:
                run = False
    
    main_win.fill(BLACK)
    draw_Map()
    
    tank.update()
    tank.reset()
       
    
    display.update()
    clock.tick(fps)
