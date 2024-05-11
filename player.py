import pygame
import json

pygame.init()


class Player:
    def __init__(self, ip, name):
        self.x = 0
        self.y = 0
        self.size = 1
        self.image = pygame.transform.scale(pygame.image.load("a roach.jpg"), (50, 50))
        self.color = [0, 0, 0]
        self.sprite = self.image
        self.name = name
        self.food_consumed = 10
        self.ip = ip

    def draw(self, window):
        self.move()
        window.blit(self.sprite, (self.x, self.y))
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render(self.name, True, self.color)
        textrect = text.get_rect()
        textrect.center = (self.x, self.y)
        window.blit(text, textrect.center)

    def move(self):
        userinput = pygame.key.get_pressed()
        if userinput[pygame.K_d] and self.x < 750:
            self.x += 1
            self.sprite = pygame.transform.rotate(self.image, 320)
        if userinput[pygame.K_a] and self.x > 0:
            self.x -= 1
            self.sprite = pygame.transform.rotate(self.image, 140)
        if userinput[pygame.K_s] and self.y < 550:
            self.y += 1
            if userinput[pygame.K_a]:
                self.sprite = pygame.transform.rotate(self.image, 180)
            elif userinput[pygame.K_d]:
                self.sprite = pygame.transform.rotate(self.image, 280)
            else:
                self.sprite = pygame.transform.rotate(self.image, 230)
        if userinput[pygame.K_w] and self.y > 0:
            self.y -= 1
            if userinput[pygame.K_a]:
                self.sprite = pygame.transform.rotate(self.image, 90)
            elif userinput[pygame.K_d]:
                self.sprite = pygame.transform.rotate(self.image, 0)
            else:
                self.sprite = pygame.transform.rotate(self.image, 50)

    def get_data(self):
        return json.dumps({"ip": self.ip, "name": self.name, "pos": [self.x, self.y], "food_consumed": self.food_consumed, "color": self.color})
