import pygame
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
prevX = 0
prevY = 0
prevX1 = -1
prevY1 = -1
currentX1 = -1
currentY1 = -1

color = (255, 255, 255)
screen.fill((0, 0, 0))

isMouseDown = False
mode = 0  #0 ручка 1 прямоугольник 2 круг 3 ластик

running = True
while running:
    currentX = prevX
    currentY = prevY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Обработка нажатий мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #ЛКМ
                isMouseDown = True
                currentX1, currentY1 = event.pos
                prevX1, prevY1 = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                isMouseDown = False

        if event.type == pygame.MOUSEMOTION:
            currentX, currentY = event.pos

        #Смена цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_w:
                color = (255, 255, 255)

            #Переключение режимов
            elif event.key == pygame.K_1:
                mode = 1 #Прямоугольник
            elif event.key == pygame.K_2:
                mode = 2 #Круг
            elif event.key == pygame.K_3:
                mode = 3 #Ластик
            elif event.key == pygame.K_0:
                mode = 0 #Перо
            elif event.key == pygame.K_4:
                mode = 4  #Квадрат
            elif event.key == pygame.K_5:
                mode = 5  #Прямоугольный треуг
            elif event.key == pygame.K_6:
                mode = 6  #Равносторонний треуг
            elif event.key == pygame.K_7:
                mode = 7  #Ромб
                
    # Перо (свободное рисование)
    # Логика: соединяет текущую и предыдущую точку линией — даёт плавное рисование
    if isMouseDown and mode == 0:
        pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

    # Прямоугольник
    # Логика: рисуется от точки нажатия до текущей позиции, независимо от направления движения мыши
    if isMouseDown and mode == 1 and prevX1 != -1 and prevY1 != -1:
        screen.fill((0, 0, 0))  # очищаем фон для предпросмотра
        pygame.draw.rect(screen, color,
                         (min(prevX1, currentX), min(prevY1, currentY),
                          abs(currentX - prevX1), abs(currentY - prevY1)), 1)

    #  Круг
    # Логика: центр между точками, радиус — половина расстояния между ними
    if isMouseDown and mode == 2 and prevX1 != -1 and prevY1 != -1:
        screen.fill((0, 0, 0))
        centerX = (prevX1 + currentX) // 2
        centerY = (prevY1 + currentY) // 2
        radius = int(sqrt((currentX - prevX1) ** 2 + (currentY - prevY1) ** 2) // 2)
        pygame.draw.circle(screen, color, (centerX, centerY), radius, 1)

    #  Ластик
    # Логика: рисует толстую чёрную линию (шириной 30) по движению мыши — стирает рисунок
    if isMouseDown and mode == 3:
        pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 30)

    #  Квадрат
    # Логика: вычисляем минимальную сторону по X и Y — рисуем квадрат с равными сторонами
    if isMouseDown and mode == 4:
        screen.fill((0, 0, 0))
        side = min(abs(currentX - prevX1), abs(currentY - prevY1))  # длина стороны квадрата
        pygame.draw.rect(screen, color, (prevX1, prevY1, side, side), 1)

    #  Прямоугольный треугольник
    # Логика: строим треугольник по трём точкам:
    # (начальная), (по X к текущей), (по Y к текущей)
    if isMouseDown and mode == 5:
        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen, color, [
            (prevX1, prevY1),
            (currentX, prevY1),
            (prevX1, currentY)
        ], 1)

    #  Равносторонний треугольник
    # Логика: вычисляем высоту по формуле через сторону: h = (sqrt(3)/2)*a
    # Используем три точки: центр вершины сверху и две нижние
    if isMouseDown and mode == 6:
        screen.fill((0, 0, 0))
        height = int(sqrt(3) / 2 * abs(currentX - prevX1))  # высота по формуле
        pygame.draw.polygon(screen, color, [
            (prevX1, prevY1 + height),  # нижний левый угол
            (prevX1 + (currentX - prevX1) // 2, prevY1),  # верхняя вершина
            (currentX, prevY1 + height)  # нижний правый угол
        ], 1)

    #  Ромб
    # Логика: считаем середину по X и Y, строим 4 точки — верх, правый, низ, левый
    if isMouseDown and mode == 7:
        screen.fill((0, 0, 0))
        midX = (prevX1 + currentX) // 2
        midY = (prevY1 + currentY) // 2
        pygame.draw.polygon(screen, color, [
            (midX, prevY1),      # верхняя точка
            (currentX, midY),    # правая
            (midX, currentY),    # нижняя
            (prevX1, midY)       # левая
        ], 1)

    # Обновляем предыдущие координаты для следующего кадра
    prevX = currentX
    prevY = currentY


    pygame.display.flip()
    clock.tick(45)

pygame.quit()