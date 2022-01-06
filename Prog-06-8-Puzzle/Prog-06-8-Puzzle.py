# 2110101 Computer Programming

# Prog-06: 8-Puzzle
# 6330085821 

def is_goal(node): 
    return node[:-1] == \
           list(range(1,len(node)-1))+[0]

def insert_all(node, fringe):
    n = len(node)
    children = gen_successors(node)
    for i in range(0,len(children),n):
        fringe.append(children[i:i+n])

def bfs(board):
    start_node = board + ['']
    fringe = [start_node]
    while True:
        if len(fringe) == 0:
            break
        front = fringe[0]
        fringe = fringe[1:]
        if is_goal(front):
            return front[-1]
        insert_all(front,fringe) 
    return ''

def print_successors(s):
    N = 1
    for e in s:
        if type(e) is str: break
        N += 1
    for i in range(0,len(s),N):
        print(s[i:i+N])
#---------------------------------------

    
def gen_successors(node):
    # A B C
    # D E F
    # G H I
    
    #A-RD  B-LRD   C-LD
    #D-RUD E-LRUD  F-LUD
    #G-RU  H-LRU   I-LU
    successors = []
    i = node.index(0)
    def R(node) :
            new_node = list(node)
            (new_node[i], new_node[i+1]) = (new_node[i+1], new_node[i])
            new_node[9] = node[9] + "R"
            successors.extend(new_node)
    def L(node) :
            new_node = list(node)
            (new_node[i-1], new_node[i]) = (new_node[i], new_node[i-1])
            new_node[9] = node[9] + "L"
            successors.extend(new_node)
        
    def U(node):
            new_node = list(node)
            (new_node[i], new_node[i-3]) = (new_node[i-3], new_node[i])
            new_node[9] = node[9] + "U"
            successors.extend(new_node)
    def D(node):      
            new_node = list(node)
            (new_node[i], new_node[i+3]) = (new_node[i+3], new_node[i])
            new_node[9] = node[9] + "L"
            successors.extend(new_node)
    if i == 0:
        D(node)
        R(node)
       
    elif i == 1:
        L(node)
        D(node)
        R(node)
    elif i == 2:  
        L(node)
        D(node)
    elif i == 3:
        U(node)
        D(node)
        R(node)
    elif i == 4:
        L(node)
        D(node)
        R(node)
        U(node)
    elif i == 5:
        L(node)
        D(node)
        U(node)
    elif i == 6:
        R(node)
        U(node)
    elif i == 7:
        L(node)
        R(node)
        U(node)
    elif i == 8:
        L(node)
        U(node)   
    return successors 
#------------------------------------------
def print_moves(board, moves):
    print(board[0],' ',board[1],' ',board[2])
    print(board[3],' ',board[4],' ',board[5])
    print(board[6],' ',board[7],' ',board[8])    
    for j in range(len(moves)):
        print("----------",moves[j])
        if moves[j] == 'U':
            k = board.index(0)
            board[k],board[k-3] = board[k-3],board[k]
        elif moves[j] == 'D':
            k = board.index(0)
            board[k],board[k+3] = board[k+3],board[k]
        elif moves[j] == 'L':
            k = board.index(0)
            board[k-1],board[k] = board[k],board[k-1]
        elif moves[j] == 'R':
            k = board.index(0)
            board[k],board[k+1] = board[k+1],board[k]
        print(board[0],' ',board[1],' ',board[2])
        print(board[3],' ',board[4],' ',board[5])
        print(board[6],' ',board[7],' ',board[8])
            
    return
    
#------------------------------------------
board = [1,3,0,4,2,5,7,8,6]
s = gen_successors(board + ['ULD'])
print_successors(s)
moves = bfs(board)
print(moves)
print_moves(board, moves)
