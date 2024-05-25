# import threading

import pygame
from player import Player
from client import Client
import json
name = input("Enter a name: ")
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def draw():
    window.fill((75, 150, 75))
    p.draw(window)
    c.send_data(p.get_data())
    try:
        if c.game_state is not None:
            player_data = json.loads(c.game_state)
            for ip in player_data:
                if ip != "food":
                    player = json.loads(player_data[ip])
                    # print(player)
                    # pygame.draw.circle(window, (player["color"][0], player["color"][1], player["color"][2]), player["pos"], player["food_consumed"])
                    window.blit(pygame.transform.rotate(p.image, player["direction"]), player["pos"])
                    font = pygame.font.Font('freesansbold.ttf', 10)
                    text = font.render(player["name"], True, (player["color"][0], player["color"][1], player["color"][2]))
                    textrect = text.get_rect()
                    textrect.center = (player["pos"])
                    window.blit(text, textrect.center)
                elif ip == "food":
                    foods = json.loads(player_data[ip])
                    for food in foods:
                        pygame.draw.circle(window, (0, 0, 0), food, 5)
    except Exception as e:
        print(e)


c = Client()
p = Player(c.ip, name)
run = True
while run:
    clock.tick(60)
    draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.stop()
            run = False
            pygame.quit()
