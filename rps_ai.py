__author__ = 'jeffrey creighton & anand patel'
import random

#rock 0
#paper 1
#scissors 2


class RPS_AI:
    def __init__(self):
        self.moves = [0,0,0]
        #[rock,paper,scissors]
        #self.paper_goodness = 0
        #self.rock_goodness = 0
        #self.scissor_goodness = 0
        self.pre_smart = 10

        def move(self, choice):
            return choice

        def choose(self, pre_smart):
            if (pre_smart > 0):
                choice = random.randint(0, 2)
                move(self,choice)
                # if (choice == 0):
                #     choose_rock(self)
                # elif (choice == 1):
                #     choose_paper(self)
                # elif (choice == 2):
                #     choose_scissors(self)
                self.pre_smart -= 1
                collect_data(self, choice)
            else:
                choice = (self.moves.index(max(self.moves)))
                move(self, choice)
                collect_data(self, choice)

                # if (get_rock_goodness(self) > get_paper_goodness(self) and get_rock_goodness(self) > get_scissor_goodness(self)):
                #     choose_rock(self)
                #     collect_data(self, 0)
                # elif (get_paper_goodness(self) > get_rock_goodness(self) and get_paper_goodness(self) > get_scissor_goodness(self)):
                #     choose_paper(self)
                #     collect_data(self, 1)
                #
                # else:
                #     choose_scissors(self)
                #     collect_data(self, 2)


        #Param is the opponents last move, assigns to appropriate goodness value
        def collect_data(self, past_move):
            self.moves[past_move] += 1


            # if(past_move == 0):
            #     self.rock_goodness = get_rock_goodness(self) + 1
            # elif(past_move == 1):
            #     self.paper_goodness = get_paper_goodness(self) + 1
            # elif(past_move == 2):
            #     self.scissor_goodness = get_scissor_goodness(self) + 1

        # def get_rock_goodness(self):
        #     return self.moves[0]
        #     #return self.rock_goodness
        # def get_paper_goodness(self):
        #     return self.moves[1]
        #     #return self.paper_goodness
        # def get_scissor_goodness(self):
        #     return self.moves[2]
        #     #return self.scissor_goodness

        # def choose_rock(self):
        #     self.move(self, 0)
        #
        # def choose_paper(self):
        #     self.move(self, 1)
        #
        # def choose_scissors(self):
        #     self.move(self, 2)