import copy

global iterations
iterations = 0
global minimum
minimum = 99999

board = list([    [9, 9, 1, 1, 1, 9, 9],
                  [9, 9, 1, 1, 1, 9, 9],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [9, 9, 1, 1, 1, 9, 9],
                  [9, 9, 1, 1, 1, 9, 9]     ]) # 1 is marble, 0 is free slot, 9 is unreachable

def get_right(board, position):
    if (position[1]+1 < 7):
        return board[position[0]][position[1]+1]
    else:
        return 9

def get_left(board, position):
    if (position[1]-1 >= 0):
        return board[position[0]][position[1]-1]
    else:
        return 9

def get_up(board, position):
    if (position[0]-1 >= 0):
        return board[position[0]-1][position[1]]
    else:
        return 9

def get_down(board, position):
    if (position[0]+1 < 7):
        return board[position[0]+1][position[1]]
    else:
        return 9

def make_move(board, source, mid, target):
    board[source[0]][source[1]] = 0
    board[target[0]][target[1]] = 1
    board[mid[0]][mid[1]] = 0
    return board

def valid_move_left(board):

    global iterations
    global minimum
    iterations += 1

    current_sum = sum(sum(board,[]))
    if current_sum < minimum:
        minimum = current_sum

    if iterations%500000 == 0:
        print(str(iterations) + " done.\nMinimum is " + str(minimum-144+1) + "\nCurrent board has " + str(current_sum-144) +" marbles.")

    if current_sum == 145:
        print('Solved puzzle')
        print('-------------')
        print(board)
        return True
    
    for j in range(7):
        for i in range(7):
            if (board[j][i] == 0) or (board[j][i] == 9):
                continue
        
            position = (j, i)

            if (get_right(board, position) == 1) and (get_left(board, position) == 0):
                new_board = make_move(copy.deepcopy(board), (position[0], position[1]+1), position, (position[0], position[1]-1))
                if valid_move_left(new_board):
                    print('-------------')
                    print(board)
                    return True

            if (get_left(board, position) == 1) and (get_right(board, position) == 0):
                new_board = make_move(copy.deepcopy(board), (position[0], position[1]-1), position, (position[0], position[1]+1))
                if valid_move_left(new_board):
                    print('-------------')
                    print(board)
                    return True

            if (get_up(board, position) == 1) and (get_down(board, position) == 0):
                new_board = make_move(copy.deepcopy(board), (position[0]-1, position[1]), position, (position[0]+1, position[1]))
                if valid_move_left(new_board):
                    print('-------------')
                    print(board)
                    return True

            if (get_down(board, position) == 1) and (get_up(board, position) == 0):
                new_board = make_move(copy.deepcopy(board), (position[0]+1, position[1]), position, (position[0]-1, position[1]))
                if valid_move_left(new_board):
                    print('-------------')
                    print(board)
                    return True
        
    return False # no more valid moves found

def main():
    global minimum
    if not valid_move_left(board):
        print('No solution found.')

if __name__ == "__main__":
    main()