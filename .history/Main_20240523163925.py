# Function 1 (draw): This function updates the game screen. It draws the player, projectiles, and store.
# Argument 1: player - A rectangle object representing the player.
# Argument 2: elapsed_time - The elapsed time since the game started.
# Argument 3: projs - An array storing all current projectiles.
# Argument 4: store - A rectangle object representing the store.
# Argument 5: days - The count of days passed in game time.
# Argument 6: money - The current amount of money.
# Return: No return value. Updates the game screen directly.
 

# Function 2 (draw_menu): Description: This function draws the store menu screen when the player enters the store area.
# Argument(s): Objects that define the game state and store options (too many to list individually).
# Return: No return value. Updates the game screen directly.
# 

# Function 3 (stock): Description: This function takes the current cost and returns a new cost which is a random number between 90% and 115% of the current cost.
# Argument 1: cost - current stock value.
# Return: A new cost value.
# 

# Function 4 (main): Description: This function is the main game loop that handles player actions, hit detection and game events like buying and selling stocks.
# Argument 1: start_time - the starting time of the game.
# Return: No return value. Controls the game processes.

# Modules used to create the game are imported
import pygame
import time
import random

# Initializes the pygame font library
pygame.font.init()

# Sets the width and height of the game window
WIDTH, HEIGHT = 1500, 1000

# Sets the dimensions of the game window and assigns it to the variable WIN
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Sets the caption for the game window
pygame.display.set_caption("Game")

# Loads a background image from the directory, resizes it to fit the window, 
# and assigns it to the variable BG
BG = pygame.transform.scale(pygame.image.load("bg.webp"),(WIDTH, HEIGHT))

# Sets the dimensions for game projectiles
PROJ_WIDTH = 10
PROJ_HEIGHT = 30

# Sets the velocity for the in-game projectiles
PROJ_VEL = 5

# Sets the dimensions for the player character
PLAYER_HEIGHT = 40
PLAYER_WIDTH = 20

# Sets the player's velocity
PLAYER_VEL = 2

# Sets the denominator 'equation' that sets the bottom margin - position player from the bottom
STORE_HEIGHT = 80
STORE_WIDTH = 400

# Sets the store's inside dimensions
IN_STORE_HEIGHT = (HEIGHT - 50)
IN_STORE_WIDTH = (WIDTH - 50)

# Sets the dimensions for the stock options in the store
STOCK_OPTION_HEIGHT = 60
STOCK_OPTION_WIDTH = (WIDTH - 70)

# Allotted for adjustment of the position of the stock options
FONT = pygame.font.SysFont("Arial", 30)

# Initializes the player character as a rectangle object with initial position
player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

# Initializes the store as a rectangle object
store = pygame.Rect(0, HEIGHT - STORE_HEIGHT,WIDTH,STORE_HEIGHT)

