## TO DO IN THIS PROJECT: ##

#1. Creating the food objects
    # Ensuring these show up at random cells in our grid
    # Ensuring these go away once the snake ate them 
    # Ensuring the food reappears once its eaten by snake
#2. Creating our snake 
    # Ensuring the snake grows one cell when it eats the food
    # Ensuring the snake is moving in the right direction one cell at a time once inputed
#3. Creating our end game conditions
    # If the snake touches the border of our grid
    # If the snake touches a cell in its body with its 'head' (the first item in the list)
#4. Displaying the score and the highest score of the player 

#Import  libraries
import pygame, sys, random
from random import randrange
from sys import exit

#Initate  pygame 
pygame.init()

#### Making the building block variables of our 'grid/board' so we can just refer to these in the code
#Global variables. These are referenced multiple times in the game so its easier if these are global.
CELL_SIZE = 30
CELL_NUMBER = 30
CURRENT_SCORE = 0
HIGHEST_SCORE = []

##### Making the classes for food and snake through OOP #########

# Using vectors allows for easier manipulation of the coordinates once we have to make the snake change directions
# We can just change directions by making the (x, y) have values of 0 or 1.

class Food:
    def __init__(self):
        ### Making the food appear at random places in the entire screen everytime the game is launched:
        # Creating the food coordinates here so code in functions is easier to read and we can just call these. / Class attributes
        self.x_coor = random.randrange(1,CELL_NUMBER-1) 
        self.y_coor = random.randrange(1,CELL_NUMBER-1) 
        #Vector 2 represents vectors with x & y coordinates (2), so we use it and not Vector 3 (x,y,z). We are working with 2D values in this game.
        self.overall_coor = pygame.math.Vector2(self.x_coor, self.y_coor) 
    
    def placing_food(self):
        #Creating food rectangle object with (x,y coordintes, width and height we want, which are decided by CELL_SIZE already)
        #Moving the x and y coordinates by the pixels of our cell size our screen
        food_rectangle = pygame.Rect((self.overall_coor.x*CELL_SIZE),
                                     (self.overall_coor.y*CELL_SIZE),
                                     CELL_SIZE, CELL_SIZE)
        # For aesthetic purposes want the food to be a circle, not a rectangle so we call the ellipse in the draw function and not the rectangle.
        pygame.draw.ellipse(screen, "red", food_rectangle)



class Snake:
    def __init__(self):
        self.body = [pygame.math.Vector2(15,15), ##These are our arbitrary starting coordinates for the snake to start in the middle of the screen 
                     pygame.math.Vector2(14,15)]
        self.direction_change = pygame.math.Vector2(1,0) # We use this to manipulate the direction of the snake cells
        

    def placing_snake(self):
        #Creating snake body rectangle objects with (x,y coordintes, width and height we want, which are decided by CELL_SIZE already)
        #Moving the x and y coordinates by the pixels of our cell size our screen, just like we did with the food
        for cell in self.body: #(x,y, width, height)
            #Creating the variables here so its easier to read the code once we make the rectangle
            x_coord = cell.x*CELL_SIZE
            y_coord = cell.y*CELL_SIZE

            #Then we can just call in these variables in the coordinates for the rectangle and draw/place it on the display screen
            cell_rectangle = pygame.Rect(x_coord, y_coord, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, " dark green", cell_rectangle)


    def moving_snake(self):
        # This makes it seem like the snake is moving 
        body_copy = self.body[:-1] # Exclude last cell
        body_copy.insert(0,body_copy[0] + self.direction_change) # We place the new block based on the direction we want
        self.body = body_copy[:] 


    def growing_snake_body(self):
        # Using append to add one item automatically to the body of the snake
        # We specify we want the new appended item to be the same as the already last item of the cell list/body of the snake, so the end of the snake is growing.
        self.body.append(self.body[-1])


    def snake_hits_border(self):
        # Creating variables of what a violation of x and y borders are
        # We specify body[0] because we care about the 'head' crossing these borders
        hit_x_borders = self.body[0].x < 0 or self.body[0].x >= CELL_NUMBER
        hit_y_borders = self.body[0].y < 0 or self.body[0].y >= CELL_NUMBER
        
        # If we ever hit any of these grid borders, the game ends
        if hit_x_borders or hit_y_borders:
            logic.game_over()


    def snake_hits_itself(self):  
        for cell in self.body[1:]: # We check for al lthe cells in the body
            if cell == self.body[0]:   # If any cell in the body ever equals the frist cell (the head), it means theres a collision
                logic.game_over()



