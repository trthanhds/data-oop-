import pygame
import random
import math

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pháo Hoa")
'''''
# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Hàm vẽ pháo hoa
def draw_firework(x, y, color):
    num_particles = 100
    for _ in range(num_particles):
        speed = random.uniform(0.5, 3)
        angle = random.uniform(0, 2 * 3.14159)
        dx = speed * math.cos(angle)
        dy = speed * math.sin(angle)
        pygame.draw.circle(screen, color, (int(x), int(y)), 2)
        x += dx
        y += dy

# Hàm main
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = random.choice(COLORS)
        draw_firework(x, y, color)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

'''