import pygame
import random
import time
from color_palette import *

pygame.init()
WIDTH=600
HEIGHT=600
font = pygame.font.SysFont("Verdana", 30)    #загружаю шрифт
screen=pygame.display.set_mode((WIDTH, HEIGHT))

image_new_level = font.render("NEW LEVEL! +2 TO SPEED", True, "black")         
image_new_level_rect= image_new_level.get_rect(center = (WIDTH // 2, HEIGHT // 2))

CELL=30
cnt = 0

level_up_shown = False         # поднимаем или точнее сбрасываем флаг
level=0
image_vse = font.render("Game Over", True, "black")
image_vse_rect = image_vse.get_rect(center = (WIDTH // 2, HEIGHT // 2))


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

    # Метод отрисовки змеи
    def draw(self):
        head = self.body[0]  # голова змеи
        # рисуем голову красным
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:  # остальное тело
            # рисуем тело жёлтым
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    # Метод проверки съедена ли еда
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:  # если координаты головы совпадают с едой
            # добавляем новый сегмент в конец тела (змея растёт)
            self.body.append(Point(head.x, head.y))
            # создаём еду в новом случайном месте
            food.generate_random_pos()
            return True  # еда съедена


class Food:
    def __init__(self):
        self.pos=Point(9,9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    def generate_random_pos(self):
        self.pos.x=random.randint(0, 19)
        self.pos.y=random.randint(0, 19)
fps=5
clock=pygame.time.Clock()
food=Food()
snake=Snake()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:                   #обрабатываем движения
                snake.dx=1
                snake.dy=0
            if event.key==pygame.K_LEFT:
                snake.dx=-1
                snake.dy=0
            if event.key==pygame.K_UP:
                snake.dx=0
                snake.dy=-1
            if event.key==pygame.K_DOWN:
                snake.dx=0
                snake.dy=1
    screen.fill("black")
    draw_grid()
    
    if snake.move()==False:
        time.sleep(1)
        running=False
        screen.fill("red")
        screen.blit(image_vse, image_vse_rect)
        pygame.display.flip()


    if snake.check_collision(food):
        cnt += 1
        level_up_shown = False
        image_counter = font.render(f"{cnt}", True, "red")
        image_counter_rect = image_counter.get_rect(center = (580, 20))
        screen.blit(image_counter, image_counter_rect)


    if cnt != 0 and cnt % 4 == 0 and not level_up_shown:
        screen.fill("red")
        screen.blit(image_new_level, image_new_level_rect)
        pygame.display.flip()
        time.sleep(1)
        fps += 2  
        level_up_shown = True       #меняем флаг на тру и соответснно на строке 123 условие будет выполняться, что нам и надо
        level+=1


    image_counter = font.render(f"counter:{cnt}", True, "red")
    image_counter_rect = image_counter.get_rect(center=(450, 20))
    screen.blit(image_counter, image_counter_rect)

    image_level_cnt=font.render(f"level:{level}", True, 'red')
    image_level_cnt_rect=image_new_level.get_rect(center=(300, 20))
    screen.blit(image_level_cnt, image_level_cnt_rect)

    snake.draw()
    food.draw()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
