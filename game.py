import people 

class Game():
    def __init__(self):
        # game_mode = input("Would you like to play singleplayer or multiplayer? S or M ").lower()
        # self.game_mode = game_mode
        self.player_1_wins = 0
        self.player_2_wins = 0

    def choose_players(self):

        while True:
            print()
            self.game_mode = input("Would you like to play singleplayer or multiplayer? S or M > ").lower()
            # self.game_mode = game_mode
            if self.game_mode == "m":
                self.player_1 = people.Player_User()
                self.player_2 = people.Player_User()
                return self.game_mode
            elif self.game_mode == "s":
                self.player_1 = people.Player_User()
                self.player_2 = people.Player_Computer()
                return self.game_mode
            else:
                print("Sorry, please type either 'S' or 'M'.")
            

    def run_game(self):
        self.choose_players()
        self.introduction()
        self.rules()
        self.continue_game()
        self.declare_winner()
    
    def introduction(self):
        print()
        print(f'Welcome to rock paper scissors with extra steps.')
        print()
    
    def rules(self):
        print("Rules:\n", "\n", "Rock crushes Scissors\n", "Scissors cuts Paper\n", "Paper covers Rock\n", "Rock crushes Lizard\n", "Lizard poisons Spock\n", "Spock smashes Scissors\n","Scissors decapitates Lizard\n", "Lizard eats Paper\n", "Paper disproves Spock\n", "Spock vaporizes Rock")
    
    def compare(self):

        while True:

            if self.game_mode == "s":
                print()
                print(f"""Current Score
    Player 1: {self.player_1_wins} 
    Computer: {self.player_2_wins}""")
                self.player_1_choice = self.player_1.choose_gesture_user()
                self.player_2_choice = self.player_2.choose_gesture_computer()
                break

            elif self.game_mode == "m": 
                print()
                print(f"""Current Score
    Player 1: {self.player_1_wins} 
    Player 2: {self.player_2_wins}""")
                self.player_1_choice = self.player_1.choose_gesture_user()
                self.player_2_choice = self.player_2.choose_gesture_user()
                break


        if self.player_1_choice == self.player_2_choice:
            print(f"It's a tie!")
        elif self.player_1_choice == "Rock" and self.player_2_choice == "Scissors":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Scissors" and self.player_2_choice == "Paper":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Paper" and self.player_2_choice == "Rock":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Lizard" and self.player_2_choice == "Spock":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Spock" and self.player_2_choice == "Scissors":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Scissors" and self.player_2_choice == "Lizard":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Lizard" and self.player_2_choice == "Paper":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Paper" and self.player_2_choice == "Spock":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        elif self.player_1_choice == "Spock" and self.player_2_choice == "Rock":
            print(f'Player 1 wins this round!')
            self.player_1_wins += 1
        else:
            if self.game_mode == "m":
                print(f'Player 2 wins this round!')
            else:
                print("The computer wins this round!")
            self.player_2_wins += 1

    
    def continue_game(self):
        while self.player_1_wins < 2 and self.player_2_wins < 2:
            self.compare()

    def declare_winner(self):
        if self.game_mode == "s":
            if self.player_1_wins >= 2:
                print("Player 1 wins!")
            else: 
                print("The computer wins!")

        else:
            if self.player_1_wins >= 2:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

