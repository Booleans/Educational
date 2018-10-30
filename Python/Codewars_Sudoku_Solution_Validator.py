# Codewars - Sudoku Solution Validator
# https://www.codewars.com/kata/529bf0e9bdf7657179000008
# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9,
# so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9. 
# (More info at: http://en.wikipedia.org/wiki/Sudoku)

# Write a function validSolution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution,
# or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells.
# Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

import numpy as np

def validSolution(board):
    if 0 in board:
        return False
    board = np.array(board)
    # Check that all rows sum to 45.
    if np.any(np.sum(board, axis=1) != 45):
        return False
    # Check that all cols sum to 45.
    if np.any(np.sum(board, axis=0) != 45):
        return False
    # Check all 3x3 subsquares. 
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if np.any(np.unique(board[i:i+3,j:j+3]) != np.arange(1,10)):
                return False
    return True  
        