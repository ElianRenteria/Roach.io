import pygame
import json

pygame.init()


class Player:
    def __init__(self, ip, name):
        self.x = 0
        self.y = 0
        self.size = 1
        self.ip = ip
        self.image = pygame.transform.scale(pygame.image.load("a roach.jpg"), (50, 50))
        self.color = [0, 0, 0]
        self.sprite = self.image
        self.name = name
        self.food_consumed = 10
        self.direction = 0

    def draw(self, window):
        self.move()
        # window.blit(self.sprite, (self.x, self.y))

    def move(self):
        userinput = pygame.key.get_pressed()
        if userinput[pygame.K_d] and self.x < 750:
            self.x += int(3 * 0.95 ** self.food_consumed)
            self.sprite = pygame.transform.rotate(self.image, 320)
            self.direction = 320
        if userinput[pygame.K_a] and self.x > 0:
            self.x -= int(3 * 0.95 ** self.food_consumed)
            self.sprite = pygame.transform.rotate(self.image, 140)
            self.direction = 140
        if userinput[pygame.K_s] and self.y < 550:
            self.y += int(3 * 0.95 ** self.food_consumed)
            if userinput[pygame.K_a]:
                self.sprite = pygame.transform.rotate(self.image, 180)
                self.direction = 180
            elif userinput[pygame.K_d]:
                self.sprite = pygame.transform.rotate(self.image, 280)
                self.direction = 280
            else:
                self.sprite = pygame.transform.rotate(self.image, 230)
                self.direction = 230
        if userinput[pygame.K_w] and self.y > 0:
            self.y -= int(3 * 0.95 ** self.food_consumed)
            if userinput[pygame.K_a]:
                self.sprite = pygame.transform.rotate(self.image, 90)
                self.direction = 90
            elif userinput[pygame.K_d]:
                self.sprite = pygame.transform.rotate(self.image, 0)
                self.direction = 0
            else:
                self.sprite = pygame.transform.rotate(self.image, 50)
                self.direction = 50

    def get_data(self):
        return json.dumps({"ip": self.ip, "name": self.name, "pos": [self.x, self.y], "food_consumed": self.food_consumed, "color": self.color, "direction": self.direction})
