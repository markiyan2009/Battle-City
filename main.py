from classes import *
while run:
    for even in event.get():
        if even.type == K_DOWN:
            if even.key == K_ESCAPE:
                run = False
    main_win.fill(BLACK)
    display.update()
    clock.tick(fps)