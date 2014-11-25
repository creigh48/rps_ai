__author__ = 'jeffrey creighton & anand patel'
import random

#rock 0
#paper 1
#scissors 2


class RPS_AI:
    def __init__(self):
        self.moves = [0,0,0]
        self.pre_smart = 10

        def move(self, choice):
            return choice

        def choose(self, pre_smart):
            if (pre_smart > 0):
                choice = random.randint(0, 2)
                move(self,choice)
                self.pre_smart -= 1
                collect_data(self, choice)
            else:
                choice = (self.moves.index(max(self.moves)))
                move(self, choice)
                collect_data(self, choice)

        #Param is the opponents last move, assigns to appropriate goodness value
        def collect_data(self, past_move):
            self.moves[past_move] += 1
