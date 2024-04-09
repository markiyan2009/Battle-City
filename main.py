from classes import *
player_img = PATH +"img/player_tank.png"
tank = PlayerTank(player_img,win_heigth,win_width/2)

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
        if even.type == K_DOWN:
            if even.key == K_ESCAPE:
                run = False
    
    main_win.fill(BLACK)
    draw_Map()
    
    
    tank.reset()
    tank.update()
    display.update()
    clock.tick(fps)
