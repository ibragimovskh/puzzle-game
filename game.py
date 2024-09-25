import random

class NumberGame:
    def __init__(self):
        self.grid = [[0 for _ in range(5)] for _ in range(5)]
        self.current_number = 1

    def initialize_game(self):
        # Place number 1 randomly
        row, col = random.randint(0, 4), random.randint(0, 4)
        self.grid[row][col] = 1
        self.current_number = 2

    def print_grid(self):
        for row in self.grid:
            print(" ".join(f"{num:2d}" if num != 0 else " ." for num in row))
        print()

    def is_adjacent(self, row, col):
        for i in range(max(0, row-1), min(5, row+2)):
            for j in range(max(0, col-1), min(5, col+2)):
                if self.grid[i][j] == self.current_number - 1:
                    return True
        return False

    def place_number(self, row, col):
        if row < 0 or row >= 5 or col < 0 or col >= 5:
            return False, "Invalid cell. Choose a cell within the 5x5 grid."
        if self.grid[row][col] != 0:
            return False, "Cell is not empty. Choose an empty cell."
        if not self.is_adjacent(row, col):
            return False, "Not adjacent to the previous number. Choose an adjacent cell."
        
        self.grid[row][col] = self.current_number
        self.current_number += 1
        return True, "Number placed successfully."

    def is_game_over(self):
        return self.current_number > 25

def main():
    game = NumberGame()
    game.initialize_game()

    print("Welcome to the Number Game - Level 1")
    print("Place numbers from 2 to 25 in ascending order.")
    print("The numbers must be adjacent to the previous number.")

    while not game.is_game_over():
        game.print_grid()
        print(f"Current number to place: {game.current_number}")
        
        try:
            row = int(input("Enter row (0-4): "))
            col = int(input("Enter column (0-4): "))
            success, message = game.place_number(row, col)
            print(message)
        except ValueError:
            print("Invalid input. Please enter numbers for row and column.")

    print("Congratulations! You've completed Level 1.")
    game.print_grid()

if __name__ == "__main__":
    main()