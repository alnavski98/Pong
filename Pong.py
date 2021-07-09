import pygame
import time
import random
from Vertical_bar import Vertical_bar
from Ball import Ball
from pygame.event import get

# Initialize pygame font
pygame.font.init()

# Screen settings
width, height = 1500, 750
bg = 0, 0, 0
text_color = 255, 255, 255
win = pygame.display.set_mode((width, height))

# Bar dimensions
bar_width = 25
bar_height = 200

# Ball dimensions
ball_width = 25
ball_height = 25

horizontal_direction = ["Left", "Right"]
vertical_direction = ["Up" , "Down"]

pygame.display.set_caption("Pong game")

def main():
    run = True
    FPS = 60

    p1_points = 0
    p2_points = 0

    p1_vel = 7
    p2_vel = 7
    
    ball_vel_x = 5
    ball_vel_y = 5

    p1 = Vertical_bar(50, height / 2 - 100) # Left bar
    p2 = Vertical_bar(1425, height / 2 - 100) # Right bar

    ball = Ball(width / 2 - ball_width, height / 2 - ball_height)

    # If left wall is hit
    if horizontal_direction[random.randint(0, 1)] == "Left":
        ball_vel_x *= -1

    # If right wall is hit
    if vertical_direction[random.randint(0, 1)] == "Up":
        ball_vel_y *= -1

    key_label_font = pygame.font.SysFont("comicsans", 70)

    clock = pygame.time.Clock()

    def redraw_window():
        win.fill(bg)
        # main_font = pygame.font.SysFont("comicsans", 50)
        # p1_points_label = main_font.render(f"P1 points: {p1_points}", 1, text_color)

        p1.draw(win)
        p2.draw(win)
        # pygame.display.flip()

        ball.draw(win)
        # win.blit("")
        pygame.display.update()

        ball_collide = False

    while run:
        clock.tick(FPS)
        redraw_window()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_ESCAPE]:
                main_menu()

        # Move one of the vertical bars using keys on keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and p1.y - p1_vel > 0: # up
            p1.move(-p1_vel)
        if keys[pygame.K_s] and p1.y + p1_vel + bar_height < height: # down
            p1.move(p1_vel)

        if keys[pygame.K_UP] and p2.y - p2_vel > 0: # up
            p2.move(-p2_vel)
        if keys[pygame.K_DOWN] and p2.y + p2_vel + bar_height < height: # down
            p2.move(p2_vel)

        # Update ball's position
        ball.move(ball_vel_x, ball_vel_y)

        # Bounce of top or bottom of the window
        if ball.y <= 0 or ball.y + ball_height >= height:
            ball_vel_y *= -1

        # Register collision between the ball and one of the vertical bars
        ball_collide_left = ball.convert_to_rect().colliderect(p1.convert_to_rect())
        ball_collide_right = ball.convert_to_rect().colliderect(p2.convert_to_rect())

        # Reverse x direction of ball if it collides with one of the bars
        if ball_collide_left or ball_collide_right:
            ball_vel_x *= -1

    pygame.quit()

def main_menu():
    title_font1 = pygame.font.SysFont("comicsans", 100)
    title_font2 = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        win.fill(bg)
        title_label1 = title_font1.render("PONG!", 1, text_color)
        title_label2 = title_font2.render("Press space bar to begin", 1, text_color)
        win.blit(title_label1, (width / 2 - title_label1.get_width() / 2, 200))
        win.blit(title_label2, (width / 2 - title_label2.get_width() / 2, 450))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_SPACE]:
                main()
    pygame.quit()

main_menu()

