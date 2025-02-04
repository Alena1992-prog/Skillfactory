import random

class SeaBattle:
    def __init__(self):
        self.size = 6
        self.board = [['O'] * self.size for _ in range(self.size)]
        self.ships = 3  # число кораблей
        self.hit_ships = 0

    def place_ships(self):
        for _ in range(self.ships):
            while True:
                try:
                    x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
                    if self.board[x][y] == 'O':
                        self.board[x][y] = 'X'
                        break
                except IndexError as e:
                    print(f"Ошибка при размещении корабля: {e}")

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print("")

    def make_move(self, x, y):
        try:
            if self.board[x][y] == 'X':
                print("Попадание!")
                self.board[x][y] = 'X'  # корабль подбит
                self.hit_ships += 1
            elif self.board[x][y] == 'O':
                print("Промах!")
                self.board[x][y] = 'T'  # промах
            else:
                print("Эта клетка уже обстреляна!")
        except IndexError:
            print("Координаты выходят за пределы поля!")

    def computer_move(self):
        while True:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.board[x][y] == 'O':
                print(f"Компьютер стреляет в ({x}, {y})")
                self.make_move(x, y)
                break
            elif self.board[x][y] == 'X' or self.board[x][y] == 'T':
                print(f"Компьютер пытается выстрелить в ({x}, {y}), но промахивается...")

    def play(self):
        self.place_ships()
        while self.hit_ships < self.ships:
            self.print_board()
            while True:
                try:
                    x, y = map(int, input("Введите координаты для выстрела (x y): ").split())
                    self.make_move(x, y)
                    break
                except ValueError:
                    print("Пожалуйста, введите две числа, разделенные пробелом.")

            if self.hit_ships < self.ships:
                self.computer_move()

        print("Поздравляем, вы победили!")

if __name__ == "__main__":
    game = SeaBattle()
    game.play()