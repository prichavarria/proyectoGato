
import tkinter as tk
from tkinter import font
from tkinter import Tk
from tkinter import messagebox
from tkinter import *
import gatito as gat

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego de gato")
        self._cells = {}
        self.display_frame = None
        self.grid_frame = None
        self._create_board_display()
        self._create_board_grid()


    def Close(self): 
        global board
        board.destroy() 


    def _create_board_display(self):

        self.display_frame = tk.Frame(master=self)

        self.display_frame.pack(fill=tk.X)

        self.display = tk.Label(

            master=self.display_frame,

            text="Bienvenido al juego",

            font=font.Font(size=28, weight="bold"),

        )

        self.display.pack()

    def _pressedButton(self, x, y):
        global game
        isValid = game.move(x, y)
     

        if (isValid[0]):
            self.paintBoard(x, y, isValid[1])
            res = game.checkWinner()
            self.popUpWinner(res)
            

    def paintBoard(self, x, y, player):
       
        paintButton = self._cells[(x, y)]
        
        paintButton.config(text=player)
         

    def popUpWinner(self, res):
        if res == "X" or res == "O" :
            choice=messagebox.askyesno(title="Felicidades", 
                                       message=f"El jugador {res} ha ganado.\n¿Desea reiniciar el juego?")
            if choice == True:
                self._cells.clear()
                self.grid_frame.destroy()
                self.display_frame.destroy()
                game.restartGame()
                self._create_board_display()
                self._create_board_grid()
                

            else:
                self.Close()
                
        elif res == "Empate" :
            choice=messagebox.askyesno(title="Oh no", 
                                       message="El juego ha quedado en empate.¿Desea reiniciar el juego?")
            if choice == True:
                self._cells.clear()
                self.grid_frame.destroy()
                self.display_frame.destroy()
                game.restartGame()
                self._create_board_display()
                self._create_board_grid()
                

            else:
                self.Close()

        else:
            pass


         

    def _create_board_grid(self):

        self.grid_frame = tk.Frame(master=self)
        self.grid_frame.pack()
        for row in range(3):

            self.rowconfigure(row, weight=1, minsize=50)

            self.columnconfigure(row, weight=1, minsize=75)

            for col in range(3):

                button = tk.Button(

                    master=self.grid_frame,

                    text=str(),

                    font=font.Font(size=36, weight="bold"),

                    fg="black",

                    width=3,

                    height=2,

                    highlightbackground="lightblue", 
                    
                    command= lambda x=row, y=col : self._pressedButton(x, y),

                    )

                self._cells[(row, col)] = button

                button.grid(

                    row=row,

                    column=col,

                    padx=5,

                    pady=5,

                    sticky="nsew"

                )
    


def startGame():
    """Create the game's board and run its main loop."""
    global game
    global board
    game = gat.Gato()
    board = TicTacToeBoard()
    board.mainloop()


def main():
    startGame()
    

if __name__ == "__main__":
    main()
