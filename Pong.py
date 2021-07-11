import pygame
import time
import random
from Vertical_bar import Vertical_bar
from Ball import Ball
import sys
from pygame.event import get

# Fix the bug with the ball going inside the vertical bars

# Initialize pygame font
pygame.font.init()

# Screen settings
width, height = 800, 600
background = (0, 0, 0)
text_color = (255, 255, 255)
window = pygame.display.set_mode((width, height))

# Bar dimensions
bar_width = 25
bar_height = 200

# Ball dimensions
ball_width = 25
ball_height = 25

horizontal_direction = ["Left", "Right"]
vertical_direction = ["Up" , "Down"]

pygame.display.set_caption("Pong game")

def main_menu():
    main_title_font1 = pygame.font.SysFont("comicsans", 100)
    subtitle_font2 = pygame.font.SysFont("comicsans", 70)
    subsubtitle_font3 = pygame.font.SysFont("comicsans", 40)
    run = True
    while run:
        window.fill(background)
        main_title_label = main_title_font1.render("PONG!", 1, text_color)
        subtitle_label = subtitle_font2.render("Press space bar to begin", 1, text_color)
        subsubtitle_label = subsubtitle_font3.render("W and S for left bar, and up and down arrow for right", 1, text_color)
        window.blit(main_title_label, (width / 2 - main_title_label.get_width() / 2, 200))
        window.blit(subtitle_label, (width / 2 - subtitle_label.get_width() / 2, 450))
        window.blit(subsubtitle_label, (width / 2 - subsubtitle_label.get_width() / 2, 550))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if keys[pygame.K_SPACE]:
                main()
            # Add the possibility for adjusting the resolution based off of the users preference
            if keys[pygame.K_TAB]:
                pass
    pygame.quit()

def main():
    run = True
    FPS = 60

    p1_points = 0
    p2_points = 0

    p1_vel = 7
    p2_vel = 7
    
    ball_vel_x = 7
    ball_vel_y = 7

    p1 = Vertical_bar(20, height / 2 - 100) # Left bar
    p2 = Vertical_bar(width - 25 - 20, height / 2 - 100) # Right bar

    ball = Ball(width / 2 - ball_width, height / 2 - ball_height)

    # Ball initially has a negative x-velocity
    if horizontal_direction[random.randint(0, 1)] == "Left":
        ball_vel_x *= -1

    # Ball initially has a negative y-velocity
    if vertical_direction[random.randint(0, 1)] == "Up":
        ball_vel_y *= -1

    key_label_font = pygame.font.SysFont("comicsans", 70)

    clock = pygame.time.Clock()

    def redraw_window():
        window.fill(background)
        score_font = pygame.font.SysFont("comicsans", 50)
        p1_score_label = score_font.render(f"P1 points: {p1_points}", 1, text_color)
        p2_score_label = score_font.render(f"P2 points: {p2_points}", 1, text_color)
        window.blit(p1_score_label, (0.2 * width, 10))
        window.blit(p2_score_label, (0.65 * width, 10))
        p1.draw(window)
        p2.draw(window)
        # pygame.display.flip()

        ball.draw(window)
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
        if keys[pygame.K_w] and p1.y - p1_vel > 0: # Up p1
            p1.move(-p1_vel)
        if keys[pygame.K_s] and p1.y + p1_vel + bar_height < height: # Down p1
            p1.move(p1_vel)

        if keys[pygame.K_UP] and p2.y - p2_vel > 0: # Up p2
            p2.move(-p2_vel)
        if keys[pygame.K_DOWN] and p2.y + p2_vel + bar_height < height: # Down p2
            p2.move(p2_vel)

        # Update ball's position
        ball.move(ball_vel_x, ball_vel_y)

        # Bounce of top or bottom of the windowdow
        if ball.y <= 0 or ball.y + ball_height >= height:
            ball_vel_y *= -1

        # Bounce of left or right side of the windowdow
        if ball.x <= 0 or ball.x + ball_width >= width:
            ball_vel_x *= -1
            if ball.x <= 0:
                p2_points = p2.add_points()
            else:
                p1_points = p1.add_points()

        # Register collision between the ball and one of the vertical bars
        ball_collide_left = ball.convert_to_rect().colliderect(p1.convert_to_rect())
        ball_collide_right = ball.convert_to_rect().colliderect(p2.convert_to_rect())

        # Reverse x direction of the ball if it collides with one of the bars
        if ball_collide_left or ball_collide_right:
            ball_vel_x *= -1

    pygame.quit()

main_menu()

