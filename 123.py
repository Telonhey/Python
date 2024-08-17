import pygame
import random
from sys import exit


class Text:
    def __init__(self, txt, size):
        font = pygame.font.SysFont("", size)
        self.surface = font.render(txt, True, white)
        self.rect = self.surface.get_rect()
        window.blit(self.surface, self.rect)


class Snake:
    def __init__(self, color, head):
        self.color = color
        self.head = head
        self.body = [head]
        self.direction = 'RIGHT'
        self.new_direction = 'RIGHT'
        length = 4
        for i in range(length - 1):
            self.head[0] += unit
            self.body.insert(0, list(self.head))


class Fruit:
    def __init__(self):
        self.pos = [0, 0]
        self.spawn()

    def spawn(self):
        self.pos = [random.randrange(0, window_x, unit),
                    random.randrange(0, window_y, unit)]
        if self.pos in snake.body:
            self.spawn()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
window_x = 720
window_y = 630
window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Pygame貪食蛇")

game_speed = 6
unit = 30

while True:

    score = 0
    snake = Snake(green, [0, 0])
    fruit = Fruit()

    while True:

        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 1000 // game_speed:
            pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    snake.new_direction = 'RIGHT'
                elif event.key == pygame.K_a:
                    snake.new_direction = 'LEFT'
                elif event.key == pygame.K_s:
                    snake.new_direction = 'DOWN'
                elif event.key == pygame.K_w:
                    snake.new_direction = 'UP'

        if snake.new_direction == 'RIGHT' and snake.direction != 'LEFT':
            snake.direction = 'RIGHT'
        elif snake.new_direction == 'LEFT' and snake.direction != 'RIGHT':
            snake.direction = 'LEFT'
        elif snake.new_direction == 'DOWN' and snake.direction != 'UP':
            snake.direction = 'DOWN'
        elif snake.new_direction == 'UP' and snake.direction != 'DOWN':
            snake.direction = 'UP'

        if snake.direction == 'RIGHT':
            snake.head[0] += unit
        elif snake.direction == 'LEFT':
            snake.head[0] -= unit
        elif snake.direction == 'DOWN':
            snake.head[1] += unit
        elif snake.direction == 'UP':
            snake.head[1] -= unit

        snake.body.insert(0, list(snake.head))
        if snake.head == fruit.pos:
            fruit.spawn()
            score += 1
        else:
            snake.body.pop()

        if not (0 <= snake.head[0] < window_x):
            break
        if not(0 <= snake.head[1] < window_y):
            break
        if snake.head in snake.body[1:]:
            break

        window.fill(black)

        for body in snake.body:
            pygame.draw.rect(window, snake.color, (body[0], body[1], unit, unit))
        pygame.draw.rect(window, red, (fruit.pos[0], fruit.pos[1], unit, unit))

        Text(str(score), 60)

        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False