__author__ = 'anand & jeff'
import JCAPPlayer
import Message

#Allows for the testing of an RPS AI by playing against the user

#begins the game
def play():
    player = JCAPPlayer.JCAPPlayer()
    round(player)

#starts the round with the plater given
def round(player):
    player.notify(Message.Message.get_match_start_message((player,None)))
    start(player)

    i = 2
    while(1 != 0 or i!= 1 or i != 2 or i != 25):
        i = ask()
        if i == 25:
            print("new game")
            new_match(player)
            #player.reset()
            print(player.moves)
            round(player)
        play = player.play()
        print("you chose:", translate(i))
        print("i chose:", translate(play))
        end_round(player,play,i,2)
        print(player.moves)
        print("\n")

#notifies the player of the round start
def start(player):
    player.notify(Message.Message.get_round_start_message((player,None)))

#notifies the player of the round end
def end_round(player,move,move_opp,win):
    player.notify(Message.Message.get_round_end_message((player,None),(move,move_opp),win))

#creates a new match with the given player
def new_match(player):
    player.notify(Message.Message.get_match_end_message((player,None),(2,4)))

#prompts the player for their move
#if invalid asks the player to enter a new number in the valid range.
def ask():
    i = input("Press 0 1 or 2 then enter: ")
    if(int(i) == 25):
        return int(i)
    if(int(i) > 2):
        print("enter a valid number: ")
        return ask()
    return int(i)

#takes in an integer and returns the correct move as a string
def translate(x):
    if x == 0:
        return "rock"
    elif x == 1:
        return "paper"
    elif x == 2:
        return "scissors"

play()