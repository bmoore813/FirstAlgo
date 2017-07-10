"""The goal of the Algo is to generate a tree of all possible moves to a certain depth.
    each position on the tree will have a single heuristic value(+/- inf) which will represent 
    the game state. The Algo will then in turn start from the bottom of the tree, to decide the 
    best move for that player and will side step all 'bad' moves."""

#Stick Game
from sys import maxsize

##==========================
##TREE FACTORY
class Node(object):
    def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value=0):
        self.i_depth = i_depth
        self.i_playerNum = i_playerNum
        self.i_sticksRemaining = i_sticksRemaining
        self.i_value = i_value
        self.children = []
        self.createChildren()

    def createChildren(self):
        if self.i_depth < 0:
            return
        #Create child for each choice
        for i in range(1, 4):
            v = self.i_sticksRemaining - i
            ##################       Flips player and decrements depth by one
            self.children.append(Node(self.i_depth - 1, -self.i_playerNum, v, self.realVal(v)))

    def realVal(self, value):
        if value == 0:
            return maxsize * self.i_playerNum
        elif value < 0:
            return maxsize * -self.i_playerNum
        return 0

#==================================================================
#Algo Engine
def minimax(node, i_depth, i_playerNum):
    if (i_depth == 0) or (abs(node.i_value) == maxsize):
        return node.i_value

    i_bestValue = maxsize * -i_playerNum

    for child in node.children:
        i_val = minimax(child, i_depth - 1, -i_playerNum)
        if abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue):
            i_bestValue = i_val

    return i_bestValue

#===============================================
#Game Runner + Helper methods
def winCheck(i_sticks, i_playerNum):
    if i_sticks <= 0:
        print("*" * 30)
        if i_playerNum > 0:
            if i_sticks == 0:
                print("\t You WIN!")
            else:
                print("\t Too many ! You loose..")
        else:
            if i_sticks == 0:
                print("\t Comp Wins... Try again.")
            else:
                print("\t COMP ERROR!")
        print("*" * 30)
        return 0
    return 1

def getAndValidateInput():
    i_choice = input("\n1, 2 or 3:")
    try:
        i_choice = int(float(i_choice))
        if (i_choice == 1 or i_choice == 2 or i_choice == 3) and i_choice is not None:
            return i_choice 
        else:
            print('\nThe number must be a 1, 2 or 3. Try again.')
            getAndValidateInput()
    except:
        print('\nThat was not even a number fool')
        getAndValidateInput()


if __name__ == '__main__':
    i_stickTotal = 13
    i_depth = 6
    i_curPlayer = 1
    print("INSTRUCTIONS : Pick up one two or three sticks at time.")
    while i_stickTotal > 0:
        print("\n%d sticks remain. How many would you like to pick up ?" % i_stickTotal)
        i_choice = getAndValidateInput()
        i_stickTotal -= i_choice
        if winCheck(i_stickTotal, i_curPlayer):
            i_curPlayer *= -1
            node = Node(i_depth, i_curPlayer, i_stickTotal)
            bestChoice = -100
            i_bestValue = -i_curPlayer * maxsize
            for i in range(len(node.children)):
                n_child = node.children[i]
                i_val = minimax(n_child, i_depth, -i_curPlayer)
                if abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer * maxsize - i_bestValue):
                    i_bestValue = i_val
                    bestChoice = i
            bestChoice += 1
            print("Comp chooses: " + str(bestChoice) + "\tBased on value: " + str(i_bestValue*1e500))
            i_stickTotal -= bestChoice
            winCheck(i_stickTotal, i_curPlayer)
            i_curPlayer *= -1