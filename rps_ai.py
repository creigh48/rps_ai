__author__ = 'jeffrey creighton & anad patel'
import random

paper_goodess = 0
rock_goodness = 0
scissor_goodness = 0

pre = 10
def chose(pre):
    if(pre > 0):
        choice = random.randint(1, 3)
        if(choice == 1):
            choose_rock()
        elif(choice == 2):
            choose_paper()
        elif(choice == 3):
            choose_scissors()
        pre -= 1
        collect_data()
        return pre

    else:
        if(get_paper_goodness() > get_rock_goodness() and get_paper_goodness() > get_scissor_goodness()):
            choose_paper()
        elif(get_rock_goodness() > get_paper_goodness() and get_rock_goodness() > get_scissor_goodness()):
            choose_rock()
        else:
            choose_scissors()
    collect_data()

def collect_data():
    #retrieve who has won the match and assign a goodness value to combat the opponents previous move



def get_paper_goodness():
    return paper_goodess

def get_rock_goodness():
    return rock_goodness

def get_scissor_goodness():
    return scissor_goodness

def choose_rock():

def choose_paper():

def choose_scissors():