class Logistics:
    def __init__(self):
        pass


    def restart_game(self):
        # In this function, we initiate our snake and food classes again, resetting everything back to how it was in the start.
        global snake, food, CURRENT_SCORE
        food = Food()
        snake = Snake()
        CURRENT_SCORE = 0


    def placing_score(self):
        global CURRENT_SCORE, HIGHEST_SCORE
        
        # If the current score is bigger than the maximum value in the highest score list, if appends that value to the Highest Score List
        # This creates a list of all the scores we have accumulated in the game in the different plays without quitting.
        
        if CURRENT_SCORE > max(HIGHEST_SCORE, default=0): #Since we start with an empty list, default 0; the first ever points we make will get appended.
            HIGHEST_SCORE.append(CURRENT_SCORE)

    # Get the current highest score if the list is not empty
        if HIGHEST_SCORE != []:
            highest_score = max(HIGHEST_SCORE) # This is what we display on the screen
        else: 
            highest_score = 0
            
        #### Visualizing the current score as a string on the display screen
        score_x_coord = (CELL_NUMBER-1) * CELL_SIZE
        score_y_coord = 25
        score_string = str(CURRENT_SCORE)
        score_surface = text_font.render(score_string, True, "black")
        score_rect = score_surface.get_rect(center=(score_x_coord, score_y_coord))
        screen.blit(score_surface,score_rect)
        
        score_label_surface = score_surface = text_font.render('Current Score:', True, "black")
        score_label_rect = score_label_surface.get_rect(midright = (score_rect.left, score_rect.centery))
        screen.blit(score_label_surface,score_label_rect)

        #### Visualizing the highest score as a string on the display screen
        High_score_x_coord = (CELL_NUMBER-1) * CELL_SIZE
        High_score_y_coord = 45
        High_score_string = str(highest_score)
        High_score_surface = text_font.render(High_score_string, True, "black")
        High_score_rect = High_score_surface.get_rect(center=(High_score_x_coord, High_score_y_coord))
        screen.blit(High_score_surface,High_score_rect)
        
        High_score_label_surface = High_score_surface = text_font.render('Highest Score:', True, "black")
        High_score_label_rect = High_score_label_surface.get_rect(midright = (High_score_rect.left, High_score_rect.centery))
        screen.blit(High_score_label_surface,High_score_label_rect)


    def game_over(self):
        global CURRENT_SCORE, HIGHEST_SCORE
        
        screen.fill("blue") # If game is over we want the screen display to be blue, not white.
        
        # Setting up the middle of the display screen coordinates to show our message
        game_over_x_coord = (CELL_NUMBER*CELL_SIZE) / 2
        game_over_y_coord = (CELL_NUMBER*CELL_SIZE) / 2


        # General Game Over Message
        game_over_surface = text_font.render("Game Over", True, "White")
        game_over_rect = game_over_surface.get_rect(center=(game_over_x_coord, game_over_y_coord))
        screen.blit(game_over_surface,game_over_rect)

        # Restarting Game Message
        game_overR_surface = text_font.render("Press R to Restart the Game", True, "White")
        game_overR_rect = game_overR_surface.get_rect(midtop=(game_over_x_coord, game_over_y_coord + 40))
        screen.blit(game_overR_surface,game_overR_rect)

        # Quitting the Game Message
        game_overQ_surface = text_font.render("Press Q to Quit the Game", True, "White")
        game_overQ_rect = game_overQ_surface.get_rect(midtop=(game_over_x_coord, game_over_y_coord + 55))
        screen.blit(game_overQ_surface,game_overQ_rect)

        pygame.display.update() 
        # If we dont include this, the game over screen will  never update and show on our display. The game will just be frozen with the snake at the border


        # This while True loop, like our main loop ensures we can take in the players keyboard input without closing the screen.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: # We get these keys for each keyboard input from Pygame online documentation
                        logic.restart_game()
                        return
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
        
 
food = Food()
snake = Snake()
logic = Logistics()
    

