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

IN_STORE_HEIGHT = (HEIGHT - 50)
IN_STORE_WIDTH = (WIDTH - 50)

STOCK_OPTION_HEIGHT = 60
STOCK_OPTION_WIDTH = (WIDTH - 70)

FONT = pygame.font.SysFont("Arial", 30)

player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
store = pygame.Rect(0, HEIGHT - STORE_HEIGHT,WIDTH,STORE_HEIGHT)
stock_option_1 = pygame.Rect(30, 50, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_2 = pygame.Rect(30, 120, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_3 = pygame.Rect(30, 190, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_4 = pygame.Rect(30, 260, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_5 = pygame.Rect(30, 330, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_6 = pygame.Rect(30, 400, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_7 = pygame.Rect(30, 470, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_8 = pygame.Rect(30, 400, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)

stock_option_1_back = pygame.Rect(29, 49, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_2_back = pygame.Rect(29, 119, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_3_back = pygame.Rect(29, 189, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_4_back = pygame.Rect(29, 259, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_5_back = pygame.Rect(29, 329, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_6_back = pygame.Rect(29, 399, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_7_back = pygame.Rect(29, 469, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_68_back = pygame.Rect(29, 549, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))

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

def draw_menu(store_back, elapsed_time, days, money, cost_a, cost_b, cost_c, cost_d, cost_e, cost_f, stock_option_1, stock_option_2, stock_option_3, stock_option_4, stock_option_5, stock_option_6, stock_option_1_back, stock_option_2_back, stock_option_3_back, stock_option_4_back, stock_option_5_back, stock_option_6_back):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "black", store_back)

    pygame.draw.rect(WIN, "white", stock_option_1_back)
    pygame.draw.rect(WIN, "white", stock_option_2_back)
    pygame.draw.rect(WIN, "white", stock_option_3_back)
    pygame.draw.rect(WIN, "white", stock_option_4_back)
    pygame.draw.rect(WIN, "white", stock_option_5_back)
    pygame.draw.rect(WIN, "white", stock_option_6_back)

    pygame.draw.rect(WIN, "black", stock_option_1)
    pygame.draw.rect(WIN, "black", stock_option_2)
    pygame.draw.rect(WIN, "black", stock_option_3)
    pygame.draw.rect(WIN, "black", stock_option_4)
    pygame.draw.rect(WIN, "black", stock_option_5)
    pygame.draw.rect(WIN, "black", stock_option_6)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    day_text = FONT.render(f"Days: {round(days)}", 1, "white")
    WIN.blit(day_text, (210, 10))
    money_text = FONT.render(f"Money: {round(money)}", 1, "white")
    WIN.blit(money_text, (410, 10))

    stock_text_1 = FONT.render(f"Company A", 1, "white")
    WIN.blit(stock_text_1, (50, 60))
    stock_text_1_cost = FONT.render(f"Cost: {round(cost_a)}", 1, "white")
    WIN.blit(stock_text_1_cost, (300, 60))   

    stock_text_2 = FONT.render(f"Company B", 1, "white")
    WIN.blit(stock_text_2, (50, 130))
    stock_text_2_cost = FONT.render(f"Cost: {round(cost_b)}", 1, "white")
    WIN.blit(stock_text_2_cost, (300, 130))

    stock_text_3 = FONT.render(f"Company C", 1, "white")
    WIN.blit(stock_text_3, (50, 200))
    stock_text_3_cost = FONT.render(f"Cost: {round(cost_c)}", 1, "white")
    WIN.blit(stock_text_3_cost, (300, 200))   

    stock_text_4 = FONT.render(f"Company D", 1, "white")
    WIN.blit(stock_text_4, (50, 270))
    stock_text_4_cost = FONT.render(f"Cost: {round(cost_d)}", 1, "white")
    WIN.blit(stock_text_4_cost, (300, 270))   

    stock_text_5 = FONT.render(f"Company E", 1, "white")
    WIN.blit(stock_text_5, (50, 340))
    stock_text_5_cost = FONT.render(f"Cost: {round(cost_e)}", 1, "white")
    WIN.blit(stock_text_5_cost, (300, 340)) 

    stock_text_6 = FONT.render(f"Company F", 1, "white")
    WIN.blit(stock_text_6, (50, 410))
    stock_text_6_cost = FONT.render(f"Cost: {round(cost_f)}", 1, "white")
    WIN.blit(stock_text_6_cost, (300, 410)) 


    pygame.display.update()

def stock(cost):
    return (float(cost)*(round((random.uniform(0.90,1.15)),2)))

def main(start_time):
    run = True

    cost_a = 100
    cost_b = 500
    cost_c = 1000
    cost_d = 5000
    cost_e = 10000
    cost_f = 50000
    cost_g = 100000
    cost_h = 500000

    own_a = 0
    own_b = 0
    own_c = 0
    own_d = 0
    own_e = 0
    own_f = 0
    own_g = 0
    own_h = 0

    buy = 0

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

    in_store = False

    store_back = pygame.Rect(25, 25, IN_STORE_WIDTH, IN_STORE_HEIGHT)
    

    while run:
        clock.tick(200)
        elapsed_time = time.time() - start_time

        
        if int(elapsed_time)/secs_per_day > (days+1):
            cost_a = stock(cost_a)
            cost_b = stock(cost_b)
            cost_c = stock(cost_c)
            cost_d = stock(cost_d)
            cost_e = stock(cost_e)
            cost_f = stock(cost_f)
            cost_g = stock(cost_g)
            cost_h = stock(cost_h)
        
        if in_store == False:
            proj_count += 5
            if proj_count > proj_increment:
                for _ in range(random.randrange(5,10)):
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

        if int(elapsed_time)/secs_per_day > days:
            days += 1
        
        if buy>0:
            buy -= 1

        keys = pygame.key.get_pressed()

        if in_store == False:
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL

            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
                player.x += PLAYER_VEL

            if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
                player.y -= PLAYER_VEL

            if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT:
                player.y += PLAYER_VEL

            if keys[pygame.K_f] and store.colliderect(player):
                proj_increment = 2000
            
                for proj in projs[:]:
                    projs.remove(proj)
            
                in_store = True
        
        if in_store:
            if keys[pygame.K_ESCAPE]:
                in_store = False
            if keys[pygame.K_1] and money > cost_a and buy==0:
                own_a +=1
                money -= cost_a
                buy += 100
            if keys[pygame.K_2] and money > cost_b and buy==0:
                own_b +=1      
                money -= cost_b
                buy += 100
            if keys[pygame.K_3] and money > cost_c and buy==0:
                own_c +=1      
                money -= cost_c
                buy += 100
            if keys[pygame.K_4] and money > cost_d and buy==0:
                own_d +=1 
                money -= cost_d
                buy += 100
            if keys[pygame.K_5] and money > cost_e and buy==0:
                own_e +=1     
                money -= cost_e
                buy += 100
            if keys[pygame.K_5] and money > cost_f and buy==0:
                own_f +=1
                money -= cost_f
                buy += 100
            if keys[pygame.K_6] and money > cost_g and buy==0:
                own_g +=1     
                money -= cost_g
                buy += 100
            if keys[pygame.K_7] and money > cost_h and buy==0:
                own_h +=1
                money -= cost_h
                buy += 100                
            
            if keys[pygame.K_q] and own_a>0 and buy==0:
                own_a -=1
                money += cost_a
                buy += 100
            if keys[pygame.K_w] and own_b>0 and buy==0:
                own_b -=1      
                money += cost_b
                buy += 100
            if keys[pygame.K_e] and own_c>0 and buy==0:
                own_c -=1      
                money += cost_c
                buy += 100
            if keys[pygame.K_r] and own_d>0 and buy==0:
                own_d -=1 
                money += cost_d
                buy += 100
            if keys[pygame.K_t] and own_e>0 and buy==0:
                own_e -=1     
                money += cost_e
                buy += 100
            if keys[pygame.K_y] and own_f>0 and buy==0:
                own_f -=1
                money += cost_f
                buy += 100
            if keys[pygame.K_u] and own_g>0 and buy==0:
                own_g -=1     
                money += cost_g
                buy += 100
            if keys[pygame.K_i] and own_h>0 and buy==0:
                own_h -=1
                money += cost_h
                buy += 100         

        if in_store:
            draw_menu(store_back, elapsed_time, days, money, cost_a, cost_b, cost_c, cost_d, cost_e, cost_f, stock_option_1, stock_option_2, stock_option_3, stock_option_4, stock_option_5, stock_option_6, stock_option_1_back, stock_option_2_back, stock_option_3_back, stock_option_4_back, stock_option_5_back, stock_option_6_back)    

        if in_store == False:
            draw(player, elapsed_time, projs, store, days, money)
            
    pygame.quit()

def start():
    start_time = time.time()
    main(start_time)

if __name__ == "__main__":
    start()