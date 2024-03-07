import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#BG=pygame.transform.scale(pygame.image.load(),(WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("bg.webp"),(WIDTH, HEIGHT))

PROJ_WIDTH = 10
PROJ_HEIGHT = 30

PROJ_VEL = 20

PLAYER_HEIGHT = 40
PLAYER_WIDTH = 40

PLAYER_VEL = 10

FONT = pygame.font.SysFont("Arial", 30)

def draw(player, elapsed_time, projs):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for proj in projs:
        pygame.draw.rect(WIN, "white", proj)

    
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    proj_increment = 2000
    proj_count = 0

    projs = []
    hit = False

    while run:

        proj_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if proj_count > proj_increment:
            for _ in range(5):
                proj_x = random.randint(0, WIDTH - PROJ_WIDTH)
                proj = pygame.Rect(proj_x, -PROJ_HEIGHT, PROJ_WIDTH, PROJ_HEIGHT)
                projs.append(proj)

            proj_increment = max(200, proj_increment - 50)
            proj_count = 0

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL

        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT:
            player.y += PLAYER_VEL

        for proj in projs[:]:
            proj.y += PROJ_VEL
            if proj.y > HEIGHT:
                projs.remove(proj)
            elif proj.y + proj.height >= player.y and proj.colliderect(player):
                projs.remove(proj)
                hit = True
                break

        if hit:
            lost_text = FONT.render("YOU LOST!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        draw(player, elapsed_time, projs)

    pygame.quit()

if __name__ == "__main__":
    main()