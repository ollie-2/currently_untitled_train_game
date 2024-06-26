import pygame


class Ticket:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Ticket.png")
        self.image_list = [
            "Ticket.png",
            "Ticket_invalid.png",
            "Ticket_valid.png"
        ]
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 12, self.image_size[1] * 12)
        self.image = pygame.transform.scale(self.image, scale_size)

    def switch_image(self, mode):
        self.image = pygame.image.load(self.image_list[mode])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()

    # def slide(self, left_only):
    #     if left_only:
    #         self.x = 2000
    #         if self.x > 1500:
    #             self.x -= 10
    #         else:
    #             self.x = 1500
