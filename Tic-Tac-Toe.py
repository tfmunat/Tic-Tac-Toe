#**************************************************************
# Tic-Tac-Toe by Tahmid Munat
#**************************************************************

# Contact: tahmid.munat@columbia.edu
# December, 2014

#**************************************************************
#**************************************************************


# This is a standard two player game of Tic-Tac-Toe.
# Can also be run by calling Interface()



#*****************************
# imports
#*****************************
from graphics import *
import math, time, random



#**********************
# Class Code
#**********************


#*****************
# Button class
#*****************

class Button:


    #******************************************************************************
    # Creates a rectangular button
    # The parameters are 4 coordinates of the rectangle, color of the rectangle,
    # text inside the rectangle and the size of the text respectively
    #******************************************************************************
    
    def __init__(self, win, coordX1, coordY1, coordX2, coordY2, color, label, labelSize):
        self.x1 = coordX1
        self.x2 = coordX2
        self.y1 = coordY1
        self.y2 = coordY2
        self.color = color
        self.shape = Rectangle(Point(coordX1, coordY1), Point(coordX2, coordY2))
        self.shape.setFill(color)
        self.shape.draw(win)
        self.text = Text(Point(((coordX2 + coordX1) / 2), ((coordY2 + coordY1) / 2)), label)
        self.text.draw(win)
        self.text.setSize(labelSize)

    # deletes the button and its text objects
    def deleteButton(self):
        self.shape.undraw()
        self.text.undraw()

    # Checks if a button was clicked
    # The parameter is a point
    def contains(self, point):
        pointX = point.getX()
        pointY = point.getY()
        if self.x1 <= pointX <= self.x2 and self.y2 <= pointY <= self.y1:
            return True
        else:
            return False        

    # Confirmes that a button was clicked by changing its color
    def press(self):
        self.shape.setFill("gray")
        time.sleep(0.25)
        self.shape.setFill(self.color)


#*****************
# Texts class
#*****************

class Texts:

    #************************************************************************************
    # Draws a text object
    #
    # The parameters are a GraphWin obejct to place the text, x and y coordinate
    # of the text, the text itself and the size of the text respectively
    #*************************************************************************************
    
    def __init__(self, win, xCoord, yCoord, text, textSize):
        self.message = Text(Point(xCoord, yCoord), text)
        self.message.draw(win)
        self.message.setSize(textSize)

    # Changes the text of the chosen text object

    # The parameter is a string that changes the current text
    def setText(self, string):
        self.message.setText(string)

        

#**************************************************************
#**************************************************************




#*******************
# Main Menu Code
#*******************

