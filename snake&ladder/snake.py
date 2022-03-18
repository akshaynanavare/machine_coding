
class Snake:
    def __init__(self,snakes) -> None:
        self.Snakes = {}
        for snake in snakes :
            self.Snakes[snake["Start"]] = snake["End"]
        

    def getEndPointFromSnakes(self, start):
        if start in self.Snakes.keys() :
            return self.Snakes[start]
        return None