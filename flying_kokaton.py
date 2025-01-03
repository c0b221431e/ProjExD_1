import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像Surfaceを作成
    bg_img2 = pg.image.load("fig/pg_bg.jpg") #背景画像7-1
    kk_img = pg.image.load("fig/3.png") #こうかとん画像Surfaceを作成
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとん画像の反転
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        key_lst = pg.key.get_pressed()
        move_x, move_y = 0, 0
        
        if key_lst[pg.K_UP]:
            move_y -= 1
        if key_lst[pg.K_DOWN]:
            move_y += 1
        if key_lst[pg.K_LEFT]:
            move_x -= 1
        if key_lst[pg.K_RIGHT]:
            move_x += 2
        kk_rct.move_ip(move_x, move_y)
        
        x = -(tmr%3200) 
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct) #screen Surfaceにこうかとん画像を張り付ける
        kk_rct.move_ip(-1, 0)
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()