import pygame, sys
import os 

pygame.init()

wh = pygame.display.Info()
win = pygame.display.set_mode((wh.current_w-300,wh.current_h-350))
pygame.display.set_caption("PONG")


wid = wh.current_w-300
hei = wh.current_h-350
finish = False
fps = 60

#GAME OBJECTS

cursor_btn_Snd = pygame.mixer.Sound("game_data\music\main_menu_track.wav")
bg_Clr = pygame.Color('grey12')

menu_img = pygame.image.load('game_data\images\pong_menu.png')
mus_off_img = pygame.image.load('game_data\images\mus_off.png')
mus_on_img = pygame.image.load('game_data\images\mus_on.png')

clock = pygame.time.Clock()

btn_clr = (200,100,50)
btn_clr1 = (200,100,50)

s = int(50*wid/1300)
s1= int(50*wid/1300)
p_x = 360*wid/1300
p_y = 80*hei/850
e_x = 360*wid/1300
e_y = 80*hei/850

play_btn = pygame.Rect(0.346153846*wid,600*hei/850,p_x,p_y)
exit_btn = pygame.Rect(0.346153846*wid,740*hei/850,e_x,e_y)
mus_btn = pygame.Rect(1150*wid/1300,120*hei/850,80,80)

def scr_text(win,x,y,text,color,size):
    game_font = pygame.font.Font('freesansbold.ttf',size)
    scr_tx = game_font.render(text,True,color)
    win.blit(scr_tx,(x,y))

def check_mouse_pos(x,y,x1,y1):
    global btn_clr1
    global pos_x
    global pos_y
    if pos_x >= x and pos_x <= x1:
        if pos_y >=y and pos_y <= y1:
            btn_clr1 = (255,255,255)
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    else:
        btn_clr1 = (200,100,50)
        return False    

def chg_ply(x,y,x1,y1):
    global btn_clr
    global pos_x
    global pos_y
    if pos_x >= x and pos_x <= x1:
        if pos_y >=y and pos_y <= y1:
            btn_clr = (255,255,255)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    else:
        btn_clr = (200,100,50)
        return False  

def chg_snd(x,y,x1,y1):
    if pos_x >=x and pos_x <=x1:
        if pos_y  >=y and pos_y <= y1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

def change_Snd_on(x,y,x1,y1):
    global imgd
    global pl
    if pos_x >=x and pos_x <=x1:
        if pos_y  >=y and pos_y <= y1:
            if imgd == mus_off_img:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    imgd = mus_on_img
                    pl = True
pl = True
imgd = mus_on_img
while not finish:

    #1300,850


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
            
    clock.tick(fps-28)
    win.fill(bg_Clr)
    pos_x , pos_y = pygame.mouse.get_pos()
    win.blit(menu_img,(480*wid/1300,30*hei/850))
    win.blit(imgd,(1150*wid/1300,120*hei/850))

    pygame.draw.rect(win,btn_clr,play_btn)
    pygame.draw.rect(win,btn_clr1,exit_btn)
    

    scr_text(win,565*wid/1300,619*hei/850,"PLAY",(10,10,10),s)
    scr_text(win,565*wid/1300,759*hei/850,"EXIT",(10,10,10),s1)


     
    
    if check_mouse_pos(450*wid/1300,740*hei/850,810*wid/1300,820*hei/850):
        pygame.quit()
        sys.exit()

    elif chg_ply(450*wid/1300,600*hei/850,810*wid/1300,680*hei/850):
        pygame.quit()
        os.system('python PONG.py')

    if chg_snd(1150*wid/1300,120*hei/850,1230*wid/1300,200*hei/850):
        pl = False
        imgd = mus_off_img

                            
    if pl:
        cursor_btn_Snd.play()
    else:
        cursor_btn_Snd.stop()

    pygame.display.update()

sys.exit()