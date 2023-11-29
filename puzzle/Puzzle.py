import sys 
import pprint

def solve_puzzle(board, start, end):

    
    rows = len(board)
    cols = len(board[0])

    # check for invalid inputs and shortcircuit
    if start[0] > rows or end[0] > rows or start[1] > cols or end[1] > cols:
        return None
    
    # short circuit for edge case
    if start == end:
        return [end]
    
    memo = [[[] for x in range(cols) ] for x in range(rows) ]

    queue = [
        (start[0], start[1]+1, start), #right
        (start[0], start[1]-1, start), #left
        (start[0]-1, start[1], start), #up
        (start[0]+1, start[1], start) #down
    ]
    
    while queue:
        row, col, previous = queue.pop(0)
        prow, pcol = previous

        #bounds check
        if row < 0 or col < 0 or row >= rows or col >= cols:
            continue

        #Blocked
        if board[row][col] == '#':
            continue
        
        cur_path = memo[row][col]
        new_path = memo[prow][pcol] + [(prow,pcol)]
        
        # if we find a better path, let's expore further
        if len(cur_path) == 0 or len(cur_path) > len(new_path):
            memo[row][col] = new_path
            if (row,col) != end:
                queue.append((row, col+1, (row,col)))
                queue.append((row, col-1, (row,col)))
                queue.append((row+1, col, (row,col)))
                queue.append((row-1, col, (row,col)))
            else:
                memo[row][col] = new_path + [end]
        else:
            continue
        
        # end




    if len(memo[end[0]][end[1]]) > 0:

        return (memo[end[0]][end[1]], directions(memo[end[0]][end[1]]))
    
    return None


def directions(nodes):
    result = ""
    for i in range(1,len(nodes)):
        if nodes[i][0] > nodes[i-1][0]:
            result = result + "D"
        if nodes[i][0] < nodes[i-1][0]:
            result = result + "U"
        if nodes[i][1] > nodes[i-1][1]:
            result = result + "R"
        if nodes[i][1] < nodes[i-1][1]:
            result = result + "L"
    return result


def test_solver():
    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ] 

    start = (0,2)
    end = (2,2)
    want =  ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)],"LDDR")
    assert solve_puzzle(puzzle, start, end) == want


    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['#', '#', '#', '#', '#'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ] 

    start = (0,2)
    end = (2,2)
    want =  None
    assert solve_puzzle(puzzle, start, end) == want

    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['#', '#', '#', '#', '#'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ] 

    start = (0,0)
    end = (0,0)
    want = [(0,0)]
    assert solve_puzzle(puzzle, start, end) == want
