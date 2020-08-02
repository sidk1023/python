import tkinter
from tkinter import*
from tkinter import messagebox

import random
###basic construction
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.geometry("275x425")
window.resizable(0,0)
top_frame = tkinter.Frame(window, width = 300, height = 50, bd = 3)
top_frame.pack()
game_frame = tkinter.Frame(window, width = 300, height = 300, bd=3, highlightbackground = 'black', highlightcolor = 'black', highlightthickness = 1)
game_frame.pack()
info_frame = tkinter.Frame(window, width = 300, height = 100, bd=3)
info_frame.pack()
#declaration of string variables for tkinter
#buttons
b1text = tkinter.StringVar()
b2text = tkinter.StringVar()
b3text = tkinter.StringVar()
b4text = tkinter.StringVar()
b5text = tkinter.StringVar()
b6text = tkinter.StringVar()
b7text = tkinter.StringVar()
b8text = tkinter.StringVar()
b9text = tkinter.StringVar()

#this variable shows the turn info
infotext = tkinter.StringVar()

#these variables show score of x and o
s1 = tkinter.StringVar()
s2 = tkinter.StringVar()
s1str = "PlayerX score = "
s2str = "PlayerO score = "
Xsc= 0
Osc= 0

#########FUNCTIONS######################
#this is to select the starting turn

     
#this is to set the score after each turn    
def set_score():
    s1.set(s1str+ str(Xsc))
    s2.set(s2str+ str(Osc))
set_score()    

