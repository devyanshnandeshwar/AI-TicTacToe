import random

def drawBoard(board):
    # This function will pront out board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)

    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')

def inputPlayerLetter():

    # Lets the player choose which letter they want to be.

    # returns a list with the player's letter as the first item, and the computer's letter as the second
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be letter X or O? ')
        letter = input().upper()

        # the first element is the list in the player's letter, the second letter is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
        
def whoGoesFirst():
    # randomly choose the player who goes first. 
    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Player'
    
def playAgain():
    # this function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    # given a board and a player's letter, this function returns True if the player has won.
    return ((board[7] == letter and board[8] == letter and board[8] == letter) or# across the top
        (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
        (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
        (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
        (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
        (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
        (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
        (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def getBoardCopy(board):
    # make a duplicate of the bo ard list and return the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    
    return dupeBoard

def isSpaceFree(board, move):
    # return True if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    # Return a valid move from the passed list on the passed board.
    # Return None if there is no valid move.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    # ALGORITHM FOR TIC-TAC-TOE AI:

    # First we check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    
    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    
    # Try to take one of the corners, if its free.
    move = chooseRandomMoveFromList(board, [1, 3, 5, 7])
    if move != None:
        return move
    
    # Try to take the center, if its free.
    if isSpaceFree(board, 5):
        return 5
    
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# MAIN CODE 

print('Welcome to TIC-TAC-TOE')

while True:
    # Reset the board
    board = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' +turn+ ' will go first. ')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player':
            # Player's turn.
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board, playerLetter, move)

            if isWinner(board, playerLetter):
                drawBoard(board)
                print('You have won the game! ')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('The game is a tie! ')
                    break
                else:
                    turn = 'Computer'
        else:
            # Computer's turn.
            move = getComputerMove(board, computerLetter)
            makeMove(board, computerLetter, move)
            
            if isWinner(board, computerLetter):
                drawBoard(board)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player'
    
    if not playAgain():
        break