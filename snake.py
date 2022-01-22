import pygame
import random
import os

pygame.mixer.init()


pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
bg=(100,255,100)

# Creating window
screen_width = 1200
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snakes.By.KG")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    
    exit_game=False
    while not exit_game:
        gameWindow.fill(bg)
        bgimg = pygame.image.load("game2.jpg")
        bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))

    
        # text_screen("Karan Gautam",black,900,530)
        # text_screen("Welcome To Snakes",black,380,200)
        # text_screen("Press Space To Play",black,380,260)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game=True
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    
                    pygame.mixer.music.load("Game.mp3")
                    pygame.mixer.music.play(-1)
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
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 28
    fps = 60
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
        # hiscore=int(hi)

    while not exit_game:
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
            gameWindow.fill(bg)
            bgimg = pygame.image.load("game3.jpg")
            bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))
            # text_screen("Mar Gaya Saanp! Fir Se Khelna hai - Press Enter ", red, 130, 250)
            text_screen("Score  "+str(score), black, 500, 300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        exit_game = True
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
                    if event.key == pygame.K_q:
                        score+=50
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<16 and abs(snake_y - food_y)<16:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                # pygame.mixer.music.load("Beep.mp3")
                # pygame.mixer.music.play()
                if(score>int(hiscore)):
                    hiscore=score

            bgimg = pygame.image.load("game4.png")
            bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))
            # gameWindow.fill(bg)

            text_screen("Score: " + str(score)+"                                                                      Hiscore : "+str(hiscore), red, 5, 5)

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                
                pygame.mixer.music.load("exp.mp3")
                pygame.mixer.music.play()

            if snake_x<=0 or snake_x>=screen_width or snake_y<=0 or snake_y>=screen_height:
                game_over = True
                pygame.mixer.music.load("exp.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

