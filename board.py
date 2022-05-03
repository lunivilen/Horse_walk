import pygame
from horse_alg import Horse


def board(field_size, place_horse, timer):
    position = Horse(field_size, place_horse).get_result()
    for p in range(len(position)):
        position[p] -= 1
    bg_color = (0, 0, 0)
    g = 0
    mas = []

    pygame.init()
    resolution = pygame.display.Info().current_h*0.8
    b = pygame.display.Info().current_h*0.8
    size = resolution / field_size
    screen = pygame.display.set_mode((resolution, resolution))
    pygame.display.set_caption("Chess")
    horse = pygame.image.load("hourse.png")
    horse = pygame.transform.scale(horse, (round(size) * 0.99, round(size) * 0.99))

    while True:
        y = 0
        u = 0
        if g == 0:
            screen.fill(bg_color)
            for i in range(field_size):
                x = 0
                if field_size % 2 == 0:
                    u += 1
                for j in range(field_size):
                    if u % 2 == 0:
                        pygame.draw.rect(screen, (255, 255, 255), (x, y, round(size), round(size)))
                    mas.append([x, y])
                    u += 1
                    x += size
                y += size

        if g == len(mas):
            pygame.time.delay(2000)
            pygame.display.quit()
            break
        else:
            pygame.draw.rect(screen, (0, 0, 0), (mas[position[g]][0], mas[position[g]][1], round(size), round(size)))
            pygame.draw.rect(screen, (246, 154, 145),
                             (mas[position[g]][0], mas[position[g]][1], round(size) * 0.99, round(size) * 0.99))
            screen.blit(horse, mas[position[g]])
            pygame.display.update()
            pygame.time.delay(round((timer / (field_size ** 2)) * 1000))
            pygame.draw.rect(screen, (246, 154, 145),
                             (mas[position[g]][0], mas[position[g]][1], round(size) * 0.99, round(size) * 0.99))
            g += 1
        pygame.display.update()
