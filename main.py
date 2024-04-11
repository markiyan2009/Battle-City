from classes import *
player_img = PATH +"img/player_tank.png"
tank = PlayerTank(player_img,size_object,size_object)

map_list = [
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0],
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0],
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0],
    [0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0,"b","b",0,0],
    [0,0,"i","i",0,0,"i","i",0,0,"i","i",0,0,"i","i",0,0]
]


       
draw_Map = draw_map(map_list)
while run:
    for even in event.get():
        if even.type == KEYDOWN:
            if even.key == K_ESCAPE:
                run = False
    
    main_win.fill(BLACK)
    draw_Map()
    
    
    tank.reset()
    tank.update()
    display.update()
    clock.tick(fps)
