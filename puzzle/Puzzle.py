def solve_puzzle(board, start, end):
    pass

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
    want =  [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]
    assert solve_puzzle(puzzle, start, end) == want
