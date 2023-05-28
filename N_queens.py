def is_safe(row, col, board):           # It checks for conflicts in the diagonal, column, and row.
    # Check the diagonal
    irow, icol = row, col              
    while irow >= 0 and icol >= 0:           
        if board[irow][icol] == 'Q':       #If it finds a queen in the cell, it means there is a conflict, 
                                           #and it returns False to indicate that placing a queen at position (row, col) is not safe.
            return False
        irow -= 1                  #If no conflict is found, it decrements both irow and icol by 1 to move to the previous diagonal cell (towards the top-left direction).
        icol -= 1

    #check the column
    irow, icol = row, col
    while irow < len(board) and icol >= 0:
        if board[irow][icol] == 'Q':
            return False
        irow += 1                               #column ke liye +row and -col yaad rkho
        icol -= 1

    # Check the row
    irow, icol = row, col
    while icol >= 0:
        if board[irow][icol] == 'Q':
            return False
        icol -= 1                     #row ke liye bs -col

    return True

    
def solve_n_queens(n):   #takes an input n, which represents the size of the chessboard. 
                        #It initializes an empty list called solutions to store all the valid solutions. 
                        #It also creates a board of size n x n initialized with dots (representing empty cells).
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    find_board(n, solutions, board, 0)
    return solutions

def find_board(n, solutions, board, col):   #recursive function that finds all the valid solutions for the N-Queens problem. 
                                            #It takes the board size n, the list of solutions, the board configuration, and the col 

    if col == n:                 #If col is equal to n, it means all the columns have been processed, 
                                 #and a valid solution has been found. The current configuration of the board is added to the solutions list.
        solution = []
        for row in board:
            solution.append(''.join(row))    # joins the characters of each row together using join function
        
        solutions.append(solution)           #appending the solution to solutions list 

        return

    for row in range(n):                          #Otherwise, it iterates over each row in the range of n.

        if is_safe(row, col, board):             #checks if it is safe to place a queen at the current row and col using the is_safe function.
            board[row][col] = 'Q'
            find_board(n, solutions, board, col + 1)   #If it is safe, it places a queen at that position on the board and 
                                                       #recursively calls find_board for the next column (col + 1).
            board[row][col] = '.'

if __name__ == '__main__':
    n = int(input("Enter the board size: "))
    solutions = solve_n_queens(n)

    for solution in solutions:
        for row in solution:
            for ch in row:
                print(ch, end=' ')
            print()
        print("---------------------------------------------------------------")
        print()

    print("Total possible solutions =", len(solutions))
