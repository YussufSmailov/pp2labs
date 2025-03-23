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
           

    # Режим "Перо": рисует плавную непрерывную линию
    #  соединяем предыдущую и текущую точку при каждом движении мыши
    if isMouseDown and mode == 0:
        pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

    # Режим "Прямоугольник": рисует прямоугольник от начальной до текущей точки мыши
    # Логика:
    # - prevX1, prevY1 — координаты, где пользователь нажал мышку
    # - currentX, currentY — текущая позиция мыши
    # - min(...), abs(...) — чтобы прямоугольник корректно рисовался в любом направлении (влево/вверх)
    # Каждый кадр очищаем экран, чтобы показать только актуальный прямоугольник (предпросмотр)
    if isMouseDown and mode == 1 and prevX1 != -1 and prevY1 != -1:
        screen.fill((0, 0, 0))  # временно очищаем для визуального эффекта
        pygame.draw.rect(screen, color,
                        (min(prevX1, currentX), min(prevY1, currentY),
                        abs(currentX - prevX1), abs(currentY - prevY1)),
                        1)  # 1 — только контур прямоугольника

    # Режим "Круг": рисует окружность, основанную на расстоянии между точками
    # Логика:
    # - Центр круга — середина между начальной и текущей точками
    # - Радиус = половина расстояния между ними (по формуле Пифагора)
    # - sqrt(...) — находим длину диагонали, делим на 2
    # Как и с прямоугольником, каждый кадр — новый "предпросмотр"
    if isMouseDown and mode == 2 and prevX1 != -1 and prevY1 != -1:
        screen.fill((0, 0, 0))  # очищаем экран перед отрисовкой круга
        centerX = (prevX1 + currentX) // 2
        centerY = (prevY1 + currentY) // 2
        radius = int(sqrt((currentX - prevX1) ** 2 + (currentY - prevY1) ** 2) // 2)
        pygame.draw.circle(screen, color, (centerX, centerY), radius, 1)  # 1 — только контур круга

    # Режим "Ластик": работает как большое перо чёрного цвета
    # Логика:
    # - То же рисование линий, как в режиме "Перо"
    # - Но цвет — чёрный (фон), и толщина больше — 30 пикселей
    # Позволяет стирать нарисованные элементы, как резинка
    if isMouseDown and mode == 3:
        pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 30)

    prevX = currentX
    prevY = currentY

    pygame.display.flip()
    clock.tick(45)

pygame.quit()