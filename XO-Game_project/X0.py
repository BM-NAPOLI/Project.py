import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#? Initialize scores
player_x_wins = 0
player_o_wins = 0
ties = 0    

def display_scoreboard():
    print(f"\n--- Scoreboard ---")
    print(f"Player X Wins: {player_x_wins}")
    print(f"Player O Wins: {player_o_wins}")
    print(f"Ties: {ties}")
    print(f"------------------\n")


class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True: 
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, enter symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol, please enter one letter.")

class Menu:
    def display_main_menu(self):
        menu_text1 = """
        Welcome to my X-O game !
        .1. Start Game
        .2. Quit Game 
        Enter your choice ( 1 or 2 ) : """
        choice = input(menu_text1)
        return choice
    
    def display_endgame_menu(self):
        menu_text2 = """
        Game over !   
        .1. Restart Game
        .2. Quit Game 
        Enter your choice ( 1 or 2 ) : """
        choice = input(menu_text2) 
        return choice

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]

    def display_board(self):
        print("\n" * 2)  
        for i in range(0, 9, 3):
            print(" " * 10 + "  |  ".join(self.board[i:i+3]))
            if i < 6: 
                print(" " * 10 + "-" * 13) 
                print("\n" * 2)  


    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]

class Game:
    def __init__(self):
        self.player = [Player(),Player()]
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == '1':
            self.setup_game()
            self.play_game()
        else:
            self.quit_game()

    def setup_game(self):
        for number, player in enumerate(self.player,start=1):
            print(f"Player {number}")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        clear_screen()
        while True:
            self.play_turn()
            global player_x_wins, player_o_wins, ties

            if self.check_win():
                clear_screen()
                self.board.display_board()
                winner_symbol = self.player[self.current_player_index].symbol
                if winner_symbol == "X":
                    player_x_wins += 1
                else:
                    player_o_wins += 1
                print(f"{self.player[self.current_player_index].name} wins!")
                display_scoreboard()
                choice = self.menu.display_endgame_menu()
                if choice == '1':
                    self.restart_game() 
                else:
                    self.quit_game()
                    break 
            
            elif self.check_draw():
                clear_screen()
                self.board.display_board()
                ties += 1
                print("It's a draw!")
                choice = self.menu.display_endgame_menu()
                if choice == '1':
                    self.restart_game() 
                else:
                    self.quit_game()
                    break 

    def play_turn(self):
        player = self.player[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choice a cell (1-9):"))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice,player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9")        
        self.switch_player()
        clear_screen()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_combination = [
            [0,1,2],[3,4,5],[6,7,8], #! rows
            [0,3,6],[1,4,7],[2,5,8], #! columns
            [0,4,8],[2,4,6]          #! diagonals
        ]
        for combo in win_combination:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] ==
                self.board.board[combo[2]]):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
        
    def quit_game(self):  
        print("\n_ Thank you for your playing !")      




game = Game()
game.start_game()
