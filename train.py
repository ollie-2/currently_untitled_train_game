import pygame


class Train:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["Train_Mint_move1.png", "Train_Mint_move2.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 10
        self.speed = 0
        self.mod = 0.05
        self.in_station = False
        self.move_animation = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)

    def action(self, direction):
        if direction == "arrive":
            self.speed = (self.x - 46)/250
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

    def switch_image(self):
        image_number = 0
        if not self.move_animation:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.move_animation = not self.move_animation


