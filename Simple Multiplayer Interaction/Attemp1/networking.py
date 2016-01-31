import socket# Import socket module
from threading import Thread
import sys

class sersock(Thread):
   def __init__(self,host,port):
      self.sock = socket.socket()
      self.sock.bind((host,port))
      self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.sock.listen(5)
      Thread.__init__(self)
   def run(self):
      while True:
         c, addr = self.sock.accept()     # Establish connection with client.
         print 'Got connection from', addr
         c.send('Thank you for connecting')
         c.close()# Close the connection
         break
      sys.exit(0)
      return


class serudpsock(Thread):
   def __init__(self,host,port,AQ,userports):
      self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
      self.sock.bind((host,port))
      self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.AQ = AQ
      self.fosocks = userports
      Thread.__init__(self)
      
   def run(self):
      while True:
         data,addr = self.sock.recvfrom(1024)
         if data.split(' ')[0] == 'New':
            self.fosocks.append((data.split(' ')[1],int(data.split(' ')[2])))
         else:
            self.AQ.addAction(data)
      sys.exit(0)
      return

