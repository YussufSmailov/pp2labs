import pygame
import random
import time
from color_palette import *

pygame.init()
WIDTH = 600
HEIGHT = 600
font = pygame.font.SysFont("Verdana", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
image_game_over = font.render("NEW LEVEL! +2 TO SPEED", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
CELL = 30
cnt = 0
level_up_shown = False
level = 0
cnt_weigh = 0

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x > 19:
            self.body[0].x = 0
        if self.body[0].x < 0:
            self.body[0].x = 19
        if self.body[0].y < 0:
            self.body[0].y = 19
        if self.body[0].y > 19:
            self.body[0].y = 0

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos()
            return True

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, "green", (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)

class Different_Weigh_Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, "orange", (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)

class DisappearingFood:
    def __init__(self):
        self.pos = Point(9, 9)
        self.visible = True
        self.spawn_time = pygame.time.get_ticks()
        self.appear_interval = 5000  # каждые 5 секунд появляется
        self.visible_duration = 3000  # видима 3 секунды

    def draw(self):
        current_time = pygame.time.get_ticks()
        if self.visible and current_time - self.spawn_time > self.visible_duration:
            self.visible = False
        elif not self.visible and current_time - self.spawn_time > self.appear_interval:
            self.visible = True
            self.generate_random_pos()
            self.spawn_time = current_time
        if self.visible:
            pygame.draw.rect(screen, "blue", (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)

fps = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()
weigh_food = Different_Weigh_Food()
disappear = DisappearingFood()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1

    screen.fill("black")
    draw_grid()
    snake.move()

    # Столкновение с обычной едой
    if snake.check_collision(food):
        cnt += 1
        level_up_shown = False

    # Столкновение с весовой едой
    if snake.check_collision(weigh_food):
        weigh = random.randint(1, 4)
        cnt += weigh

    # Столкновение с исчезающей едой
    if disappear.visible and snake.body[0].x == disappear.pos.x and snake.body[0].y == disappear.pos.y:
        cnt += 2
        disappear.visible = False
        disappear.spawn_time = pygame.time.get_ticks()

    # Повышение уровня
    if cnt != 0 and cnt % 4 == 0 and not level_up_shown:
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        fps += 2
        level_up_shown = True
        level += 1

    # Отображение текста
    image_counter = font.render(f"counter: {cnt}", True, "red")
    image_counter_rect = image_counter.get_rect(center=(450, 20))
    screen.blit(image_counter, image_counter_rect)

    image_new_level = font.render(f"level: {level}", True, 'red')
    image_new_level_rect = image_new_level.get_rect(center=(300, 20))
    screen.blit(image_new_level, image_new_level_rect)

    # Рисуем всё
    snake.draw()
    food.draw()
    weigh_food.draw()
    disappear.draw()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
