__author__ = 'jeffrey creighton & anad patel'
import random


class RPS_AI:
    def __init__(self):
        self.paper_goodess = 0
        self.rock_goodness = 0
        self.scissor_goodness = 0
        self.pre_smart = 10

        def move(self, choice):
            return choice

        def chose(self, pre_smart):
            if (pre_smart > 0):
                choice = random.randint(1, 3)
                if (choice == 1):
                    choose_rock(self)
                elif (choice == 2):
                    choose_paper(self)
                elif (choice == 3):
                    choose_scissors(self)
                pre_smart -= 1
                collect_data(self)
            else:
                if (get_paper_goodness(self) > get_rock_goodness(self) and get_paper_goodness(self) > get_scissor_goodness(self)):
                    choose_paper(self)
                elif (get_rock_goodness(self) > get_paper_goodness(self) and get_rock_goodness(self) > get_scissor_goodness(self)):
                    choose_rock(self)
                else:
                    choose_scissors(self)

            collect_data(self)

        #Param is the opponents last move, assigns to appropriate goodness value
        def collect_data(self, past_move):
            if(past_move == 0):
                self.paper_goodess = get_paper_goodness(self) + 1
            elif(past_move == 1):
                self.scissor_goodness = get_scissor_goodness(self) + 1
            elif(past_move == 2):
                self.rock_goodness = get_rock_goodness(self) + 1

        def get_paper_goodness(self):
            return self.paper_goodess

        def get_rock_goodness(self):
            return self.rock_goodness

        def get_scissor_goodness(self):
            return self.scissor_goodness

        def choose_rock(self):
            self.move(self, 0)

        def choose_paper(self):
            self.move(self, 1)

        def choose_scissors(self):
            self.move(self, 2)