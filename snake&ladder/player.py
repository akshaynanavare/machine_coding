
class Player:
    def __init__(self,name) -> None:
        self.Name = name
        self.Current = 0
    
    def getName(self) :
        return self.Name

    def getCurrentPos(self):
        return self.Current
    
    def setCurrentPost(self,no):
        self.Current = no