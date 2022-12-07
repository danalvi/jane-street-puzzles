import numpy as np
from copy import copy, deepcopy

board = np.array([  [0,77,32,403,337,452],
                    [5,23,-4,592,445,620],
                    [-7,2,357,452,317,395],
                    [186,42,195,704,452,228],
                    [81,123,240,443,353,508],
                    [57,33,132,268,492,732] ])

def move(die, c) :
    new_dice = deepcopy(die) # took me a long time to realise pythons .copy() does not work on multidimensional arrays properly
    if(c == (0, 1)) :
        temp = new_dice[1][0]
        new_dice[1][0] = new_dice[1][1]; new_dice[1][1] = new_dice[1][2]; new_dice[1][2] = new_dice[1][3]; new_dice[1][3] = temp
    if(c == (0, -1)) :
        temp = new_dice[1][3]
        new_dice[1][3] = new_dice[1][2]; new_dice[1][2] = new_dice[1][1]; new_dice[1][1] = new_dice[1][0]; new_dice[1][0] = temp
    if(c == (1,0)) :
        temp = new_dice[1][2]
        new_dice[1][2] = new_dice[2][0]; new_dice[2][0] = new_dice[1][0]; new_dice[1][0] = new_dice[0][0]; new_dice[0][0] = temp
    if(c == (-1,0)) :
        temp = new_dice[1][2]
        new_dice[1][2] = new_dice[0][0]; new_dice[0][0] = new_dice[1][0]; new_dice[1][0] = new_dice[2][0]; new_dice[2][0] = temp
    return new_dice


def get_top(die) :
    return die[1][2]

def set_top(die, val) :
    die[1][2] = val

def neighbours(c) :
    nbrs = []
    if( c[0] < 5 ) : nbrs.append((c[0] + 1, c[1]))
    if( c[1] < 5 ) : nbrs.append((c[0], c[1] + 1))
    if( c[0] > 0 ) : nbrs.append((c[0] - 1, c[1]))
    if( c[1] > 0 ) : nbrs.append((c[0], c[1] - 1))
    return nbrs


def neighbours(c) :
    nbrs = []
    if( c[0] < 5 ) : nbrs.append((c[0] + 1, c[1]))
    if( c[1] < 5 ) : nbrs.append((c[0], c[1] + 1))
    if( c[0] > 0 ) : nbrs.append((c[0] - 1, c[1]))
    if( c[1] > 0 ) : nbrs.append((c[0], c[1] - 1))
    return nbrs

visited = np.array([np.zeros(6) for _ in range(1,7)])
visited[(0,0)] = 1
def search(xs, d, visited) :
    if( board[xs[-1]] == 732 ) :
        sum = 0
        for i in range(6):
            for j in range(6) :
                if (i,j) not in xs :
                    sum += board[(i,j)]
        print(sum)
    nbrs = neighbours(xs[-1])
    for n in nbrs :
        mov = tuple(np.subtract(n, xs[-1]))
        new_dice = move(d, mov)
        x = ( board[n] - board[xs[-1]] ) / len(xs)
        top = get_top(new_dice)
        if top == None  :
            set_top(new_dice, x)
            visited[n] = 1
            #print("Hello1")
            search(xs + [n], new_dice, visited)
        elif top == x : # top is non-zero and satisfies the constraint i.e. there is an available move
            visited[n] = 1
            search(xs + [n], new_dice, visited)

search([(0,0)], [[None,None,None,None],
                    [None,None,None,None],
                    [None,None,None,None]], np.array([np.zeros(6) for _ in range(1,7)]))
