# import threading

import pygame
from player import Player
from client import Client
import json

window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def draw():
    window.fill((75, 150, 75))
    p.draw(window)
    c.send_data(p.get_data())
    try:
        if c.game_state != None:
            player_data = json.loads(c.game_state)
            for ip in player_data:
                player = json.loads(player_data[ip])
                print(player)
                pygame.draw.circle(window, (player["color"][0], player["color"][1], player["color"][2]), player["pos"], player["food_consumed"])
    except Exception as e:
        print(e)

name = input("Enter your name: ")
c = Client()
p = Player(c.ip, name)
run = True
while run:
    clock.tick(100)
    draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.stop()
            run = False
            pygame.quit()
