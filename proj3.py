#File: proj3.py
#Author: Matthew Lyan
#Section: 17
#E-mail: mlyan1@umbc.edu
#Description:  Plays the game of sudoku by opening a puzzle from a file and solving the puzzle from the given file


#constants for making the board
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
EMPTYCELL = "0"
CELLSEPERATE = ","
NUMBER6 = "6"
COMMA = ","
ZERO = 0



# prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;   the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ") 
    print("  +-------+-------+-------+")

    for i in range(len(board)): 
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i]) 
        for j in range(len(boardRow)):
            if boardRow[j] == 0:
                boardRow[j] = "_"

        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1, 
                boardRow[0], boardRow[1], boardRow[2], 
                boardRow[3], boardRow[4], boardRow[5], 
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")



# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
#              fileName; the name of the file to use for writing to 
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()



#dropNumber() drops the number onto the board
#             validates the board for correct row, number, col entered as well
#Input:       ints for row, col, number
#Output:      the 2d board list to be rearranged with a valid dropped number
    
def dropNumber(board,undoList):
    flag = False
    while not flag:
        flag = True


        
        row = int(input("Enter a row number between (1-9): "))   
        while row < ONE or row > NINE:         # checks if the row entered is between 1-9
            print("Row must be between 1-9")
            row = int(input("Enter a row number between (1-9): "))
            flag = False
            
        
        col = int(input("Enter a col number between (1-9): "))
        while col < ONE or col > NINE:   #checks if the col entered is between 1-9
            print("Col must be between 1-9")
            col = int(input("Enter a col number between (1-9): "))
            flag = False
        
            
        number = int(input("Enter a number to put in cell:(" + str(row) + "," + str(col) + "): "))
        while number < ONE or number > NINE:   # checks if the number entered is between 1-9
            print("Number must be between 1-9")
            number = int(input("Enter a number to put in cell:(" + str(row) + "," + str(col) + "): "))
            flag = False

        
        
        if board[row-1][col - 1] != 0:      # user validation for checking if there is already a number in the cell
            print("There is already a number in that place")
            flag = False

        if number in board[row-1]:  #user validation for not placing the same number in a row
            print("The number",number, "is already in that row.")
            flag = False


        for i in range(len(board)): #user validation for not placing the same number in a col


            if board[i][col-1] == number:
                print("the number", number, "is already in that column.")
                flag = False


        #if,elif, and for loop are for checking valid nonets
        if row % THREE == 0 and col % THREE == 0:
            checkTop, checkBottom = THREE *((row-ONE)//THREE), ONE *((col-ONE)//THREE)   #mathmatical expression to get to the top left corner of a square


        elif row % THREE == 0:
            checkTop, checkBottom = THREE *((row-ONE)//THREE), THREE *(col//THREE)


        elif col % 3 == 0:
            checkTop, checkBottom = THREE *(row//THREE), THREE *((col-ONE)//THREE)


        else:
            checkTop, checkBottom = THREE *(row//THREE), 3 *(col//THREE)

        for x in range(checkTop, checkTop+THREE):   #once the top left corner has been reached, it checks the row and col of the 3x3 box, if a number is there already or not
            for y in range(checkBottom, checkBottom+THREE):
                if board[x][y] == number:
                    print("the number",number,"is already in that square.")
                    flag = False

        

        

        

    undoList.append([row,col])   #appends the move as coordinates to the undo move list
    board[row-1][col-1] = number      #drops the valid number onto the board
    

    return board



#dropNumberCorrectness() esentially the same function as dropNumber, but with correctness, drops a valid number on the board
#Input:                 ints for row, col, and number
#Output:                the 2d list of board to be changed with the valid number replaced for 0

def dropNumberCorrectness(board,undoList,correctBoard):
    flag = False

    while not flag:

        flag = True
        row = int(input("Enter a row number between (1-9): "))

        while row < ONE or row > NINE:    #Checks if the entered row is between 1-9
            print("Row must be between 1-9")
            row = int(input("Enter a row number between (1-9): "))

            flag = False

        col = int(input("Enter a col number between (1-9): "))
        while col < ONE or col > NINE:      #Checks if the entered col is between 1-9
            print("Col must be between 1-9")
            col = int(input("Enter a col number between (1-9): "))
            flag = False


        number = int(input("Enter a number to put in cell:(" + str(row) + "," + str(col) + "): "))
        while number < ONE or number > NINE:        #Checks if the entered number is between 1-9
            print("Number must be between 1-9")
            number = int(input("Enter a number to put in cell:(" + str(row) + "," + str(col) + "): "))
            flag = False


        if board[row-1][col - 1] != 0: #user validation for placing a number in a cell that already has a number in it.                                                                                     
            print("There is already a number there")
            flag = False




        if number in board[row-1]:  #user validation for not placing the same number in a row                                                                                                               
            print("the number",number,"is already in that row.")
            flag = False


        for i in range(len(board)): #user validation for not placing the same number in a col                                                                                                               
            if board[i][col-1] == number:
                print("the number",number,"is already in that column.")
                flag = False


        #if,elif, and for loop are for checking valid nonets
        if row % THREE == 0 and col % THREE == 0:
            checkTop, checkBottom = THREE *((row-1)//3), THREE *((col-1)//THREE)  #mathmatical expression to get to the top left corner of a 3x3 box


        elif row % 3 == 0:
            checkTop, checkBottom = THREE *((row-1)//THREE), THREE *(col//THREE)


        elif col % 3 == 0:
            checkTop, checkBottom = THREE *(row//THREE), THREE *((col-1)//THREE)


        else:
            checkTop, checkBottom = THREE *(row//THREE), THREE *(col//THREE)

        for x in range(checkTop, checkTop+3):            #once the top left corner has been reached, it checks the row and col of the 3x3 box, if a number is there already or not
            for y in range(checkBottom, checkBottom+3):
                if board[x][y] == number:
                    print("the number",number," is already in that square.")
                    flag = False



        if number != correctBoard[row-1][col-1]:          # this is for implementing the correctness, it compares the number from the board to the solution
            print("OOPS!", number, "does not belong in position (" + str(row) + "," + str(col) + ")!")
            flag = False


    undoList.append([row,col])   # adds the moves as coordinates to a list
    board[row-1][col-1] = number   # drops a valid number into the board
    return board





#def getRow() Used for the recursive function in order to check for a valid row
#Input:      nothing, checks for a valid row
#Output      a boolean flag if the row is valid or not
def getRow(board,row,number):
    for i in range(len(board)):
        if board[row][i] == number:
            return False


    return True

#def getCol() Used for the recursive function in order to check for a valid col
#Input:       nothing, checks for valid col
#Output:      a boolean flag if the col is valid or not
def getCol(board,col,number):
    for i in range(len(board)):
        if board[i][col] == number:
            return False


    return True


#def getBox() used for the recursive function in order to check each nonet
#Input:       Nothing checks for a valid nonet
#Output:      A boolean flag if a nonet is valid or not
def getBox(board,row,col,number):
    for i in range(THREE):
        for j in range(THREE):
            if board[i+row][j+col] == number:
                return False


    return True
#def ifBoardFull() base case for the recursive function, checks if the 2d board list is full
#Input:            Nothing, checks if the board is full
#Output:           returns a boolean flag is the board is full or not
def ifBoardFull(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return False


    return True
                
                                
    

#def solveSudoku() Recursive function for solving the sudoku board
#Input:            Inputs the board that is given by opening the file
#Output:           Outputs a solution with the correct numbers for a sudoku puzzle
def solveSudoku(board):


    row = 0
    col = 0

    if ifBoardFull(board):     # base case, if the board is full the function exits
        return True

    else:   #finds a vacant spot
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 0:
                    row = x
                    col = y

    #assign list values to the row and col that we got above

    for number in range(1,TEN):     

        if getRow(board,row,number) == True and getCol(board,col,number) == True and getBox(board,row-row%THREE,col-col%THREE,number) == True:     # if there is a valid row, col and box to be placed

            board[row][col] = number  #places the number

            if solveSudoku(board):  # keeps recalling the function in order to check if theres a number
                return True


            board[row][col] = 0  #resets the board's row and col to 0 in order to keep checking for valid locations


    return False

    





#def makeSolution() makes a deep copy of the solution in the recursive function
#Input:            Inputs the solution from the solveSudoku function
#Outputs:          Returns a copy of the solveSudoku function in as a 2d list
def makeSolution(board):
    solution = []
    for element in board:
        solution.append(element[:])

    solveSudoku(solution)
    return solution
        



def main():
    myFile = input("Enter the puzzle you want to solve: ")
    openFile = open(myFile, "r")
    openBoard = openFile.readlines()
    board = []
    gameOver = False
    keepPlaying = False
    keepPlaying2 = False
    undoList = []
    for i in range(len(openBoard)):   #makes a 2d list for the board 
        eachLine = openBoard[i].strip()
        eachLines = eachLine.split(COMMA)
        for j in range(len(eachLines)): # makes each number in the list a interger
            eachLines[j] = int(eachLines[j])
        board.append(eachLines)
    solution = makeSolution(board)
    
    prettyPrint(board)
    while not gameOver: # loop for the whole structure of the program
        userChoice = input("play(p) or solve (s)?: ")
                
        if userChoice == "p":
            correctness = input("correctness checking(y/n): ")
            if correctness == "y":
                while not keepPlaying2:
                    playChoices= input("play number(p), save(s), undo (u), quit (q): ")
                    if playChoices == "p":
                        board = dropNumberCorrectness(board,undoList,solution)
                        prettyPrint(board)

                        if board == solution:
                            print("You have won!")
                            keepPlaying2 = True
                            gameOver = True



                        
                        


                    if playChoices == "s":
                        saveFile = input("What file do you want to save the game in? ")
                        savePuzzle(board,saveFile)


                    if playChoices == "u":

                        if not undoList:
                            print("There are no moves to undo")

                        else:


                            
                            coordinates = undoList[-1:][0]     #searches for the last element of the undoList(previous move that the player has made)
                            row = coordinates[0]
                            col = coordinates[1]
                            undoList.remove(coordinates)
                            board[row-1][col-1] = 0
                            print("Your move has been undone")
                        prettyPrint(board)

                    if playChoices == "q":
                        print("Here is your final board")
                        prettyPrint(board)
                        keepPlaying2 = True
                        gameOver = True

                        
                    



            else:
                while not keepPlaying:  # loop to keep playing sudoku, until its solved or quit
                    playChoices= input("play number(p), save(s), undo (u), quit (q): ")
                    if playChoices == "p":
                
                        board = dropNumber(board,undoList)
                        prettyPrint(board)

                        if board == solution:
                            print("You have won!")
                            keepPlaying = True
                            gameOver = True


                    if playChoices == "s":
                        saveFile = input("What file do you want to save the game in? ")
                        savePuzzle(board,saveFile)


                    if playChoices == "u":
                        if not undoList:
                            print("There are no moves to undo")

                        else:

                            
                            coordinates = undoList[-1:][0]
                            row = coordinates[0]
                            col = coordinates[1]
                            undoList.remove(coordinates)
                            board[row-1][col-1] = 0
                            print("Your move has been undone")
                        prettyPrint(board)

                    if playChoices == "q":
                        print("Here is your final board")
                        prettyPrint(board)
                        keepPlaying = True
                        gameOver = True
                    
                    
                

        else:
            if solveSudoku(board):
                prettyPrint(board)
            else:
                print("No solution exists")
                    
            #put the solved sudoku solution here
            gameOver = True
            
    
    

main()
    
