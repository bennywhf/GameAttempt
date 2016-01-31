import sys, pygame, time, socket
from ActionQueue import *
from networking import serudpsock
## initial setup
pygame.init()
screen = pygame.display.set_mode((640,480))
game = True
black = 0,0,0
speed = [0,0]
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
foreignsockets = []
todo = ActionQueue()
s = serudpsock('0',6003,todo,foreignsockets).start()
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while game:
    ## check for event. if event is quit then close program.
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           #Quit Game
           game = False
           pygame.quit()

    for i in todo.getall():
        print(i)
        print(str(ballrect.x),str(ballrect.y))
        if(i == 'up'):
            speed[1]-=3
        elif(i == 'down'):
            speed[1]+=3
        elif(i == 'left'):
            speed[0] -=3
        elif(i == 'right'):
            speed[0] +=3
        elif(i == 'up-r'):
            speed[1]+=3
        elif(i == 'down-r'):
            speed[1]-=3
        elif(i == 'left-r'):
            speed[0]+=3
        elif(i == 'right-r'):
            speed[0]-=3
    ## other game logic.
    if speed[1] == -2 : speed[1] = -1
    if speed[1] == 2 : speed[1] = 1
    if speed[0] == 2 : speed[0] = 1
    if speed[0] == -2 : speed[0] = -1
    #moving object
    ballrect = ballrect.move(speed)
    screen.fill(black)
    ###################
    #draw objects here.
    screen.blit(ball, ballrect)
    for i in foreignsockets:
        c.sendto(str(ballrect.x)+' '+str(ballrect.y), i)
    for i in foreignsockets:
        c.sendto('Done',i)
    pygame.display.flip()
    time.sleep(1/60.0)
