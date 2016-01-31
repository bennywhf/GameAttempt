##Action queue
##Author:Benny
##this queue is dedicated to storing actions (keypress) that are
##to be taken by player. at 60 frames persecond, this should look
##like entity acts immediately.

class ActionQueue():
    def __init__(self):
        self.container = list()

    def addAction(self,action):
        self.container.append(action)

    def empty(self):
        return self.container.count == 0

    def getall(self):
        temp = self.container
        self.container = list()
        return temp
    def delall(self):
        self.container = list()
