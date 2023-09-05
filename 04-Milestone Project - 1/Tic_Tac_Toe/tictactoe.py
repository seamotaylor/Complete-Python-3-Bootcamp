class TicTacToe:
    def __init__(self):
        # Initialize the game board with labels from 1 to 9
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        # Initialize the current player as "X"
        self.current_player = "X"

    def print_board(self):
        # Function to print the Tic-Tac-Toe board
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def check_win(self):
        # Function to check if the current player has won
        
        # Check rows for a win
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == self.current_player:
                return True

        # Check columns for a win
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == self.current_player:
                return True

        # Check diagonals for a win
        if self.board[0] == self.board[4] == self.board[8] == self.current_player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == self.current_player:
            return True

        # If no win is found, return False
        return False

    def is_board_full(self):
        # Function to check if the board is full (a tie)

        # Check if all positions on the board are filled with "X" or "O"
        return all(cell != str(i + 1) for i, cell in enumerate(self.board))

    def play_game(self):
        # Main game loop
        
        print("Welcome to Tic-Tac-Toe!")
        
        while True:
            self.print_board()  # Display the current game board
            print(f"Player {self.current_player}'s turn.")
            
            move = input("Enter a position (1-9), or 'q' to quit: ")  # Prompt the current player for a move
            
            if move.lower() == 'q':
                print("Thanks for playing! Goodbye.")
                return  # Exit the game

            try:
                move = int(move) - 1  # Convert the input to a zero-based index
                
                # Check if the move is valid (within 1-9) and the selected cell is empty
                if move < 0 or move > 8 or self.board[move] != str(move + 1):
                    raise ValueError()
            except ValueError:
                print("Invalid move. Try again.")
                continue

            self.board[move] = self.current_player  # Update the board with the current player's move

            # Check if the current player has won
            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            # Check if the game is a tie (board is full)
            if self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            # Switch to the other player for the next turn
            self.current_player = "O" if self.current_player == "X" else "X"
