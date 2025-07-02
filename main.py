import pygame
import sys

# O'yin oynasi o'lchami
WIDTH, HEIGHT = 800, 600

# RANGLAR
WHITE = (255, 255, 255)
PINK = (255, 85, 165)
BLACK = (0, 0, 0)

# Pygame ni boshlash
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fergo's Mini Pygame Demo 🎮")

# FPS
clock = pygame.time.Clock()
FPS = 60

# Kvadrat o'zgaruvchilar
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# O'yin sikli
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Hodisalar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tugmalarni tekshirish
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Kvadratni chizish
    pygame.draw.rect(screen, PINK, (player_pos[0], player_pos[1], player_size, player_size))

    # Ekranni yangilash
    pygame.display.flip()
