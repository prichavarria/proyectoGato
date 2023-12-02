import os
import csv

class AdmGato:
  def __init__(self):
    self.archivo = "gatito.csv"

  def guardarTablero(self, tablero, jugador_actual):
    with open(self.archivo, 'w') as archivo:
      escritor_csv = csv.writer(archivo)
      escritor_csv.writerow(jugador_actual)
      for i in tablero:
        escritor_csv.writerow(i)

  def actualizarTablero(self, tablero):
    jugador_actual = " "
    with open(self.archivo, "r") as archivo:
      jugador_actual = archivo.readline()[0]
      lector_csv = csv.reader(archivo)
      for numFila, fila in enumerate(lector_csv):
        tablero[numFila] = fila
    return jugador_actual

class Gato:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
        self.admGato = AdmGato()

    def print_tablero(self):
        for fila in self.tablero:
            print('|'.join(fila))
            print('-' * 5)

    def movimiento(self, fila, col):
      if self.tablero[fila][col] == ' ':
        self.tablero[fila][col] = self.jugador_actual
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
        self.admGato.guardarTablero(self.tablero, self.jugador_actual)
        self.jugador_actual = self.admGato.actualizarTablero(self.tablero)
      else:
        print("Movimiento no válido! Intente de nuevo.")

    def rev_ganador(self):
        # Revisar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]

        # Revisar columnas
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != ' ':
                return self.tablero[0][col]

        # Revisar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]

        # Revisar por empate
        if all(self.tablero[fila][col] != ' ' for fila in range(3) for col in range(3)):
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

    def menu (self):
      while True:
        print("\n=== MENÚ ===")
        print("1. Jugar")
        print("2. Reiniciar partida")
        print("3. Salir")

        opcion = self.obtenerEntero("Seleccione una opción: ")

        if opcion == 1:
          self.jugador_actual = self.admGato.actualizarTablero(self.tablero)
          self.jugar()
          break
        elif opcion == 2:
          #Al no cargar el archivo este se sobreescribe
          self.jugar()
          break
        elif opcion == 3:
          break
        else:
          print("Opción inválida. Intente de nuevo.\n")

    def jugar(self):
      while True:
        os.system('cls')
        juego.print_tablero()

        if juego.rev_ganador():
          result = juego.rev_ganador()
          if result == 'Empate':
            print("Es un empate!")
          else:
            print(f"El jugador {result} ganó!")
            break

        fila = int(input("Digite una fila (0-2): "))
        col = int(input("Digite una columna (0-2): "))
        juego.movimiento(fila, col)

# Main game loop
juego = Gato()
juego.menu()