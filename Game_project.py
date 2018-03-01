import pygame
import time
import random


#game name-papaya racers
# display dimension
display_width = 1250
display_height = 700

# car dimension
car_width = 140
car_height = 70


# colors(rgd values)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (53, 115, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
pause = False
score_game = 0

game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()


# game setup
def game_init():
    pygame.init()
    pygame.display.set_caption('Papaya Racers')

    # game_icon = pygame.image.load('carIcon.png')
    # pygame.display.set_icon(game_icon)


# backgroundImg = pygame.image.load ('way.png')

##############---------FUNCTIONS--------------##################

def display(count, x, y, message_format='Dodged: %d'):
    """display the score"""
    # max_dodged = 10
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render(message_format % count, True, black)
    game_display.blit(text, (x, y))


def things(thingX, thingY, thingW, thingH, color):
    """draw random things (car or anything)"""
    pygame.draw.rect(game_display, color, [thingX, thingY, thingW, thingH])

#to create the line
def line(lineX, lineY, lineW, lineH, color):
    """draw way lines """
    pygame.draw.rect(game_display, color, [lineX, lineY, lineW, lineH])


def load_imageCar(x, y, image_name):
    img = pygame.image.load(image_name)
    game_display.blit(img, (x, y))

def load_imageTrees(x, y, image_name):
    img = pygame.image.load(image_name)
    game_display.blit(img, (x, y))


def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):

    largeText = pygame.font.SysFont("comicsansms", 115)
    textSurf, textRect = text_object(text, largeText)
    textRect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(textSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash(x, y):
    car_crash = pygame.image.load('images/carcrash.png')
    game_display.blit(car_crash, ((x - 45), (y - 30)))
    #crash_sound = pygame.mixer.Sound("music/crash.wav")
    #pygame.mixer.Sound.play(crash_sound)
    #pygame.mixer.music.stop()
    largeText = pygame.font.SysFont("comicsansms", 90)
    textSurf, textRect = text_object("You Crashed!", largeText)
    textRect.center = ((display_width / 2), (display_height / 4))
    game_display.blit(textSurf, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 250, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 250, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

#defines all the values needed to work out the button, there's actually not a default button
def button(msg, x, y, w, h, ic, ac, action=None):
    """message, dimension, active/inactive color"""

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(mouse)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(game_display, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def game_unpause():
    global pause
    pause = False


def game_pause():
    ############
    pygame.mixer.music.pause()
    #############
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 90)
        textSurf, textRect = text_object("Pause!", largeText)
        textRect.center = ((display_width / 2), (display_height / 4))
        game_display.blit(textSurf, textRect)

        button("Continue !", 150, 250, 100, 50, green, bright_green, game_unpause)
        button("Quit", 550, 250, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    #pygame.mixer.music.load("music/atlanta.wav")
    ## pygame.mixer.music.play(-1)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(white)

        largeText = pygame.font.SysFont("comicsansms", 80)
        textSurf, textRect = text_object("Let's Ride !", largeText)
        textRect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(textSurf, textRect)

        button("GO !", 350, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 800, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    global score_game

    #pygame.mixer.music.load('music/coffee_stains.wav')
    #pygame.mixer.music.play(-1)

    car_x = 0
    car_y = (display_height * 0.65)

    x_change = 0
    y_change = 0
    speed_change = 0

    car_width = 70
    car_height = 140

    enemy_car_Startx = random.randrange(100, 600)
    enemy_car_Starty = 300
    enemy_car_speed = 4
    car_speed=3

    lineX = 400
    lineY = 0
    lineW = 20
    lineH = 450
    line_speed = 10

    tree_y_top = 10
    tree_y_bottom = 650
    tree_w = 600
    tree_speed = 10

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    y_change = -5
                if event.key == pygame.K_RIGHT:
                    y_change = +5
                #pause key, along with all other relevant keys
                if event.key == pygame.K_p:
                    pause = True
                    game_pause()

            #up key pressed does nothing and this is for if the key is up
            if event.type == pygame.KEYUP:
                y_change = 0

        car_y += y_change

        game_display.fill(white)

        line(0, 100, display_width, 20, green)
        line(0,display_height - 100 ,display_width ,20 , green)
#on each iteration the game is drawn again
        load_imageCar(enemy_car_Startx, enemy_car_Starty, 'images/carEnemy.png')
        load_imageCar(car_x,car_y, 'images/carUser.png')
        #x values should be updated and not y values by any +ve values
        load_imageTrees(tree_y_top,30 ,'images/Test_image.jpg')
        load_imageTrees(tree_y_bottom,620, 'images/Test_image.jpg')

        enemy_car_Startx += enemy_car_speed+car_speed
        car_x+=car_speed
        lineX += line_speed
        tree_y_top += tree_speed
        tree_y_bottom += tree_speed

        display(dodged, 5, 25)
        display(car_speed * 60, 5, 50, "Spd: %d px/s")
        display(score_game, 5, 5, "Final Score: %d")

        if car_y > display_height + car_width + 150 or car_y<100:
            # 100 way background image
            crash(car_x, car_y)

        if enemy_car_Startx > display_width:
            enemy_car_Startx = 0 # reset y
            #enemy_car_Startx = random.randrange(170, display_height - car_height - 150)


        if car_x >display_width:
            car_x=0
            dodged += 1  ##refers to number of times the track has been dodged through
            score_game += 1
            car_speed += 1 / 20  # accelarate

        if lineX > display_width:
            lineX = 0 - lineH  # reset y
            car_speed += 1 / 15

        if tree_y_top > display_width:
            tree_y_top = 0 - tree_w  # reset y
            car_speed += 1 / 15

        if tree_y_bottom > display_width:
            tree_y_bottom = 0 - tree_w  # reset y
            car_speed += 1 / 15

        ### check crash
        if car_y < (enemy_car_Starty + car_height) and car_y + car_height >= enemy_car_Starty + car_height:
            if car_x > enemy_car_Startx and car_x < (enemy_car_Startx + car_width) or car_x + car_width > enemy_car_Startx \
                    and car_x + car_width < enemy_car_Startx + car_width:
                crash(car_x, car_y)

        pygame.display.update()
        clock.tick(60)


def main():
    game_init()
    game_intro()
    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
