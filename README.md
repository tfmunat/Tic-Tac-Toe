# Tic-Tac-Toe

A graphical game of Tic-Tac-Toe written in Python.

Copy the source file and graphics.py under the same directory.

The game window is set to 500x500. You can change the background color by altering the color name [win.setBackground("colorName")] under the class Interface. To add a custom background, add these two lines under the class Interface. Then comment out the old setBackground call. Make sure the image file is located in the same directory.

Add these two lines right after creating GraphWin:

    img = Image(Point(0, 0), "yourImageFile")
    img.draw(win)


example:

    win = GraphWin("Tic-Tac-Toe", 500, 500)
    img = Image(Point(0, 0), "image.png")
    img.draw(win)
    #win.setBackground("burlywood2")  #comment out this line
