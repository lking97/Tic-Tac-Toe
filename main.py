class TicTacToe:
    def __init__(self):
        """Initialize the game state."""
        self.board = ["-"] * 9                  # 3x3 board represented as a list
        self.current_player = "X"               # X always starts
        self.winner = None                      # Stores the winner ("X" or "O")
        self.game_still_running = True          # Tracks if the game is active

    def display_board(self):
        """Prints the current board with position references (1-9)."""
        print("\n")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}     1 | 2 | 3")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}     4 | 5 | 6")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}     7 | 8 | 9")
        print("\n")

    def handle_turn(self):
        """Handles a single player's move with input validation."""
        print(f"{self.current_player}'s turn.")
        position = input("Choose a position from 1-9: ")

        # Input validation loop
        while True:
            # Check if input is valid number
            if position not in [str(n) for n in range(1,10)]:
                position = input("Invalid input. Choose a number 1-9: ")
                continue

            # Convert to list index
            position = int(position) - 1

            # Check if spot is free
            if self.board[position] != "-":
                position = input("That spot is taken. Choose another: ")
                continue

            # Exit loop if valid move
            break

        # Place the player's mark on the board
        self.board[position] = self.current_player
        self.display_board()

    def change_player(self):
        """Switches the active player (X ↔ O)."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_rows(self):
        """Check all rows for a win."""
        for i in range(0, 9, 3):    # 0-2, 3-5, 6-8
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != "-":
                self.game_still_running = False
                return self.board[i]    # Return the winner symbol
        return None

    def check_columns(self):
        """Check all columns for a win."""
        for i in range(3):  # First three columns
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "-":
                self.game_still_running = False
                return self.board[i]
        return None

    def check_diagonals(self):
        """Check both diagonals for a win."""
        # Top-left → bottom-right
        if self.board[0] == self.board[4] == self.board[8] != "-":
            self.game_still_running = False
            return self.board[0]
        # Top-right → bottom-left
        if self.board[2] == self.board[4] == self.board[6] != "-":
            self.game_still_running = False
            return self.board[2]
        return None

    def check_winner(self):
        """Determine the winner of the game, if any."""
        self.winner = (
            self.check_rows()
            or self.check_columns()
            or self.check_diagonals()
        )

    def check_tie(self):
        """Check if the board is full and no winner exists (tie)."""
        if "-" not in self.board and not self.winner:
            self.game_still_running = False

    def check_game_over(self):
        """Check if the game should end due to win or tie."""
        self.check_winner()
        self.check_tie()

    def play_game(self):
        """Play one full game of TicTacToe."""
        self.__init__()     # Reset game state at start
        self.display_board()

        # Main game loop
        while self.game_still_running:
            self.handle_turn()
            self.check_game_over()
            if self.game_still_running:     # Prevents unnecessary switch after win
                self.change_player()

        # Show result
        if self.winner:
            print(f"{self.winner} won!")
        else:
            print("It's a tie!")

    def start(self):
        while True:
            self.play_game()
            restart = input("Play again? (y/n): ").lower()
            if restart != "y":
                print("Thanks for playing!")
                break

# Run game if executed directly
if __name__ == "__main__":
    TicTacToe().start()