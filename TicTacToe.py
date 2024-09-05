import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((800, 800))
""", pygame.RESIZABLE"""
screen.fill(white)
clock = pygame.time.Clock()
running = True
gameOver = False
fps = 60

def circle(screen, color, x, y, z) :
    pygame.draw.circle(screen, color, [x, y], z, 5)
def cross(screen, color, x, y, z) :
    pygame.draw.line(screen, color, (x-z/2,y-z/2), (x+z/2,y+z/2), 5)
    pygame.draw.line(screen, color, (x+z/2,y-z/2), (x-z/2,y+z/2), 5)

def textscreen(text, color, x, y, z) :
    font = pygame.font.SysFont(None, z)
    screentext = font.render(text, True, color)
    screen.blit(screentext, [x, y])
x = 1
l = [0,0,0,0,0,0,0,0,0]
score1 = 0
score2 = 0
tie = 0
while running:
    if gameOver :
        screen.fill(white)
        textscreen("GAME OVER", red, 200, 300, 100)
        if x == 0 : 
            textscreen("Player 1 won", red, 200, 400, 100)
            #score1 += 1
        elif x == 1 :
            textscreen("Player 2 won", red, 200, 400, 100)
            #score2 += 1 
        else :
            textscreen("Tie", red, 350, 400, 100)
            #tie += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameOver = False
                    count = 0
                    x = 1
                    for i in range (0,9) :
                       l[i] = 0
                    screen.fill(white)
        clock.tick(fps)
        pygame.display.update()
    else :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if 100 < pygame.mouse.get_pos()[0] < 300 and 100 < pygame.mouse.get_pos()[1] < 300 and l[0] == 0 :
                    if x == 0 :
                        circle(screen, blue, 200, 200, 75)
                        x=1
                        l[0] = -1
                    else :
                        cross(screen, red, 200, 200, 150)
                        x=0
                        l[0] = 1
                if 300 < pygame.mouse.get_pos()[0] < 500 and 100 < pygame.mouse.get_pos()[1] < 300 and l[1] == 0 :
                    if x == 0 :
                        circle(screen, blue, 400, 200, 75)
                        x=1
                        l[1] = -1
                    else :
                        cross(screen, red, 400, 200, 150)
                        x=0
                        l[1] = 1
                if 500 < pygame.mouse.get_pos()[0] < 700 and 100 < pygame.mouse.get_pos()[1] < 300 and l[2] == 0 :
                    if x == 0 :
                        circle(screen, blue, 600, 200, 75)
                        x=1 
                        l[2] = -1
                    else : 
                        cross(screen, red, 600, 200, 150)
                        x=0
                        l[2] = 1
                if 100 < pygame.mouse.get_pos()[0] < 300 and 300 < pygame.mouse.get_pos()[1] < 500 and l[3] == 0 :
                    if x == 0 :
                        circle(screen, blue, 200, 400, 75)
                        x=1
                        l[3] = -1
                    else :
                        cross(screen, red, 200, 400, 150)
                        x=0
                        l[3] = 1
                if 300 < pygame.mouse.get_pos()[0] < 500 and 300 < pygame.mouse.get_pos()[1] < 500 and l[4] == 0 :
                    if x == 0 :
                        circle(screen, blue, 400, 400, 75)
                        x=1
                        l[4] = -1
                    else :
                        cross(screen, red, 400, 400, 150)
                        x=0
                        l[4] = 1
                if 500 < pygame.mouse.get_pos()[0] < 700 and 300 < pygame.mouse.get_pos()[1] < 500 and l[5] == 0 :
                    if x == 0 :
                        circle(screen, blue, 600, 400, 75)
                        x=1
                        l[5] = -1
                    else :
                        cross(screen, red, 600, 400, 150)
                        x=0
                        l[5] = 1
                if 100 < pygame.mouse.get_pos()[0] < 300 and 500 < pygame.mouse.get_pos()[1] < 700 and l[6] == 0 :
                    if x == 0 :
                        circle(screen, blue, 200, 600, 75)
                        x=1
                        l[6] = -1
                    else :
                        cross(screen, red, 200, 600, 150)
                        x=0
                        l[6] = 1
                if 300 < pygame.mouse.get_pos()[0] < 500 and 500 < pygame.mouse.get_pos()[1] < 700 and l[7] == 0 :
                    if x == 0 :
                        circle(screen, blue, 400, 600, 75)
                        x=1
                        l[7] = -1
                    else :
                        cross(screen, red, 400, 600, 150)
                        x=0
                        l[7] = 1
                if 500 < pygame.mouse.get_pos()[0] < 700 and 500 < pygame.mouse.get_pos()[1] < 700 and l[8] == 0 :
                    if x == 0 :
                        circle(screen, blue, 600, 600, 75)
                        x=1
                        l[8] = -1
                    else : 
                        cross(screen, red, 600, 600, 150)
                        x=0
                        l[8] = 1
        if(l[0]+l[1]+l[2] == 3 or l[0]+l[1]+l[2] == -3
        or l[3]+l[4]+l[5] == 3 or l[3]+l[4]+l[5] == -3
        or l[6]+l[7]+l[8] == 3 or l[6]+l[7]+l[8] == -3
        or l[0]+l[3]+l[6] == 3 or l[0]+l[3]+l[6] == -3
        or l[1]+l[4]+l[7] == 3 or l[1]+l[4]+l[7] == -3
        or l[2]+l[5]+l[8] == 3 or l[2]+l[5]+l[8] == -3
        or l[0]+l[4]+l[8] == 3 or l[0]+l[4]+l[8] == -3
        or l[6]+l[4]+l[6] == 3 or l[2]+l[4]+l[6] == -3
        ) :
            if x == 0 :
                score1 += 1
            else :
                score2 += 1
            gameOver = True
        else :
            count = 0
            for i in range (0,9) :
                if l[i] != 0 :
                    count+=1
            if count == 9 :
                x = -1
                tie += 1
                gameOver = True
                
        textscreen("Score of Player 1 : " + str(score1), red, 100, 50, 30)
        textscreen("Score of Player 2 : " + str(score2), blue, 500, 50, 30)
        textscreen("Tie : " + str(tie), black, 370, 50, 30)
        clock.tick(fps)
        pygame.draw.line(screen, black, (100,300), (700,300), 5)
        pygame.draw.line(screen, black, (100,500), (700,500), 5)
        pygame.draw.line(screen, black, (300,100), (300,700), 5)
        pygame.draw.line(screen, black, (500,100), (500,700), 5)
        pygame.display.update()
pygame.quit()