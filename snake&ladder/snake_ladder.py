import json
from snake import Snake
from ladder import Ladder
from dice import Dice
from player import Player
import os 


class SnakeLadderGame :
    def __init__(self,config_path) -> None:
        f = open(config_path)
 
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        
        snakes = data["Snake"]
        ladders = data["Ladder"]
        dice = data["Dice"]
        players  = data["Player"]

        self.Snake = Snake(snakes=snakes)
        self.Ladder = Ladder(ladders=ladders)
        self.Dice = Dice(dice)
        self.Players = []
        self.Max = 100
        for player in players :
            p = Player(player["Name"])
            self.Players.append(p)
        
    def play_game(self) :
        
        while(len(self.Players) != 1) :
            player = self.Players.pop(0)
            print("Player's turn :" , player.Name)

            current = player.getCurrentPos()
            roll_dice = self.Dice.getDiceNumber()
            new_pos = roll_dice + current
            if  new_pos > self.Max :
                print("Your position : %d , Not allowed dice number : %d" %(current,roll_dice))
                self.Players.append(player)
            elif new_pos == self.Max :
                print("You have played %d dice and your new position : %d" %( roll_dice,check_pos))
                print("Congrats, %s !! You won ", player.Name)
            else:
                check_pos = new_pos
                if self.Snake.getEndPointFromSnakes(check_pos) != None:
                    check_pos = self.Snake.getEndPointFromSnakes(check_pos)
                    print(":-( You have been eaten by Snake. You are at now %d"% check_pos)

                if self.Ladder.getEndPointFromLadder(check_pos) != None:
                    check_pos = self.Ladder.getEndPointFromLadder(check_pos)
                    print(":-) You got ladder hurrey !!. You are at now %d"% check_pos)


                if new_pos == self.Max or check_pos == self.Max:
                    print("You have played %d dice and your new position : %d" %( roll_dice,check_pos))
                    print("Congrats, %s !! You won ", player.Name)
                else:
                    print("You have played %d dice and your new position : %d" %( roll_dice,check_pos))
                    player.setCurrentPost(check_pos)
                    self.Players.append(player)


        print("Game finished !!!")
        print("You looser : %s" % self.Players[0].Name)

game = SnakeLadderGame("gameconfig.json")
game.play_game()           

