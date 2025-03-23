import pygame
import random
import time
from color_palette import *

pygame.init()
WIDTH = 600
HEIGHT = 600
font = pygame.font.SysFont("Verdana", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
image_lvl = font.render("NEW LEVEL! +2 TO SPEED", True, "black")
image_lvl_rect = image_lvl.get_rect(center=(WIDTH // 2, HEIGHT // 2))
CELL = 30
cnt = 0
level_up_shown = False
level = 0
cnt_weigh = 0
image_vse = font.render("Game Over", True, "black")
image_vse_rect = image_vse.get_rect(center = (WIDTH // 2, HEIGHT // 2))
#делим экран на клетки
# Функция для отрисовки обычной сетки
def draw_grid():
    for i in range(HEIGHT//CELL):                      # проходим по строкам
        for j in range(WIDTH//CELL):                   # проходим по столбцам
            # рисуем прямоугольник-сетку с границей в 1 пиксель
            pygame.draw.rect(screen, colorGRAY, (i*CELL, j*CELL, CELL, CELL), 1)

# Функция для отрисовки шахматной сетки
def draw_grid_chess():
    color = [colorWHITE, colorGRAY]                    # два цвета для шахматного узора
    for i in range(HEIGHT // CELL):                    # строки
        for j in range(WIDTH // CELL):                 # столбцы
            # цвет чередуется в зависимости от суммы индексов (чёт/нечёт)
            pygame.draw.rect(screen, color[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки — используется для координат змейки и еды
class Point:
    def __init__(self, x, y):
        self.x = x  # координата по X
        self.y = y  # координата по Y

# Класс змейки
class Snake:
    def __init__(self):
        # тело змеи — список точек (Point), начальное положение
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # направление движения по X (1 = вправо)
        self.dy = 0  # направление по Y (0 = не движется вверх/вниз)

    # Метод движения змеи
    def move(self):
        # перемещаем все сегменты тела: от хвоста к голове
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x  # сегмент принимает координаты предыдущего
            self.body[i].y = self.body[i - 1].y

        # двигаем голову по направлению движения
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # проверка на выход за границы по X
        if self.body[0].x > 19:
            return False  # игра закончится
        if self.body[0].x < 0:
            return False

        # по Y змея "телепортируется" (граница сверху и снизу замыкается)
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
#класс еда
class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, "green", (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)
#класс еда с рандомным весом
class Different_Weigh_Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, "orange", (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)
#класс с исчезающей едой
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
            #проверяем нажатие клавиш
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
    if snake.move()==False:
        time.sleep(1)
        running=False
        screen.fill("red")
        screen.blit(image_vse, image_vse_rect)
        pygame.display.flip()

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
        screen.blit(image_lvl, image_lvl_rect)
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