#this function checks if the player has won the game
def wincheck(board, mark):
     return ((board[1] == mark and board[2] == mark and board[3] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across the bottom
    (board[2] == mark and board[5] == mark and board[8] == mark) or # down the middle
    (board[1] == mark and board[4] == mark and board[7] == mark) or # down the left
    (board[3] == mark and board[6] == mark and board[9] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#the is the main gameplay function, which updates with each button click
count = 0
if random.randint(0, 1) == 0:
    var1 = "X"
    var2="O"
else:
    var1 = "O"
    var2="X"

infotext.set(var1 +"'s turn")
        


def update(self,button):
    global count
    if count%2 ==0:##to alternate the turns
       
        self.set(var1)
        
        infotext.set(var2 +"'s turn")
    else:
        self.set(var2)
        
        infotext.set(var1 +"'s turn")
    button['state']= DISABLED    
    count+=1    
    board =  ["#",b1text.get(),b2text.get(),b3text.get(),b4text.get(),b5text.get(),b6text.get(),b7text.get(),b8text.get(),b9text.get()]
    #above is the board on which we apply functions
    if wincheck(board, "X"):
        messagebox.showinfo("Result", "X Wins!")
        reset_()
        global Xsc
        Xsc+=1
    
        set_score()
        
        return
           
    if wincheck(board, "O"):
        messagebox.showinfo("Result", "O Wins!")
        reset_()
        global Osc
        Osc+=1

        set_score()
        
        return
    if "" not in board:
        messagebox.showinfo("Result", "Draw!")
        reset_()
        return
#resetting buttons
def res_but():
    b1["state"] = NORMAL
    b2["state"] = NORMAL
    b3["state"] = NORMAL
    b4["state"] = NORMAL
    b5["state"] = NORMAL
    b6["state"] = NORMAL
    b7["state"] = NORMAL
    b8["state"] = NORMAL
    b9["state"] = NORMAL
#resetting the board

def reset_():
    b1text.set('')
    b2text.set('')
    b3text.set('')
    b4text.set('')
    b5text.set('')
    b6text.set('')
    b7text.set('')
    b8text.set('')
    b9text.set('')
    res_but()
    
#resetting the score(start from scratch)    
def reset_score():
    global Xsc
    global Osc
    Xsc = 0
    Osc = 0
    set_score()
    reset_()

##################GUI###############    
#first row
b1 = tkinter.Button(game_frame, textvariable = b1text, activebackground = "#e6feff", fg = 'black', font = ("arial", 20, 'bold'), width = 2, height = 1, bg = "#a5edf0", cursor = "hand2", command = lambda :update(b1text,b1))
b1.grid(row = 0, column =0,padx=1, pady=1)
b2 = tkinter.Button(game_frame, textvariable = b2text,  font = ("arial", 20, 'bold'),activebackground = "#e6feff",fg = 'black', width = 2, height = 1, bg = "#c7e9eb", cursor = "hand2", command = lambda :update(b2text,b2))
b2.grid(row = 0, column =1,padx=1, pady=1)
b3 = tkinter.Button(game_frame, textvariable = b3text,  font = ("arial", 20, 'bold'),activebackground = "#e6feff",fg = 'black', width = 2, height = 1, bg = "#a5edf0", cursor = "hand2", command = lambda :update(b3text,b3))
b3.grid(row = 0, column =2,padx=1, pady=1)
#second row
b4 = tkinter.Button(game_frame, textvariable = b4text,  font = ("arial", 20, 'bold'),activebackground = "#e6feff",fg = 'black', width = 2, height = 1, bg = "#c7e9eb", cursor = "hand2", command = lambda :update(b4text,b4))
b4.grid(row = 1, column =0,padx=1, pady=1)
b5 = tkinter.Button(game_frame, textvariable = b5text,  font = ("arial", 20, 'bold'),activebackground = "#e6feff",fg = 'black', width = 2, height = 1, bg = "#a5edf0", cursor = "hand2", command = lambda :update(b5text,b5))
b5.grid(row = 1, column =1,padx=1, pady=1)
b6 = tkinter.Button(game_frame, textvariable = b6text,  font = ("arial", 20, 'bold'),activebackground = "#e6feff",fg = 'black', width = 2, height = 1, bg = "#c7e9eb", cursor = "hand2", command = lambda :update(b6text,b6))
b6.grid(row = 1, column =2,padx=1, pady=1)
#third row
b7 = tkinter.Button(game_frame, textvariable = b7text, font = ("arial", 20, 'bold'),activebackground = "#e6feff", fg = 'black', width = 2, height = 1, bg = "#a5edf0", cursor = "hand2", command = lambda :update(b7text,b7))
b7.grid(row = 2, column =0,padx=1, pady=1)
b8 = tkinter.Button(game_frame, textvariable = b8text,  font = ("arial", 20, 'bold'),activebackground = "#e6feff",fg = 'black', width = 2, height = 1, bg = "#c7e9eb", cursor = "hand2", command = lambda :update(b8text,b8))
b8.grid(row = 2, column =1,padx=1, pady=1)
b9 = tkinter.Button(game_frame, textvariable = b9text,  font = ("arial", 20, 'bold'),activebackground = "#e6feff",fg = 'black', width = 2, height = 1, bg = "#a5edf0", cursor = "hand2", command = lambda :update(b9text,b9))
b9.grid(row = 2, column =2,padx=1, pady=1)
#score
lb1 = tkinter.Label(info_frame, textvariable = s1, font =('arial', 12, 'bold') ).grid(row = 0, column = 0)
lb2 = tkinter.Label(info_frame, textvariable = s2, font =('arial', 12, 'bold') ).grid(row = 1, column = 0)
#reset button
reset = tkinter.Button(info_frame, text = "Reset Table", font = ("arial", 12, 'bold'), width = 15, height = 2, cursor = "hand2", command = reset_).grid(row = 3, columnspan = 3, column = 0, padx = 1, pady= 1)
#info button on top
title = tkinter.Label(top_frame, text = "Welcome to Tic-Tac-Toe!", font = ("arial", 10, 'bold' )).grid(row = 0)
info = tkinter.Label(top_frame, textvariable = infotext, font = ("arial", 20, 'bold' )).grid(row = 1)
#reset the score
resetsc = tkinter.Button(info_frame, text = "Reset Score", font = ("arial", 12, 'bold'), width = 15, height = 2, cursor = "hand2", command = reset_score).grid(row = 4, columnspan = 3, column = 0, padx = 1, pady= 1)
window.mainloop()