# Initializes rectangles for the stock options to be displayed in the game store
stock_option_1 = pygame.Rect(30, 50, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_2 = pygame.Rect(30, 120, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_3 = pygame.Rect(30, 190, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_4 = pygame.Rect(30, 260, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_5 = pygame.Rect(30, 330, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_6 = pygame.Rect(30, 400, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_7 = pygame.Rect(30, 470, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)
stock_option_8 = pygame.Rect(30, 550, STOCK_OPTION_WIDTH, STOCK_OPTION_HEIGHT)

# Initializes rectangles that serve as the backgrounds for the stock option rectangles
stock_option_1_back = pygame.Rect(29, 49, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_2_back = pygame.Rect(29, 119, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_3_back = pygame.Rect(29, 189, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_4_back = pygame.Rect(29, 259, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_5_back = pygame.Rect(29, 329, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_6_back = pygame.Rect(29, 399, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_7_back = pygame.Rect(29, 469, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))
stock_option_8_back = pygame.Rect(29, 549, (STOCK_OPTION_WIDTH+2), (STOCK_OPTION_HEIGHT+2))

def draw(player, elapsed_time, projs, store, days, money):

    # Blit the background image onto the screen
    WIN.blit(BG, (0, 0))

    # Draw the store rectangle
    pygame.draw.rect(WIN, "gray", store)

    # Render and display the elapsed time, days, and money texts
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    day_text = FONT.render(f"Days: {round(days)}", 1, "white")
    WIN.blit(day_text, (10, 40))
    money_text = FONT.render(f"Money: {round(money)}", 1, "white")
    WIN.blit(money_text, (10, 70))

    # Draw the player character
    pygame.draw.rect(WIN, "red", player)

    # Draw each of the projectiles
    for proj in projs:
        pygame.draw.rect(WIN, "white", proj)

    # Update the display
    pygame.display.update()

# Define a function called draw_menu that takes a significant number of parameters.
def draw_menu(store_back, elapsed_time, days, money, own_a, own_b, own_c, own_d, own_e, own_f, own_g, own_h, cost_a, cost_b, cost_c, cost_d, cost_e, cost_f, cost_g, cost_h, stock_option_1, stock_option_2, stock_option_3, stock_option_4, stock_option_5, stock_option_6, stock_option_7, stock_option_8, stock_option_1_back, stock_option_2_back, stock_option_3_back, stock_option_4_back, stock_option_5_back, stock_option_6_back, stock_option_7_back, stock_option_8_back):

    # The blit method is used to draw the 'BG' bitmap image to the 'WIN' surface at position (0, 0). 
    WIN.blit(BG, (0, 0))

    # Draw a black rectangle for the 'store_back' object on the 'WIN' surface.
    pygame.draw.rect(WIN, "black", store_back)

    # Draw white rectangles for the stock_option_x_back objects on the 'WIN' surface.
    pygame.draw.rect(WIN, "white", stock_option_1_back)
    pygame.draw.rect(WIN, "white", stock_option_2_back)
    pygame.draw.rect(WIN, "white", stock_option_3_back)
    pygame.draw.rect(WIN, "white", stock_option_4_back)
    pygame.draw.rect(WIN, "white", stock_option_5_back)
    pygame.draw.rect(WIN, "white", stock_option_6_back)
    pygame.draw.rect(WIN, "white", stock_option_7_back)
    pygame.draw.rect(WIN, "white", stock_option_8_back)

    # Draw black rectangles for the stock_option_x objects on the 'WIN' surface.
    pygame.draw.rect(WIN, "black", stock_option_1)
    pygame.draw.rect(WIN, "black", stock_option_2)
    pygame.draw.rect(WIN, "black", stock_option_3)
    pygame.draw.rect(WIN, "black", stock_option_4)
    pygame.draw.rect(WIN, "black", stock_option_5)
    pygame.draw.rect(WIN, "black", stock_option_6)
    pygame.draw.rect(WIN, "black", stock_option_7)
    pygame.draw.rect(WIN, "black", stock_option_8)

    # Create a text surface object, `time_text` with "Time: <rounded elapsed_time>s" using the provided font, anti-aliasing enable parameter, and the text color.
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    # Draw the `time_text` object on the WIN surface at position (10, 10).
    WIN.blit(time_text, (10, 10))

    # Similar to the above, create and draw text surfaces for "Days" and "Money" at the specified locations.
    day_text = FONT.render(f"Days: {round(days)}", 1, "white")
    WIN.blit(day_text, (210, 10))
    money_text = FONT.render(f"Money: {round(money)}", 1, "white")
    WIN.blit(money_text, (410, 10))

    # Create and draw the text surface for "Company A" and it's relevant cost on specified position.
    stock_text_1 = FONT.render(f"Company A", 1, "white")
    WIN.blit(stock_text_1, (50, 60))
    stock_text_1_cost = FONT.render(f"Cost: {cost_a}", 1, "white")
    WIN.blit(stock_text_1_cost, (300, 60))   
        WIN.blit(FONT.render((f"You own:{own_b}"), 1, "white"), (600, 130))


    # The same operations are performed for "Company B" through to "Company H", displaying each one at different positions.   
    stock_text_2 = FONT.render(f"Company B", 1, "white")
    WIN.blit(stock_text_2, (50, 130))
    stock_text_2_cost = FONT.render(f"Cost: {round(cost_b)}", 1, "white")
    WIN.blit(stock_text_2_cost, (300, 130))
    WIN.blit(FONT.render((f"You own:{own_b}"), 1, "white"), (600, 130))

    stock_text_3 = FONT.render(f"Company C", 1, "white")
    WIN.blit(stock_text_3, (50, 200))
    stock_text_3_cost = FONT.render(f"Cost: {round(cost_c)}", 1, "white")    
    WIN.blit(stock_text_3_cost, (300, 200))   
    WIN.blit(FONT.render((f"You own:{own_c}"), 1, "white"), (600, 200))

    stock_text_4 = FONT.render(f"Company D", 1, "white")
    WIN.blit(stock_text_4, (50, 270))
    stock_text_4_cost = FONT.render(f"Cost: {round(cost_d)}", 1, "white")
    WIN.blit(stock_text_4_cost, (300, 270))   
    WIN.blit(FONT.render((f"You own:{own_d}"), 1, "white"), (600, 270))

    stock_text_5 = FONT.render(f"Company E", 1, "white")
    WIN.blit(stock_text_5, (50, 340))
    stock_text_5_cost = FONT.render(f"Cost: {round(cost_e)}", 1, "white")
    WIN.blit(stock_text_5_cost, (300, 340)) 
    WIN.blit(FONT.render((f"You own:{own_e}"), 1, "white"), (600, 340))

    stock_text_6 = FONT.render(f"Company F", 1, "white")
    WIN.blit(stock_text_6, (50, 410))
    stock_text_6_cost = FONT.render(f"Cost: {round(cost_f)}", 1, "white")
    WIN.blit(stock_text_6_cost, (300, 410)) 
    WIN.blit(FONT.render((f"You own:{own_f}"), 1, "white"), (600, 410))

    stock_text_7 = FONT.render(f"Company G", 1, "white")
    WIN.blit(stock_text_7, (50, 480))
    stock_text_7_cost = FONT.render(f"Cost: {round(cost_g)}", 1, "white")
    WIN.blit(stock_text_7_cost, (300, 480)) 
    WIN.blit(FONT.render((f"You own:{own_g}"), 1, "white"), (600, 480))

    stock_text_8 = FONT.render(f"Company H", 1, "white")
    WIN.blit(stock_text_8, (50, 560))
    stock_text_8_cost = FONT.render(f"Cost: {round(cost_h)}", 1, "white")
    WIN.blit(stock_text_8_cost, (300, 560)) 
    WIN.blit(FONT.render((f"You own:{own_h}"), 1, "white"), (600, 560))

    pygame.display.update()

# Function definition: stock(), take in a single argument for the cost and return a random float number times cost and round it to integer. 
def stock(cost):
    return round((float(cost)*(round((random.uniform(0.90,1.15)),2))),0)

# Function definition: main(), take in a single argument for the starting time of a game.
def main(start_time):
    # Initialize variables, related to game state, ownings, costs, projectiles and related parameters, and interaction status.
    # The game is initially running.
    run = True
    # starting cost for each stock
    cost_a = 100
    cost_b = 500
    cost_c = 1000
    cost_d = 5000
    cost_e = 10000
    cost_f = 50000
    cost_g = 100000
    cost_h = 500000
    # initially no stocks are owned
    own_a = 0
    own_b = 0
    own_c = 0
    own_d = 0
    own_e = 0
    own_f = 0
    own_g = 0
    own_h = 0
    # Initially no stock has been bought
    buy = 0
    # Create a pygame clock object and define initial game parameters like elapsed_time, days etc
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    days = 1
    secs_per_day = 5
    # initial money is 1000 units
    money = 1000
    # Initial parameters related to the 'projectile' objects.
    proj_increment = 2000
    proj_count = 0
    projs = []
    hit = False
    # Initially, the player is not inside the store
    in_store = False
    store_back = pygame.Rect(25, 25, IN_STORE_WIDTH, IN_STORE_HEIGHT)

    # While the game is running
    while run:
        # Limit the frame rate to 200 FPS
        clock.tick(200)
        # Calculate the elapsed time since the game started
        elapsed_time = time.time() - start_time
        
        # If a new day has started according to the in-game time scale
        if int(elapsed_time)/secs_per_day > (days):
            # Recalculate the cost for each stock
            cost_a = stock(cost_a)
            cost_b = stock(cost_b)
            cost_c = stock(cost_c)
            cost_d = stock(cost_d)
            cost_e = stock(cost_e)
            cost_f = stock(cost_f)
            cost_g = stock(cost_g)
            cost_h = stock(cost_h)

        # If the player is not in the store
        if in_store == False:
            # Increase the projectile count
            proj_count += 5

            # If it's time to generate new projectiles
            if proj_count > proj_increment:
                # Create multiple new projectiles
                for _ in range(random.randrange(5,10)):
                    proj_x = random.randint(0, WIDTH - PROJ_WIDTH)
                    proj = pygame.Rect(proj_x, -PROJ_HEIGHT, PROJ_WIDTH, PROJ_HEIGHT)
                    # Add them to the list of projectiles
                    projs.append(proj)

                # Lower the increment for next time or set it to 200 if it would go below
                proj_increment = max(200, proj_increment - 50)
                # Reset the projectile count
                proj_count = 0

            # Update the position of each projectile
            for proj in projs[:]:

                # Move the projectile down by its velocity
                proj.y += PROJ_VEL
                # If a projectile has gone off screen
                if proj.y > HEIGHT:
                    # Remove it from the list
                    projs.remove(proj)
                    # The player earns money
                    money += 1
                # If a projectile hits the player
                elif proj.y + proj.height >= player.y and proj.colliderect(player):
                    # Remove it from the list
                    projs.remove(proj)
                    # Mark that a hit happened
                    hit = True
                    # Only the first hit in a frame counts
                    break

        # Handle events
        for event in pygame.event.get():
            # If the player tries to quit
            if event.type==pygame.QUIT:
                # end the game
                run=False
                break

        # If the player was hit in the last frame
        if hit:
            # Create a message to be displayed on the screen
            lost_text = FONT.render("You got hit Money - 500", 1, "white")
            # Blit the message to the window
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            # Deduct 500 from the player's money
            money -= 500
            # Update the display
            pygame.display.update()
            # Reset the hit flag
            hit = False
            # Wait for a second (1000 milliseconds)
            pygame.time.delay(1000)
            
        # If the player has run out of money
        if money<0:
            # Draw the current game state
            draw(player, elapsed_time, projs, store, days, money)
            # Create a message to be displayed on the screen
            lost_text = FONT.render("You went bankrupt", 1, "white")
            # Blit the message to the window
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            # Update the display
            pygame.display.update()
            # Wait for a second
            pygame.time.delay(1000)
            # Stop the game
            run = False
        
        # If the player has more than a million money
        if money>1000000:
            # Draw the current game state
            draw(player, elapsed_time, projs, store, days, money)
            # Create a success message
            win_text = FONT.render("You Won!", 1, "white")
            # Blit the message to the window
            WIN.blit(win_text, (WIDTH/2 - win_text.get_width()/2, HEIGHT/2 - win_text.get_height()/2))
            # Update the display
            pygame.display.update()
            # Wait for a second
            pygame.time.delay(1000)
            # Stop the game
            run = False            

        # If a day has passed
        if int(elapsed_time)/secs_per_day > days:
            # Advance to the next day
            days += 1
        
        # If the player is bound by the buy cooldown
        if buy>0:
            # Decrease the buy cooldown by one
            buy -= 1

        # Get the state of all keyboard buttons
        keys = pygame.key.get_pressed()

        # If the player is not in the store
        if in_store == False:
            # If the left key is pressed and the player's x-position is greater than the player's velocity,
            # reduce the x-position by the velocity to move the player to the left
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL

            # If the right key is pressed and the player's x-position plus their width and velocity does not exceed width of the window,
            # increase the x-position by the velocity to move the player to the right
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
                player.x += PLAYER_VEL

            # If the up key is pressed and the player's y-position is greater than the player's velocity, 
            # reduce the y-position by the velocity to move the player up
            if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
                player.y -= PLAYER_VEL

            # If the down key is pressed and the player's y-position plus their height and velocity does not exceed height of the window, 
            # increase the y-position by the velocity to move the player down
            if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= HEIGHT:
                player.y += PLAYER_VEL

            # If the "f" key is pressed and player's colliderect is intersecting with the store's colliderect,
            # increase the number of projectiles that can be presented in the game field, remove all existing projectiles, and move the player into the store
            if keys[pygame.K_f] and store.colliderect(player):
                proj_increment = 2000
            
                for proj in projs[:]:
                    projs.remove(proj)
            
                in_store = True
        
        # If the player is currently inside the store
        if in_store:
            # If the escape key is pressed, player leaves the store
            if keys[pygame.K_ESCAPE]:
                in_store = False
            
            # If the "1" key is pressed, player has enough money, and the "buy" cooldown is 0
            if keys[pygame.K_1] and money > cost_a and buy==0:
                # Increase the amount of stock "A" the player owns
                own_a +=1
                # Decrease the player's money by the cost of stock "A"
                money -= cost_a
                # Set the "buy" cooldown to 100
                buy += 100

            # The following if-code blocks repeat the above structure for different keys and stocks.
            # The key number corresponds to the stock, e.g., pressing "2" tries to buy stock "B"
            # The player can only buy if they have enough money and the "buy" cooldown is 0
            # If a stock is bought, the amount of that stock increases, the player's money decreases, and the "buy" cooldown is initiated
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
            
            # Similar to the previous blocks, these blocks are for selling stock.
            # If the player owns a particular stock and the buy cooldown is 0, 
            # the respective key press will sell the stock, increasing money and initiating the "buy" cooldown.
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

        # If the player is in the store, draw the store menu with the necessary parameters
        if in_store:
            draw_menu(store_back, elapsed_time, days, money, own_a, own_b, own_c, own_d, own_e, own_f, own_g, own_h, cost_a, cost_b, cost_c, cost_d, cost_e, cost_f, cost_g, cost_h, stock_option_1, stock_option_2, stock_option_3, stock_option_4, stock_option_5, stock_option_6, stock_option_7, stock_option_8, stock_option_1_back, stock_option_2_back, stock_option_3_back, stock_option_4_back, stock_option_5_back, stock_option_6_back, stock_option_7_back, stock_option_8_back)

        # If the player is not in the store, draw the current game state
        if in_store == False:
            draw(player, elapsed_time, projs, store, days, money)
            
    # Exit the game
    pygame.quit()

# Define the function "start" that will begin the main game loop
def start():
    # Record the start time
    start_time = time.time()
    
    # Call the main function with the start time as an argument
    main(start_time)

# Check if this script is being run directly, if so call the "start" function
if __name__ == "__main__":
    start()