import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

BG = pygame.transform.scale(pygame.image.load("bg.webp"),(WIDTH, HEIGHT))

PROJ_WIDTH = 10
PROJ_HEIGHT = 30

PROJ_VEL = 5

PLAYER_HEIGHT = 40
PLAYER_WIDTH = 20

PLAYER_VEL = 2

STORE_HEIGHT = 80
STORE_WIDTH = 400

STOREBACK_HEIGHT = (HEIGHT - 100)
STOREBACK_WIDTH = (WIDTH - 100)

FONT = pygame.font.SysFont("Arial", 30)

def draw(player, elapsed_time, projs, store, days, money):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "gray", store)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    day_text = FONT.render(f"Days: {round(days)}", 1, "white")
    WIN.blit(day_text, (10, 40))
    money_text = FONT.render(f"Money: {round(money)}", 1, "white")
    WIN.blit(money_text, (10, 70))



    pygame.draw.rect(WIN, "red", player)

    for proj in projs:
        pygame.draw.rect(WIN, "white", proj)

    
    pygame.display.update()

def draw_menu(storeBack):
    WIN.blit(BG, (0, 0))

    # time_text = FONT.render("", 1, "white")
    # WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "gray", storeBack)

    pygame.display.update()

def stock(elapsed_time, days, secs_per_day):
    if int(elapsed_time)/secs_per_day > days:
        return random.randint(0.90,1.15)

def main(start_time):
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    #store = pygame.Rect(0, STORE_HEIGHT, STORE_HEIGHT, STORE_WIDTH)
    store = pygame.Rect(0, HEIGHT - STORE_HEIGHT,WIDTH,STORE_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    days = 0
    secs_per_day = 20

    money = 1000

    proj_increment = 2000
    proj_count = 0

    projs = []
    hit = False

    storeBack = pygame.Rect(50, 50, STOREBACK_HEIGHT, STOREBACK_WIDTH)

    while run:
        clock.tick(200)
        elapsed_time = time.time() - start_time
        
        if instore =
        proj_count += 5
        if proj_count > proj_increment:
            for _ in range(random.randrange(5,7)):
                proj_x = random.randint(0, WIDTH - PROJ_WIDTH)
                proj = pygame.Rect(proj_x, -PROJ_HEIGHT, PROJ_WIDTH, PROJ_HEIGHT)
                projs.append(proj)

            proj_increment = max(200, proj_increment - 50)
            proj_count = 0

        for proj in projs[:]:
            proj.y += PROJ_VEL
            if proj.y > HEIGHT:
                projs.remove(proj)
                money += 1
            elif proj.y + proj.height >= player.y and proj.colliderect(player):
                projs.remove(proj)
                hit = True
                break

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

        if keys[pygame.K_e] and store.colliderect(player):
            proj_increment = 2000
            
            for proj in projs[:]:
                projs.remove(proj)
            
            instore = True

            while instore:
                draw_menu(store)
                keys = pygame.key.get_pressed()

                if keys[pygame.K_f]:
                    instore = False




        if hit:
            lost_text = FONT.render("You got hit Money - 500", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            money -= 500
            pygame.display.update()
            hit = False
            pygame.time.delay(1000)
            
        if money<0:
            draw(player, elapsed_time, projs, store, days, money)
            lost_text = FONT.render("You went bankrupt", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)
            run = False

        #stock(elapsed_time, days, secs_per_day)

        if int(elapsed_time)/secs_per_day > days:
            days += 1

        draw(player, elapsed_time, projs, store, days, money)

    pygame.quit()

def start():
    start_time = time.time()
    main(start_time)

if __name__ == "__main__":
    start()