def Interface():


    #******************************************************************
    # Creates the game window, board and internal graphics components
    #******************************************************************
    
    win = None
    while True:
        if win == None:
            win = GraphWin("Tic-Tac-Toe", 500, 500)
            win.setBackground("burlywood2")
            win.setCoords(-250, -250, 250, 250)

            # Options for the user

            box1 = Button(win, -100, -75, 100, -150,  "beige", "Start Game", 15)
            box2 = Button(win, 190, -190, 240, -230, "orange", "Quit", 10)

            # Text objects

            text1 = Texts(win, 0, 150, "Welcome!", 30)
            text2 = Texts(win, 0, 50, "Time to play Tic-Tac-Toe", 17)


        #****************************************************************
        # Waits for the user to choose an option and reacts accordingly
        #
        # If an option is chosen then the main window closes and
        # the chosen game pops up. The main window returns when
        # the user quits the game. The main window closes if the
        # user selects 'Quit.'
        ##***************************************************************
        
        clickPosition = win.getMouse()

        if box1.contains(clickPosition) == True:
            box1.press()
            box1.deleteButton()
            box2.deleteButton()
            text1.setText("")
            text2.setText("Game is starting! Wait a moment...")
            time.sleep(1)
            text2.setText("")


            #**************************
            # The game of tic-tac-toe
            #**************************
            win.setCoords(-500, -500, 500, 500)

            # Drawing the shape

            # Line points
            l1, l2 = Point(-275, 100), Point(275, 100)
            l3, l4 = Point(-275, -100), Point(275, -100)
            l5, l6 = Point(-100, 275), Point(-100, -275)
            l7, l8 = Point(100, 275), Point(100, -275)

            # Lines
            line1, line2 = Line(l1, l2), Line(l3, l4)                                 
            line3, line4 = Line(l5, l6), Line(l7, l8)
            line1.draw(win), line2.draw(win)
            line3.draw(win), line4.draw(win)
            line1.setWidth(5), line2.setWidth(5)
            line3.setWidth(5), line4.setWidth(5)
            xWin, oWin = 0, 0
            xWinText = Text(Point(400, 250), "'X' wins: %d" %(xWin))
            oWinText = Text(Point(400, 200), "'O' wins: %d" %(oWin))
            xWinText.draw(win), oWinText.draw(win)

            # Labels
            gameText = Texts(win, 0, -400, "May the odds be ever in your favor", 13)
            warning = Texts(win, 0, 400, "", 13)

            # Quit and reset button

            quitButton = Button(win, 400, -480, 480, -400, "orange", "Quit", 10)
            reset = Button(win, 390, -320, 490, -240, "azure3", "Reset", 8)

            # Warning
            warning.setText("You'll be penalized if you click an occupied box. Play wisely!")
            time.sleep(2.5)
            warning.setText("")


            #**************************
            # Internal board
            #**************************

            # Makes a 3x3 board and gets the row and column number
            def makeNewBoard():
                board = []
                for i in range(3):
                    board.append(["."] * 3)
                return board

            board = makeNewBoard()

            def numRows(board):
                return len(board)

            def numColumns(board):
                return len(board[0])

            # Checks for a row, column, up-diagonal and down-diagonal win
            rValue = 0
            def checkRow(r, board, piece):
                for c in range(numColumns(board)):
                    if board[r][c] != piece:
                        return False
                    else:
                        rValue = r
                return True

            cValue = 0
            def checkColumn(c, board, piece):
                for r in range(numRows(board)):
                    if board[r][c] != piece:
                        return False
                    else:
                        cValue = c
                return True

            def checkDownDiagonal(board, piece):
                r = 0
                c = 0
                for i in range(numRows(board)):
                    if board[r][c] != piece:
                        return False
                    else:
                        r = r + 1
                        c = c + 1
                return True

            def checkUpDiagonal(board, piece):
                r = numRows(board) - 1
                c = 0
                for i in range(numRows(board)):
                    if board[r][c] != piece:
                        return False
                    else:
                        r = r - 1
                        c = c + 1
                return True


            # Checks for a cat's game
            def catsGame(board):
                for r in range(numRows(board)):
                    if "." in board[r]:
                        return False
                return True



        #**************************************************************
        #**************************************************************


            #****************
            # The Game
            #****************
            
            currentlyDrawn = []
            status = False
            currentObject = random.choice([1,2])

            # Waits for the user to click

            while status == False:
                clickScreen = win.getMouse()
                pointX, pointY = clickScreen.getX(), clickScreen.getY()

                # If the point lies in a proper region then creates
                # two text objects 'X' and 'O'(doesn't draw)

                if (-270 < pointX < -105) and (105 < pointY < 270) \
                    or (-95 < pointX < 95) and (105 < pointY < 270) \
                    or (105 < pointX < 270) and (105 < pointY < 270) \
                    or (-270 < pointX < -105) and (-95 < pointY < 95) \
                    or (-95 < pointX < 95) and (-95 < pointY < 95) \
                    or (105 < pointX < 270) and (-95 < pointY < 95) \
                    or (-270 < pointX < -105) and (-270 < pointY < -105) \
                    or (-95 < pointX < 95) and (-270 < pointY < -105) \
                    or (105 < pointX < 270) and (-270 < pointY < -105) \
                    or (400 <= pointX <= 480 and -480 <= pointY <= -400) \
                    or (400 <= pointX <= 480 and -320 <= pointY <= -240):
                    objectX = Text(Point(pointX, pointY), 'X')        
                    objectO = Text(Point(pointX, pointY), 'O')

                    # Tests the point and each box to get row and column number

                    r, c = 0, 0
                    if (-270 < pointX < -105) and (105 < pointY < 270):     # upper left
                        r, c = 0, 0
                    elif (-95 < pointX < 95) and (105 < pointY < 270):      # upper middle
                        r, c = 0, 1
                    elif (105 < pointX < 270) and (105 < pointY < 270):     # upper right
                        r, c = 0, 2
                    elif (-270 < pointX < -105) and (-95 < pointY < 95):    # middle left
                        r, c = 1, 0
                    elif (-95 < pointX < 95) and (-95 < pointY < 95):       # middle middle
                        r, c = 1, 1
                    elif (105 < pointX < 270) and (-95 < pointY < 95):      # middle right
                        r, c = 1, 2
                    elif (-270 < pointX < -105) and (-270 < pointY < -105): # bottom left
                        r, c = 2, 0
                    elif (-95 < pointX < 95) and (-270 < pointY < -105) :   # bottom middle
                        r, c = 2, 1
                    elif (105 < pointX < 270) and (-270 < pointY < -105):   # bottom right
                        r, c = 2, 2



                    #*********************
                    # Checks for a win
                    #*********************

                    def checkWin(board, piece):
                        for r in range(numRows(board)):
                            if checkRow(r, board, piece) == True:
                                return True
                        for c in range(numColumns(board)):
                            if checkColumn(c, board, piece) == True:
                                return True
                        if checkDownDiagonal(board, piece) == True:
                            return True
                        elif checkUpDiagonal(board, piece) == True:
                            return True
                        else:
                            return False




                    #******************************
                    # The move making function
                    #******************************
                    
                    def makeMove(board, piece):
                        condition = False
                        while condition == False:
                            if board[r][c] != ".":
                                warning.setText("That position is already occupied! You have lost your turn!")
                                time.sleep(2)
                                warning.setText("")
                                return condition
                            else:
                                board[r][c] = piece
                                if piece == "X":
                                    objectX.draw(win), objectX.setSize(30)
                                    currentlyDrawn.append(objectX)
                                    objectX.setStyle("bold")
                                elif piece == "O":
                                    objectO.draw(win), objectO.setSize(30)
                                    currentlyDrawn.append(objectO)
                                    objectO.setStyle("bold")
                                condition = True
                        return condition
                    


                    #********************
                    # Quit feature
                    #********************
                    
                    if 400 <= pointX <= 480 and -480 <= pointY <= -400:
                        quitButton.press()
                        time.sleep(0.5)
                        yes = Rectangle(Point(400, -340), Point(440, -400))
                        no = Rectangle(Point(440, -400), Point(480, -340))
                        yesText = Text(Point(420, -370), 'Y')
                        noText = Text(Point(460, -370), 'N')
                        yes.draw(win), no.draw(win)
                        yesText.draw(win), noText.draw(win)
                        yes.setFill('green'), no.setFill('red')

                        # Getting confirmation to quit.
                        # Y/N stands for 'Yes' and 'No'
                        confirmation = win.getMouse()
                        confirmX, confirmY = confirmation.getX(), confirmation.getY()
                        if 400 <= confirmX <= 440 and -400 <= confirmY <= -340:
                            status = True
                            for t in currentlyDrawn:
                                t.undraw()
                            currentlyDrawn = []
                            board = makeNewBoard()
                            line1.undraw(), line2.undraw()
                            line3.undraw(), line4.undraw()
                            quitButton.deleteButton(), reset.deleteButton()
                            yes.undraw(), no.undraw()
                            yesText.undraw(), noText.undraw()
                            xWinText.undraw(), oWinText.undraw()
                            xWin, oWin = 0, 0
                            win.setCoords(-250, -250, 250, 250)
                            # Options for the user
                            box1 = Button(win, -100, -75, 100, -150,  "beige", "Start Game", 15)
                            box2 = Button(win, 190, -190, 240, -230, "orange", "Quit", 10)
                            # Text objects
                            text1 = Texts(win, 0, 150, "Welcome!", 30)
                            text2 = Texts(win, 0, 50, "Time to play Tic-Tac-Toe", 17)
                            gameText.setText("")
                                            
                        else:
                            yes.undraw(), no.undraw()
                            yesText.undraw(), noText.undraw()
                            


                    #*********************
                    # Reset feature
                    ##********************
                    
                    elif 400 <= pointX <= 480 and -320 <= pointY <= -240:
                        reset.press()
                        for t in currentlyDrawn:
                            t.undraw()
                        currentlyDrawn = []
                        board = makeNewBoard()
                        # Resetting win numbers
                        xWinText.undraw(), oWinText.undraw()
                        xWin, oWin = 0, 0
                        xWinText = Text(Point(400, 250), "'X' wins: %d" %(xWin))
                        oWinText = Text(Point(400, 200), "'O' wins: %d" %(oWin))
                        xWinText.draw(win), oWinText.draw(win)
                        gameText.setText("May the odds be ever in your favor")
                    
                                    

                    #****************************************
                    # Making plays in Tic-Tac-Toe
                    #****************************************

                    else:
                        # Makes move                                                         
                        if currentObject == 1:
                            # Updates the board to keep track of the status
                            # Draws the icon, appends to the icon-list
                            # Changes player                   
                            makeMove(board, "X")
                            if checkWin(board, "X") == True:
                                xWinText.undraw()
                                xWin = xWin + 1
                                xWinText = Text(Point(400, 250), "'X' wins: %d" %(xWin))
                                xWinText.draw(win)
                                # Drawing the winning lines
                                if checkDownDiagonal(board, "X") == True:
                                    winLine = Line(Point(-180, 180), Point(180, -180))
                                    winLine.draw(win), winLine.setFill("red")
                                    winLine.setWidth(3)
                                elif checkUpDiagonal(board, "X") == True:
                                    winLine = Line(Point(-180, -180), Point(180, 180))
                                    winLine.draw(win), winLine.setFill("red")
                                    winLine.setWidth(3)
                                elif checkRow(r, board, "X") == True:
                                    if r == 0: # upper
                                        winLine = Line(Point(-180, 180), Point(180, 180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif r == 1: # middle
                                        winLine = Line(Point(-180, 0), Point(180, 0))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif r == 2: # lower
                                        winLine = Line(Point(-180, -180), Point(180, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    rValue, cValue = 0, 0
                                elif checkColumn(c, board, "X") == True:
                                    if c == 0: # left
                                        winLine = Line(Point(-180, 180), Point(-180, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif c == 1: # middle
                                        winLine = Line(Point(0, 180), Point(0, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif c == 2: # right
                                        winLine = Line(Point(180, 180), Point(180, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    rValue, cValue = 0, 0
                                gameText.setText("'X' Wins! Great job!")
                                time.sleep(2)
                                gameText.setText("Game is being reset. Thanks for playing")
                                time.sleep(2)
                                for t in currentlyDrawn:
                                    t.undraw()
                                winLine.undraw()
                                currentlyDrawn = []
                                board = makeNewBoard()
                                gameText.setText("May the odds be ever in your favor")
                            elif catsGame(board) == True:
                                gameText.setText("Sorry, cat's game.")
                                time.sleep(2)
                                gameText.setText("Game is being reset. Thanks for playing")
                                time.sleep(2)
                                for t in currentlyDrawn:
                                    t.undraw()
                                currentlyDrawn = []
                                board = makeNewBoard()
                                gameText.setText("May the odds be ever in your favor")
                            else:
                                gameText.setText("Next players turn. You are 'O'")
                                time.sleep(0.5) # To prevent an accidental click
                                currentObject = 2
      
                            
                        elif currentObject == 2:
                            # Updates the board to keep track of the status
                            # Draws the icon, appends to the icon-list
                            # Changes player
                            makeMove(board, "O")
                            if checkWin(board, "O") == True:
                                oWinText.undraw()
                                oWin = oWin + 1
                                oWinText = Text(Point(400, 200), "'O' wins: %d" %(oWin))
                                oWinText.draw(win)
                                # Drawing the winning lines
                                if checkDownDiagonal(board, "O") == True:
                                    winLine = Line(Point(-180, 180), Point(180, -180))
                                    winLine.draw(win), winLine.setFill("red")
                                    winLine.setWidth(3)
                                elif checkUpDiagonal(board, "O") == True:
                                    winLine = Line(Point(-180, -180), Point(180, 180))
                                    winLine.draw(win), winLine.setFill("red")
                                    winLine.setWidth(3)
                                elif checkRow(r, board, "O") == True:
                                    if r == 0: # upper
                                        winLine = Line(Point(-180, 180), Point(180, 180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif r == 1: # middle
                                        winLine = Line(Point(-180, 0), Point(180, 0))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif r == 2: # lower
                                        winLine = Line(Point(-180, -180), Point(180, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    rValue, cValue = 0, 0
                                elif checkColumn(c, board, "O") == True:
                                    if c == 0: # left
                                        winLine = Line(Point(-180, 180), Point(-180, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif c == 1: # middle
                                        winLine = Line(Point(0, 180), Point(0, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    elif c == 2: # right
                                        winLine = Line(Point(180, 180), Point(180, -180))
                                        winLine.draw(win), winLine.setFill("red")
                                        winLine.setWidth(3)
                                    rValue, cValue = 0, 0
                                gameText.setText("'O' Wins! Great job!")
                                time.sleep(2)
                                gameText.setText("Game is being reset. Thanks for playing")
                                time.sleep(2)
                                for t in currentlyDrawn:
                                    t.undraw()
                                winLine.undraw()
                                currentlyDrawn = []
                                board = makeNewBoard()
                                gameText.setText("May the odds be ever in your favor")
                            elif catsGame(board) == True:
                                gameText.setText("Sorry, cat's game.")
                                time.sleep(2)
                                gameText.setText("Game is being reset. Thanks for playing")
                                time.sleep(2)
                                for t in currentlyDrawn:
                                    t.undraw()
                                currentlyDrawn = []
                                board = makeNewBoard()
                                gameText.setText("May the odds be ever in your favor")
                            else:
                                gameText.setText("Next players turn. You are 'X'")
                                time.sleep(0.5) # To prevent an accidental click
                                currentObject = 1

                    

        elif box2.contains(clickPosition) == True:
            box2.press()
            yes = Rectangle(Point(190, -160), Point(215, -190))
            no = Rectangle(Point(215, -190), Point(240, -160))
            yesText = Text(Point(202, -175), 'Y')
            noText = Text(Point(227, -175), 'N')
            yes.draw(win), no.draw(win)
            yesText.draw(win), noText.draw(win)
            yes.setFill('green'), no.setFill('red')

            # Getting confirmation to quit.
            # Y/N stands for 'Yes' and 'No'
            confirmation = win.getMouse()
            confirmX, confirmY = confirmation.getX(), confirmation.getY()

            if 190 <= confirmX <= 215 and -190 <= confirmY <= -160:
                text1.setText("")
                text2.setText("Thanks for playing")
                box1.deleteButton(), box2.deleteButton()
                yes.undraw(), yesText.undraw()
                no.undraw(), noText.undraw()
                time.sleep(1.5)
                win.close()    
                return
            else:
                yes.undraw(), no.undraw()
                yesText.undraw(), noText.undraw()



#********************
# Starting the game
#********************

Interface()



#******************************************************
#******************************************************
