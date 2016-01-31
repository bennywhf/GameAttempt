import sys,pygame
import socket               # Import socket module
from time import *
from networking import serudpsock
from threading import Thread

##port to send info to server
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object
host = "192.168.1.3" # server ip
port = 6003             # Reserve a port for your service.
##
##port to recieve from server
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object
c.bind(('0',6000))

pygame.init()
screen = pygame.display.set_mode((640,480))
s.sendto("New 192.168.1.26 6000",(host,port))
black = 0,0,0
class controllor(Thread):
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    k = event.key
                    if(k == 273):
                        mess = 'up'
                    elif(k == 274):
                        mess = 'down'
                    elif(k == 275):
                        mess = 'right'
                    elif(k == 276):
                        mess = 'left'
                    s.sendto(mess,(host,port))
                if event.type == pygame.KEYUP:
                    k = event.key
                    if(k == 273):
                        mess = 'up-r'
                    elif(k == 274):
                        mess = 'down-r'
                    elif (k == 275):
                        mess = 'right-r'
                    elif (k == 276):
                        mess = 'left-r'
                    s.sendto(mess,(host,port))

def main():
    ball = pygame.image.load("ball.gif")
    ballrect = ball.get_rect()
    mes = None
    updates = []
    control = controllor().start()
    while True:
        while mes != 'Done':
            mes,addr = c.recvfrom(1024)
            if(mes != 'Done'):
                updates.append(mes)
        mes = None
        try:
            ballrect.x,ballrect.y = int(updates[0].split(' ')[0]),int(updates[0].split(' ')[1])
        except Exception:
            pass
        screen.fill(black)
        screen.blit(ball,ballrect)
        pygame.display.flip()
        updates = []
main()
