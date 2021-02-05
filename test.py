import pygame
import os

pygame.init()

# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# CONSTANTS
BG = (0, 0, 0)
AANG_WIDTH, AANG_HEIGHT = 150, 150
VEL = 1  # Sebesség
direction = 'right'

VEL_Y = 1
jump = False

# Images
# ANG_IMAGE_LOAD = pygame.image.load(os.path.join('Images', 'ang.png'))

ANG_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'ang.png')), (AANG_WIDTH, AANG_HEIGHT))
ANG = pygame.transform.flip(ANG_IMAGE, True, False)  # Elfordítja a képet


def draw(ang):
    WIN.fill(BG)
    # WIN.blit(ANG_IMAGE_LOAD, (red.x, red.y))
    if direction == "left":
        WIN.blit(ANG, (ang.x, ang.y))
    else:
        WIN.blit(ANG_IMAGE, (ang.x, ang.y))

    # WIN.blit(ANG, (600, 335)) # Jobb oldali képet rakja fel

    pygame.display.update()  # Updates the screen


def ang_handle_movement(keys_pressed, ang):
    global direction
    global jump
    global VEL_Y
    if keys_pressed[pygame.K_a] and ang.x - VEL > 0:  # LEFT
        ang.x -= VEL
        direction = 'left'
    if keys_pressed[pygame.K_d] and ang.x + VEL + ang.width < WIDTH:  # RIGHT
        ang.x += VEL
        direction = 'right'
    if keys_pressed[pygame.K_w] and ang.y - VEL < 400:  # UP
        ang.y -= VEL
    if keys_pressed[pygame.K_s] and ang.y + VEL + ang.height < HEIGHT - 15:  # DOWN
        ang.y += VEL



def main():
    ang = pygame.Rect(0, 335, AANG_WIDTH, AANG_HEIGHT)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        ang_handle_movement(keys_pressed, ang)

        draw(ang)


if __name__ == '__main__':
    main()
