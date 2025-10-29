"""
Suppose you have a one-dimensional board of two colors of tiles. Red tiles can only move to the right, black tiles can only move to the left. A tile can move 1 space at a time. Either they move to an adjacent empty space, or they can jump over a single tile of the other color to an empty space.

Eg:
red = R->
black = <-B
empty = _

R _ B _ => _ R B _ or
         R B _ _

R B _ _ => _ B R _
                  
Given a start and end configuration represented as a list of strings, return a list of valid moves to get from start to end (doesn't need to be shortest), including the start and end states in the list of moves. If there's no list of valid moves, return an empty collection.

Example #1:
start_1 = [R, _, B, B]
end_1 = [B, _, B, R]
-> [
  [R, _, B, B],
  [_, R, B, B],
  [B, R, _, B], [B,_,R,B]
  [B, R, B, _], [B,B,R,_]
  [B, _, B, R], [B,B,_,R]  - no possible moves (base case)
]    
    


Example #2:
start_2 = [R, R, _, _]
end_2   = [_, _, R, R]
-> [
  [R, R, _, _],         [R, R, _, _],
  [R, _, R, _],         [R, _, R, _],
  [_, R, R, _],   or    [R, _, _, R],
  [_, R, _, R],         [_, R, _, R],
  [_, _, R, R]          [_, _, R, R]
]

Example #3:
start_3 = [R, B, _]
end_3   = [B, R, _]
-> []

Example #4:
start_4 = [_, B, B]
end_4   = [B, B, _]
->  [_, B, B], 
    [B, _, B], 
    [B, B, _]

Example #5:
start_5 = [R, R, B]
end_5   = [B, R, _]
-> []

Example #6:
start_6 = [_, R, _]
end_6   = [B, R, _]
-> []
   
Example #7:
start_7 = [B, _, R]
end_7   = [R, _, B]
-> []       

Example #8:
start_8 = [_, R, R, B] 
end_8   = [B, R, R, _]
-> []       

Example #9:
start_9 = [R, _, _, B]
end_9   = [R, B, _, _]
-> [
  [R, _, _, B],
  [R, _, B, _],
  [R, B, _, _]
]


All Test Cases:
validMoves(start_1, end_1)
validMoves(start_2, end_2)
validMoves(start_3, end_3)
validMoves(start_4, end_4)
validMoves(start_5, end_5)
validMoves(start_6, end_6)
validMoves(start_7, end_7)
validMoves(start_8, end_8)
validMoves(start_9, end_9)

n: length of the board


Example #1:
start_1 = [R, _, B, B]
end_1 = [B, _, B, R]
-> [
  [R, _, B, B],
  [_, R, B, B],
  [B, R, _, B], [B,_,R,B]
  [B, R, B, _], [B,B,R,_]
  [B, _, B, R], [B,B,_,R]  - no possible moves (base case)
]

calculate all possible moves -> list

base case when no possible moves (len(list of moves)==0)
    if curr array == end: true
    else false

iterate thru possible moves:
    if move in previous_move_set:
        continue
    explore that move -> dfs(move,previous_move_set)
"""
import copy
def validMoves(start, end):
    def find_moves(board):
        # finds all the possible moves given a board, returns []
        moves = []
        for i in range(len(board)):
            # [R, _, B, B]
            possible = []
            if board[i]=="R":
                one_up = i + 1
                two_up = i + 2
                if one_up < len(board) and board[one_up]=="_":
                    possible.append(1)
                if two_up < len(board) and board[one_up]=="B" and board[two_up]=="_":
                    possible.append(2)

            if board[i]=="B":
                one_back = i - 1
                two_back = i - 2
                if one_back >= 0 and board[one_back]=="_":
                    possible.append(-1)
                if two_back >= 0 and board[one_back]=="R" and board[two_back]=="_":
                    possible.append(-2)
            
            for possible_move in possible:
                moves.append((i, possible_move))
        return moves
            
        
        
    # print(find_moves(["R", "_", "B", "B"]))

    def move_board(board, move):
        # board = list
        # move: (index, -2, -1 or 1, 2)
        temp_board = copy.deepcopy(board)
        index, direction = move
        old_tile = temp_board[index]
        new_tile = temp_board[index+direction]
        temp_board[index] = new_tile
        temp_board[index+direction] = old_tile
        
        return temp_board
        

    '''
    board: list
    move: (index of tile to be moved, -1 or 1)

    '''
    def dfs(board, path):
        possible_moves = find_moves(board)
        
        # base case
        if board==end:
            return path

        print(board)
        # iterate thru moves  -- move is (index, -1 or 1)
        for move in possible_moves:
            new_board = move_board(board, move)
            # add this board to path
            path.append(new_board)
            if dfs(new_board, path):
                return path
            # backtrack - remove last elt
            path.pop()
        
        return []
    
    return dfs(start, [])

start_1 = ["R", "_", "B", "B"]
end_1 = ["B", "_", "B", "R"]

print(validMoves(start_1,end_1))



start_2 = ["R", "R", "_", "_"]
end_2 = ["_", "_", "R", "R"]

start_3 = ["R", "B", "_"]
end_3 = ["B", "R", "_"]

start_4 = ["_", "B", "B"]
end_4 = ["B", "B", "_"]

start_5 = ["R", "R", "B"]
end_5 = ["B", "R", "_"]

start_6 = ["_", "R", "_"]
end_6 = ["B", "R", "_"]

start_7 = ["B", "_", "R"]
end_7 = ["R", "_", "B"]

start_8 = ["_", "R", "R", "B"]
end_8 = ["B", "R", "R", "_"]

start_9 = ["R", "_", "_", "B"]
end_9 = ["R", "B", "_", "_"]