import pygame

# Bar dimensions
bar_width = 25
bar_height = 200

class Vertical_bar:
    def __init__(self, x, y, points=0):
        self.x = x
        self.y = y
        self.points = points
        self.shape = pygame.Surface((bar_width, bar_height))
        self.shape.fill((255, 255, 255))

    def draw(self, window):
        window.blit(self.shape, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def convert_to_rect(self):
        return self.shape.get_rect(x=self.x, y=self.y)

    def add_points(self):
        self.points += 1
        return self.points