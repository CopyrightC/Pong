import pygame
from pygame import mixer
import sys
import time
import os
import random

pygame.init()
mixer.init()
pygame.font.Font("freesansbold.ttf", 64)
sound1 = mixer.Sound("music\gameover.wav")
wh = pygame.display.Info()


def chg_clr(x, y, x1, y1):
    global play_clr
    pos_x, pos_y = pygame.mouse.get_pos()

    if pos_x >= x and pos_x <= x1:
        if pos_y >= y and pos_y <= y1:
            play_clr = (120, 40, 10)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                os.system("python PONG.py")

        else:
            play_clr = (255, 165, 0)


def chg_clrex(x, y, x1, y1):
    global exit_clr
    pos_x, pos_y = pygame.mouse.get_pos()

    if pos_x >= x and pos_x <= x1:

        if pos_y >= y and pos_y <= y1:
            exit_clr = (120, 40, 10)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()

        else:
            exit_clr = (255, 165, 120)


def ball_movement():
    global score
    global velo_ball_x1
    global velo_ball_y1

    ball.x = ball.x + velo_ball_x1
    ball.y = ball.y + velo_ball_y1

    if ball.top <= 0 or ball.bottom >= height:
        velo_ball_y1 *= -1

    if ball.left <= 0:
        mixer.Sound("music\BALL HIT.wav").play()
        velo_ball_x1 *= -1

    if ball.right >= width:
        velo_ball_x1 *= -1

    if ball.colliderect(user):
        mixer.Sound("music\BALL HIT.wav").play()
        velo_ball_x1 *= -1
        score = score + 1

    if ball.colliderect(computer_AI):
        mixer.Sound("music\BALL HIT.wav").play()
        velo_ball_x1 *= -1


def screen_text(win, text, color, x, y):
    text_Screen = game_font.render(text, True, color)
    display_Window.blit(text_Screen, (x, y))


def screen_text4(win, text, color, x, y, s):
    game_font4 = pygame.font.Font("freesansbold.ttf", s)
    text_Screen = game_font4.render(text, True, color)
    display_Window.blit(text_Screen, (x, y))


def screen_text_Small(win, text, color, x, y):
    pygame.font.Font("freesansbold.ttf", 32)
    text_Screen_sm = game_font_small.render(text, True, color)
    display_Window.blit(text_Screen_sm, (x, y))


def screen_text_Small1(win, text, color, x, y, s):
    game_font_small1 = pygame.font.Font("freesansbold.ttf", s)
    text_Screen_sm = game_font_small1.render(text, True, color)
    display_Window.blit(text_Screen_sm, (x, y))


width = wh.current_w
height = wh.current_h

music = True
score = 0

white = (255, 255, 255)

display_Window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("PONG GAME")
background_color = pygame.Color("grey12")

velo_ball_x = [7, -7]
velo_ball_y = [7, -7]

velo_ball_x1 = random.choice(velo_ball_x)
velo_ball_y1 = random.choice(velo_ball_y)

AI_velocity_Y = 7.8
user_velocity_Y = 0

game_font = pygame.font.Font("freesansbold.ttf", 64)
game_font_small = pygame.font.Font("freesansbold.ttf", 32)

# GAME_OBJECTS


b_w = int(30 * width / 1600)
h_w = int(30 * width / 1600)

ball = pygame.Rect(width / 2 - (b_w / 2), height / 2 - (h_w / 2), b_w, h_w)
user = pygame.Rect(width - 20, height / 2 - 70, int(10 * width / 1600), int(140 * height / 1200))
computer_AI = pygame.Rect(10, height / 2 - 70, int(10 * width / 1600), int(140 * height / 1200))
aaline = (200, 200, 200)

over = False
close = False
sleep = True

boolx = True
sy = 0
hk = (width / 2, height)
play_clr = (255, 165, 0)
exit_clr = (255, 165, 120)

play_gn = pygame.Rect(420 * width / 1600, 780 * height / 1200, int(260 * width / 1600), int(60 * height / 1200))
exit_gn = pygame.Rect(880 * width / 1600, 780 * height / 1200, int(260 * width / 1600), int(60 * height / 1200))

while not close:

    if user.top <= 10:
        user.top = 10
    if user.bottom >= height - 10:
        user.bottom = height - 10
    if computer_AI.top < ball.y:
        computer_AI.y += AI_velocity_Y
    if computer_AI.bottom > ball.y:
        computer_AI.y -= AI_velocity_Y
    if ball.right >= width:
        over = True
        music = True

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                user_velocity_Y += 7

            if event.key == pygame.K_UP:
                user_velocity_Y -= 7

        if event.type == pygame.KEYUP:
            user_velocity_Y = 0

    ball_movement()

    user.y += user_velocity_Y

    display_Window.fill(background_color)

    if over:
        if boolx:
            sound1.play()
            boolx = False


        user.x = 1000000
        user.y = 100000
        ball.x = 1000000
        ball.y = 1000000
        computer_AI.x = 10000
        computer_AI.y = 10000
        aaline = (255, 255, 255)
        hk = (10000, 10000)

        display_Window.fill(white)

        screen_text4(display_Window, "GAME OVER", (0, 0, 0), width / 2 - (320*width/1600), 60 * height / 1200, int(95 * width * height / 1920000))

        screen_text4(
            display_Window, f"Score : {score}", (0, 0, 0), 640 * width / 1600, 380 * height / 1200,
            int(60 * width * height / 1920000)
        )
        sy = 11110

        pygame.draw.rect(display_Window, play_clr, play_gn)
        pygame.draw.rect(display_Window, exit_clr, exit_gn)

        screen_text_Small1(display_Window, "PLAY AGAIN", (0, 0, 0), 428 * width / 1600, 789 * height / 1200,
                           int(38 * width * height / 1920000))

        screen_text_Small1(display_Window, "EXIT", (0, 0, 0), 946 * width / 1600, 790 * height / 1200,
                           int(38 * width * height / 1920000))

        chg_clr(428 * width / 1600, 789 * height / 1200, 688 * width / 1600, 849 * height / 1200)
        chg_clrex(946 * width / 1600, 790 * height / 1200, 1206 * width / 1600, 1006 * height / 1200)

    screen_text_Small(display_Window, "Score : " + str(score), (200, 100, 60), 0, sy)
    pygame.draw.ellipse(display_Window, (200, 200, 200), ball)
    pygame.draw.rect(display_Window, (200, 200, 200), user)
    pygame.draw.rect(display_Window, (200, 200, 200), computer_AI)
    m = pygame.draw.aaline(display_Window, aaline, (width / 2, 0), hk)

    pygame.display.update()
    clock.tick(60)

    if sleep == True:
        time.sleep(1.3)
        sleep = False
