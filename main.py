import pygame
from train import Train
from ticket import Ticket
import random
# import time


# picks the secret word from word list and returns as UPPERCASE string
def pick_stations():
    station_list = []
    d_stops = []

    
    f = open("stations.txt", "r", encoding="utf-8")
    for w in f:
        station_list.append(w.rstrip())
    f.close()

    r1 = random.randint(0, len(station_list) - 7)
    r2 = r1 + 7

    for station in station_list:
        if r1 < station_list.index(station) < r2:
            d_stops.append(station)

    return d_stops, r1, r2, station_list


def ticket_stops(first, last):
    if random.randint(1, 4) == 4:
        invalid_ticket = True
        if random.randint(0, 1) == 1:
            t_first_stop = random.randint(0, first - 3)
            t_last_stop = random.randint(t_first_stop + 2, last - 1)
        else:
            t_first_stop = random.randint(last + 1, 151)
            t_last_stop = random.randint(t_first_stop + 2, 154)
    else:
        invalid_ticket = False
        t_first_stop = random.randint(first, last - 3)
        t_last_stop = random.randint(t_first_stop, last)
    if t_last_stop - t_first_stop >= 6:
        t_last_stop = t_first_stop + 6
    return t_first_stop, t_last_stop, invalid_ticket


# set up pygame modules
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Tiny5 - Regular', 125)
game_font = pygame.font.SysFont('Tiny5 - Regular', 25)
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
score = 0
show_ticket = False
title = "Tickets, Please"
stop_animation = False
door_open = False
depart = False
door_closed = False
new_ticket = False
no_ticket = True
invalid = False

display_ticket1 = game_font.render("ERROR: display_ticket1 undef", True, (255, 255, 255))
display_ticket2 = game_font.render("ERROR: display_ticket2 undef", True, (255, 255, 255))
display_title = title_font.render(title, True, (255, 255, 255))

r = 50
g = 0
b = 100


# render the text for later

# train stations.txt

t = Train(2000, 60)
ticket = Ticket(1500, 30)
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

stops, first_stop, last_stop, list_stations = pick_stations()

stops_txt = ", ".join(stops)
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
        if door_open and no_ticket:
            new_ticket = True
            no_ticket = False
        if new_ticket:
            ticket_from, ticket_to, invalid = ticket_stops(first_stop, last_stop)
            print(invalid)
            ticket_text1 = "From: " + list_stations[ticket_from]
            ticket_text2 = "To: " + list_stations[ticket_to]
            display_ticket1 = game_font.render(ticket_text1, True, (255, 255, 255))
            display_ticket2 = game_font.render(ticket_text2, True, (255, 255, 255))
            print(ticket_text1, "\n" + ticket_text2)
            new_ticket = False
            show_ticket = True
        if keys[pygame.K_y]:
            if not invalid:
                ticket.switch_image(2)
                score += 1
            else:
                ticket.switch_image(1)
                score -= 1
        elif keys[pygame.K_n]:
            if invalid:
                ticket.switch_image(2)
                score += 1
            else:
                ticket.switch_image(1)
                score -= 1

    # Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    if scene == 0:
        screen.blit(display_title, (0, 0))
    if scene == 1:
        screen.blit(display_stops, (0, 0))
        if show_ticket:
            screen.blit(ticket.image, ticket.rect)
            screen.blit(display_ticket1, (1550, 80))
            screen.blit(display_ticket2, (1550, 110))
        screen.blit(t.image, t.rect)
    pygame.display.update()

    frame += 1
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