#### Display Screen Set Up  ####
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER)) #(x,y) format
pygame.display.set_caption('CS10 Final Project :)') # Extra step of adding a title to the tab of the game


clock = pygame.time.Clock() #Creating the  clock feature so we can edit the frame per second 
text_font = pygame.font.Font('CS10/FinalProject/things/font.ttf', 10) #(font, size) Loading in the specific font we are using through the game, in our case its stored in a computer file


####### Starting the main game Loop ########
#If we dont turn this into a loop, then our display screen will go away right after it appears.

update = pygame.USEREVENT
pygame.time.set_timer(update,100) #This also determines how fast our snake is moving, the lower the number the faster it is. 
#Could be useful if we wanted to increase difficulty of game in later projects.

while True:
    for event in pygame.event.get():

        #Here we put the keyboard inputs
        if event.type == pygame.QUIT:
            pygame.quit() #This is if they just close the game window overall
            exit() #ends the while loop completely
        
        if event.type == update:
            snake.moving_snake()
            snake.snake_hits_border()
            snake.snake_hits_itself()

        #### Setting up player keyboard inputs #####
        #First we check if any keys are pressed
        if event.type == pygame.KEYDOWN:
            
            # We get the code for each direction key input from Pygame Online documentation
            if event.key == pygame.K_UP:   #Up key

                # To make sure we cant just reverse the snake on itself, we make sure you cant call the exact opposite direction of the current direction the snake is going in.
                # For example, if we are moving the snake to the left, changing the x by -1, we have to make sure we are not heading right already 
                    # We do this by only allowing the direction change to happen if our x was not (!=) 1 in the first place (a 1 in x means we are moving right)
                if snake.direction_change.y != 1:
                    snake.direction_change = pygame.math.Vector2(0,-1) # Note that the signs are 'flipped' because we want to decrease our y coordinate in order to move up
                    # In Pygame, the top left corner of our display screen is the (0,0) origin, so to move up we substract -1
            if event.key == pygame.K_DOWN:   #Down key
                if snake.direction_change.y != -1:
                    snake.direction_change = pygame.math.Vector2(0,1)
            if event.key == pygame.K_RIGHT:   #Right key
                if snake.direction_change.x != -1:
                    snake.direction_change = pygame.math.Vector2(1,0) 
            if event.key == pygame.K_LEFT:   #Left key
                if snake.direction_change.x != 1:
                    snake.direction_change = pygame.math.Vector2(-1,0) 

        
            ##### Now we set up the snake growing algorithm inside the game loop #####
            # We check if the first item in the snake body is clashing with the coordinates where the food is at, this means the snake "ate" the food
            
        head = snake.body[0] #Creating our local / non global variable
        if head == food.overall_coor:
                # If they are in the same place in the grid, then we call the grow snake function we made before in the snake class
            snake.growing_snake_body()
            food = Food() #Here we call the food attributes once again and this places the food randomly in the grid again, it initializes the class again.
            CURRENT_SCORE += 5 # Everytime we eat food and grow one cell, we get 5 points added to our score



        screen.fill("white") # This is the background color of our display screen
        # If we dont place this in the while loop then our screen wont update and we will see the snake 'drag' as it moves through a black screen

        food.placing_food()
        snake.placing_snake()
        logic.placing_score()

    clock.tick(60)  #(chosen framerate) 60 is like the average good number for most computers   
    #This makes sure our screen updates with the info we put in the loop
    pygame.display.update()
    
pygame.quit()
