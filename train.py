import pygame


class Train:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Train_Mint_move1.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 10
        self.speed = 0
        self.mod = 0.05
        self.in_station = False

    def action(self, direction):
        if direction == "arrive":
            self.speed = (self.x - 460)/500
            if self.x > 500:
                self.x -= self.speed
            else:
                self.in_station = True
                self.x = 500
        if direction == "leave":
            if not self.in_station:
                self.speed = 5
                self.in_station = True
            self.speed = 2 ** self.mod
            self.mod -= 0.005
            if self.speed < 0.25:
                self.speed = 0
        self.x -= self.speed
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])



