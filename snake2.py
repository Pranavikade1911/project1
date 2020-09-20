import pygame
import random

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background image
bgimg = pygame.image.load("image.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()
agimg = pygame.image.load("s.jpg")
agimg = pygame.transform.scale(agimg, (screen_width,screen_height)).convert_alpha()
cgimg = pygame.image.load("welcome2.jpg")
cgimg = pygame.transform.scale(cgimg, (screen_width,screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("SnakesWithPranav")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text, [x,y])
 

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:   
        pygame.draw.rect(gameWindow, color, [x, y , snake_size, snake_size]) 

#Home Screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(cgimg, (0,0))  
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.load('back.mp3.mp3')
                        pygame.mixer.music.play() 
                        gameloop()
        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    snk_list = []
    snk_length = 1
    
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(agimg, (0,0))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))           
            text_screen("Score: " + str(score), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('end.mp3.mp3')
                pygame.mixer.music.play()
                
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('end.mp3.mp3')
                pygame.mixer.music.play()
                
            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
# welcome()    