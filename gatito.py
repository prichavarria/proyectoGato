import os
import csv


class AdmTicTacToe:
 def __init__(self):
   self.file = "gatito.csv"


 def saveBoard(self, board, currentPlayer):
   with open(self.file, 'w') as file:
     writer_csv = csv.writer(file)
     writer_csv.writerow(currentPlayer)
     for i in board:
       writer_csv.writerow(i)


 def updateBoard(self, board):
   currentPlayer = " "
   with open(self.file, "r") as file:
     currentPlayer = file.readline()[0]
     read_csv = csv.reader(file)
     for numFila, row in enumerate(read_csv):
       board[numFila] = row
   return currentPlayer


class Gato:
   def __init__(self):
       self.board = [[' ' for _ in range(3)] for _ in range(3)]
       self.currentPlayer = "X"
       self.admTicTacToe = AdmTicTacToe()


   def print_board(self):
       for row in self.board:
           print('|'.join(row))
           print('-' * 5)


   def move(self, row, col):
     valido = False
     playerMove = self.currentPlayer


     if self.board[row][col] == ' ':
       valido = True
       self.board[row][col] = self.currentPlayer
       self.currentPlayer = 'O' if self.currentPlayer == 'X' else 'X'
       self.admTicTacToe.saveBoard(self.board, self.currentPlayer)
       self.currentPlayer = self.admTicTacToe.updateBoard(self.board)
      
     else:
       print("Movimiento no válido! Intente de nuevo.")


     return (valido, playerMove)
  


   #  Retorna x, o, Empate o None
   def checkWinner(self):
       # Revisar rows
       for row in self.board:
           if row[0] == row[1] == row[2] != ' ':
               return row[0]


       # Revisar columnas
       for col in range(3):
           if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
               return self.board[0][col]


       # Revisar diagonales
       if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
           return self.board[0][0]
       if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
           return self.board[0][2]


       # Revisar por empate
       if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
           return 'Empate'


       # Sin ganador por el momento
       return None


   def obtenerEntero(self, mensaje):
     entero = 0
     valorValido = False


     while not valorValido:
       try:
         entero = int(input(mensaje))
         valorValido = True
       except:
         continue
     return entero
  
   def restartGame(self):
      self.board = [[' ' for _ in range(3)] for _ in range(3)]
     




   def menu (self):
     while True:
       print("\n=== MENÚ ===")
       print("1. Jugar")
       print("2. Reiniciar partida")
       print("3. Salir")


       opcion = self.obtenerEntero("Seleccione una opción: ")


       if opcion == 1:
         self.currentPlayer = self.admTicTacToe.updateBoard(self.board)
         self.play()
         break
       elif opcion == 2:
         #Al no cargar el archivo este se sobreescribe
         self.play()
         break
       elif opcion == 3:
         break
       else:
         print("Opción inválida. Intente de nuevo.\n")


   def play(self):
     while True:
       os.system('cls')
       game.print_board()


       if game.checkWinner():
         result = game.checkWinner()
         if result == 'Empate':
           print("Es un empate!")
         else:
           print(f"El jugador {result} ganó!")
           break


       row = int(input("Digite una fila (0-2): "))
       col = int(input("Digite una columna (0-2): "))
       game.move(row, col)
