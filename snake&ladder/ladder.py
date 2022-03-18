
class Ladder:
    def __init__(self,ladders) -> None:
        self.Ladder = {}
        for snake in ladders :
            self.Ladder[snake["Start"]] = snake["End"]
        

    def getEndPointFromLadder(self, start):
        if start in self.Ladder.keys() :
            return self.Ladder[start]
        return None