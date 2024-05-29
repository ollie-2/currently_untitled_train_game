
import pygame
from train import Train
from ticket import Ticket
import random
import time


# picks the secret word from word list and returns as UPPERCASE string
def pick_stations():
    station_list = []
    stops = []
    f = open("stations.txt", "r")
    for w in f:
        station_list.append(w.rstrip())
    f.close()

    r1 = random.randint(0, len(station_list) - 7)
    r2 = r1 + 7

    for station in station_list:
        if r1 < station_list.index(station) < r2:
            stops.append(station)

    return stops, r1, r2


def render_ticket(stops, first, last):
    if random.randint(1, 4) == 4:
        if random.randint(0, 1) == 1:
            first_stop = random.randint(0, first - 3)
            last_stop = random.randint(first_stop + 2, first - 1)
        else:
            first_stop = random.randint(last + 1, 151)
            last_stop = random.randint(first_stop + 2, 154)
    else:
        first_stop = random.randint(first, last - 3)
        last_stop = random.randint(first_stop, last)

    return first_stop, last_stop


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Arial', 45)
game_font = pygame.font.SysFont('Arial', 25)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# more vars
frame = 0
frames_from_start = 0
train_start_frame = 0
scene = 0
show_ticket = False
title = "Tickets, Please"
stop_animation = False
door_open = False
depart = False
door_closed = False


display_title = title_font.render(title, True, (255, 255, 255))

r = 50
g = 0
b = 100


# render the text for later

# train stations.txt

t = Train(2000, 60)
ticket = Ticket(0, 0)
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

stops, first_stop, last_stop = pick_stations()

stops_txt = str(stops)
print(stops_txt)

display_stops = game_font.render(stops_txt, True, (255, 255, 255))

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    clock.tick(60)
    if frame % 1 == 0:
        frames_from_start += 1
    if scene == 0:
        display_title = title_font.render(title, True, (255, 255, 255))
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            scene = 1

    if scene == 1:
        if train_start_frame == 0:
            train_start_frame = frames_from_start

        if not stop_animation:
            if frame % 1 == 0:
                stop_animation = t.action("arrive")
            if frame % 15 == 0:
                t.switch_image()

        if stop_animation and not door_open:
            if frame % 5 == 0:
                door_open = t.door_animation("open")

        if keys[pygame.K_RETURN]:
            depart = True

        if depart:
            if frame % 5 == 0:
                door_closed = t.door_animation("close")
            if door_closed:
                if frame % 1 == 0:
                    t.action("leave")
                if frame % 15 == 0:
                    t.switch_image()

        # TICKET LOGIC


    # Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    if scene == 0:
        screen.blit(display_title, (0, 0))
    if scene == 1:
        if show_ticket:
            screen.blit(ticket.image, ticket.rect)
        screen.blit(t.image, t.rect)
    pygame.display.update()

    frame += 1
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
