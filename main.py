import string
import pygame
import os
import sys
from network import Network
pygame.init()
network = Network("localhost")
# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avatar")
# CONSTANTS
BG = (0, 0, 0)
CHARACTER_SIZE = (150, 150)
VEL = 1  # Sebesség
direction = 'right'
ISJUMP = False
JUMP_COUNT = 10

# Images
# ANG_IMAGE_LOAD = pygame.image.load(os.path.join('Images', 'ang.png'))

ANG_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'ang.png')), CHARACTER_SIZE)
# ANG = pygame.transform.flip(ANG_IMAGE, True, False)  # Elfordítja a képet

KATARA_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'katara.png')), CHARACTER_SIZE)
TOPH_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'toph.png')), CHARACTER_SIZE)
ZUKO_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'zuko.png')), CHARACTER_SIZE)


# def

def draw(player1):
    WIN.fill(BG)
    # WIN.blit(ANG_IMAGE_LOAD, (red.x, red.y))
    if direction == "left":
        WIN.blit(ANG, (player1.x, player1.y))
    else:
        WIN.blit(ANG_IMAGE, (player1.x, player1.y))

    # WIN.blit(ANG, (600, 335)) # Jobb oldali képet rakja f
    pygame.display.update()  # Updates the screen


def player1_handle_movement(keys_pressed, player1):
    global direction

    global ISJUMP
    global JUMP_COUNT
    if keys_pressed[pygame.K_a] and player1.x - VEL > 0:  # LEFT
        player1.x -= VEL
        direction = 'left'
    if keys_pressed[pygame.K_d] and player1.x + VEL + player1.width < WIDTH:  # RIGHT
        player1.x += VEL
        direction = 'right'
    if keys_pressed[pygame.K_w] and player1.y - VEL < 400:  # UP
        player1.y -= VEL
    if keys_pressed[pygame.K_s] and player1.y + VEL + player1.height < HEIGHT - 15:  # DOWN
        player1.y += VEL

    #
    # if not (ISJUMP):
    #
    #
    #     if keys_pressed[pygame.K_SPACE]:
    #         ISJUMP = True
    # else:
    #     if JUMP_COUNT >= -10:
    #         ang.y -= (JUMP_COUNT * 0.1)
    #         JUMP_COUNT -= 1
    #     else:
    #         JUMP_COUNT= 10
    #         ISJUMP = False


def main():
    player1 = pygame.Rect(0, 335, CHARACTER_SIZE[0], CHARACTER_SIZE[1])
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        player1_handle_movement(keys_pressed, player1)

        draw(player1)


def Button(surf, coord, mouse):
    if coord[0]+surf.get_rect()[2] > mouse[0] > coord[0] and coord[1]+surf.get_rect()[3] > mouse[1] > coord[1]:
        return True
    else:
        return False
        
def character(selected_character):
    if selected_character == "KATARA":
        return KATARA_IMAGE
    elif selected_character == "TOPH":
        return TOPH_IMAGE
    elif selected_character == "ANG":
        return ANG_IMAGE        
    elif selected_character == "ZUKO":
        return ZUKO_IMAGE

