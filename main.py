import pygame
from train import Train

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# more vars
frame = 0

r = 50
g = 0
b = 100

# render the text for later

t = Train(5000, 60)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
while run:
    clock.tick(60)

    if frame % 15 == 0:
        t.switch_image()
        print("SWITCH IMAGE!")


    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_l]:
        t.action("leave")
    if keys[pygame.K_a]:
        t.action("arrive")
    if t.x < -1200:
        t.x = 2000
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    screen.blit(t.image, t.rect)
    pygame.display.update()

    frame += 1
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
