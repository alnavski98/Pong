import pygame

# Ball dimensions
ball_width = 25
ball_height = 25

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = pygame.Surface((ball_width, ball_height))
        self.shape.fill((255, 255, 255))

    def draw(self, window):
        window.blit(self.shape, (self.x, self.y))

    def move(self, x_vel, y_vel):
        self.x += x_vel
        self.y += y_vel

    def convert_to_rect(self):
        return self.shape.get_rect(x=self.x, y=self.y)
