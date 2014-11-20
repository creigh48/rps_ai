__author__ = 'jeffrey creighton & anand patel'
import random
import Player.py

class JCAPPlayer(Player.Player):
    def __init__(self):
        self.name = None
        self.moves =[0,0,0]
        self.pre_smart = 3
        self.decrementing = 25

        # Decide to make a smart or random move and
        # return  the final decision
        def choose(self):
            if self.pre_smart > 0:
                choice = explore()
                self.pre_smart =- 1
            else:
                if random.randint(1, 100) < self.decrementing:
                    choice = explore()
                else:
                    choice = exploit()
                if self.decrementing > 5:
                    self.decrementing =- 1
            return choice

        # Make a random move
        def explore():
            return random.randint(0,2)

        # Make an educated guess
        def exploit():
            if self.moves[0] == self.moves[1] and self.moves[0] == self.moves[2]:
                return explore()
            else:
                return self.moves.index(max(self.moves))

        # Return instance variable 'name'
        def get_name(self):
            return self.name

        # Set instance variable 'name'
        def set_name(self, playername):
            self.name = playername

        # Get messages of previous moves or alert of new game
        def notify(self, message):
            if message[0] == Message.MatchStart:
                self.moves = [0,0,0]
                self.pre_smart = 3
                self.decrementing = 25
            elif message[0] == Message.GameEnd:
                if message[1] == get_name(self):
                    self.moves[int(message[4])] =+ 1
                elif message[2] == get_name(self):
                    self.moves[int(message[3])] =+ 1
            else:
                pass

        # Returns either 0, 1, or 2
        def play(self):
            return choose(self)