def menu3(run, name, selected_character):
    
    while run:
        print(network.send(name))
        mouse_pos = pygame.mouse.get_pos()
        WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join('Images', 'menubg3.png')), (WIDTH, HEIGHT)),(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()   
                if event.key == pygame.K_f:
                    print(mouse_pos)
             
        pygame.display.update()

def menu2(run, name):
    # run = True
    if name == "":
        name = "TESTNAME"
    font = pygame.font.SysFont("Arial", 29)
    NAME = font.render(name, True, (240, 222, 198))
    
    while run:
        # print(network.send(name))
        mouse_pos = pygame.mouse.get_pos()
        WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join('Images', 'menubg2.jpg')), (WIDTH, HEIGHT)),(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()   
                if event.key == pygame.K_f:
                    print(mouse_pos)
            
        if Button(KATARA_IMAGE, ((CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2) , 0), mouse_pos): 
            WIN.blit(KATARA_IMAGE,((CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2) , 10))
            if pygame.mouse.get_pressed()[0] == True:
                menu3(True, name, "KATARA")
        else:
            WIN.blit(KATARA_IMAGE,((CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2) , 0))

        if Button(TOPH_IMAGE, ((WIDTH-CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2),0), mouse_pos):
            WIN.blit(TOPH_IMAGE,((WIDTH-CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2), 10 ))
            if pygame.mouse.get_pressed()[0] == True:
                menu3(True, name, "TOPH")
        else:
            WIN.blit(TOPH_IMAGE,((WIDTH-CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2), 0 ))
        
        if Button(ANG_IMAGE, ((CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2), HEIGHT-CHARACTER_SIZE[0]), mouse_pos):
            WIN.blit(ANG_IMAGE,((CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2), HEIGHT-CHARACTER_SIZE[0]-10))
            if pygame.mouse.get_pressed()[0] == True:
                menu3(True, name, "ANG")
        else:
            WIN.blit(ANG_IMAGE,((CHARACTER_SIZE[0]) - (CHARACTER_SIZE[0]//2), HEIGHT-CHARACTER_SIZE[0]))
        
        if Button(ZUKO_IMAGE, (WIDTH-CHARACTER_SIZE[0] - CHARACTER_SIZE[0]//2, HEIGHT-CHARACTER_SIZE[0]), mouse_pos):
            WIN.blit(ZUKO_IMAGE,(WIDTH-CHARACTER_SIZE[0] - CHARACTER_SIZE[0]//2, HEIGHT-CHARACTER_SIZE[0]-10))
            if pygame.mouse.get_pressed()[0] == True:
                menu3(True, name, "ZUKO")
        else:
            WIN.blit(ZUKO_IMAGE,(WIDTH-CHARACTER_SIZE[0] - CHARACTER_SIZE[0]//2, HEIGHT-CHARACTER_SIZE[0]))
        
        WIN.blit(NAME, (WIDTH//2-NAME.get_rect()[2]//2, 120))
        pygame.display.update()

def box():
    temp_surface = pygame.Surface((230,55))
    temp_surface.fill((0,0,0))
    pygame.draw.rect(temp_surface, (252,229,195) ,(5, 5, 230-10 ,55-10))
    return temp_surface
   
def menu1():
    run = True
    
    global name
    name = "" # a karakter neve
    possible_letter = string.ascii_lowercase # behúzzuk a betűket a könyvtárból
    font = pygame.font.SysFont("Arial", 29) # font object # milyen stílusban íródjanak a szövegek
    font.set_bold(True)
    NAME = font.render(name, True, (165, 184, 216)) # font surface 
    exit_game = font.render("Exit Game", True, (0,0,0)) # font surface, exit game szövege
    play_game = font.render("Play", True, (0,0,0)) # font surface, play szövege
    BACKGROUNND = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'background.jpg')), (WIDTH, HEIGHT))
    BUTTON1_COLOR, BUTTON2_COLOR = (165, 184, 216), (165, 184, 216)
    NAME_BOX = box()
    while run:
        # print(network.send("hello"))
        WIN.blit(BACKGROUNND, (0,0))
        mouse_pos = pygame.mouse.get_pos() # ezzel hivatkozunk az egérrel
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    print(mouse_pos)
                key = pygame.key.name(event.key)
                # A név beírása
                if key in possible_letter:
                    name += key
                    if len(name) > 12:
                        name = name[:-1]
                    name = name.upper()
                    NAME = font.render(name, True, (165, 184, 216))
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                    name = name.upper()
                    NAME = font.render(name, True, (165, 184, 216))
        
        WIN.blit(NAME_BOX, (WIDTH//2-NAME_BOX.get_rect()[2]//2,30))

        WIN.blit(NAME, (WIDTH/2-NAME.get_rect()[2]/2, 40)) # Kirajzolja a karakter nevét amit beírunk 
        
        if (WIDTH//2-mouse_pos[0])**2 + ((HEIGHT//2-40)-mouse_pos[1])**2 <= 75**2: #kör egyenlet -> ha kisebb egyenlő csinál valamit
            BUTTON1_COLOR = (106, 138,191) # gomb színe átállsítása ha benne van a körben az egér
            if pygame.mouse.get_pressed()[0] == True:
                name = name.upper()
                menu2(True, name)
        else:
            BUTTON1_COLOR = (165, 184, 216)
            
        if (WIDTH//2-mouse_pos[0])**2 + ((HEIGHT-100)-mouse_pos[1])**2 <= 75**2:
            BUTTON2_COLOR = (106, 138,191) # megváltoztatja a kör színét
            if pygame.mouse.get_pressed()[0] == True: # ha kattint a körön belül, akkor bezárja
                run = False
                pygame.quit()
                sys.exit()
        else:
            BUTTON2_COLOR = (165, 184, 216)
            
            
        pygame.draw.circle(WIN, BUTTON1_COLOR, (WIDTH//2, HEIGHT//2-40), 75) # a két kör rajzolása 
        pygame.draw.circle(WIN, BUTTON2_COLOR, (WIDTH//2, HEIGHT-100), 75)   # -,,-
        WIN.blit(exit_game, ((WIDTH//2)-(exit_game.get_rect()[2]//2),(HEIGHT-100)-16)) # Az exit game szövegét rajzolja ki
        WIN.blit(play_game, ( (WIDTH//2) - (play_game.get_rect()[2]//2)  , (HEIGHT//2-40-(play_game.get_rect()[3]//2)))) # a play szövegét rajzolja ki

        

        # print(name)
        pygame.display.update()


if __name__ == '__main__':
    
    menu1()
