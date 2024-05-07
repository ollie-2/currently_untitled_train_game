import pygame


class Train:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.door_image_list = ["Train_Mint_open1.png", "Train_Mint_open2.png", "Train_Mint_open3.png",
                                "Train_Mint_open4.png", "Train_Mint_open5.png", "Train_Mint_open6.png",
                                "Train_Mint_open7.png", "Train_Mint_open8.png", "Train_Mint_open9.png",
                                "Train_Mint_open10.png", "Train_Mint_open11.png", "Train_Mint_open12.png",
                                "Train_Mint_open13.png", "Train_Mint_open14.png", ]
        self.move_image_list = ["Train_Mint_move1.png", "Train_Mint_move2.png"]
        self.image = pygame.image.load(self.move_image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 10
        self.speed = 0
        self.mod = 0.05
        self.door_number = 0
        self.in_station = False
        self.move_animation = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 6, self.image_size[1] * 6)
        self.image = pygame.transform.scale(self.image, scale_size)

    def action(self, direction):
        if direction == "arrive":
            if self.x >= 400:
                self.x -= 0.015 * (self.x - 360)
            elif not self.in_station:
                self.x = 400
                self.in_station = True

        if direction == "leave":
            if self.x >= -1400:
                self.x -= 0.015 * (440 - self.x)

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def switch_image(self):
        image_number = 0
        if not self.move_animation:
            image_number = 1
        self.image = pygame.image.load(self.move_image_list[image_number])
        self.move_animation = not self.move_animation

        self.rescale_image(self.image)
        self.image_size = self.image.get_size()

    def door_animation(self, door_direction):
        if door_direction == "open":
            self.door_number += 1
        if not self.move_animation:
            image_number = 1
        self.image = pygame.image.load(self.move_image_list[self.door_number])

        self.rescale_image(self.image)
        self.image_size = self.image.get_size()

