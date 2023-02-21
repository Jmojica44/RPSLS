
class Game():
    def __init__(self):
        game_mode = input("Would you like to play singleplayer or multiplayer? S or M ")
        self.game_mode = game_mode


    def run_game(self):
        self.introduction()
        self.rules()
    
    def introduction(self):
        print(f'Welcome to rock paper scissors with extra steps.')
    
    def rules(self):
        print("Rules:\n", "Rock crushes Scissors\n", "Scissors cuts Paper\n", "Paper covers Rock\n", "Rock crushes Lizard\n", "Lizard poisons Spock\n", "Spock smashes Scissors\n","Scissors decapitates Lizard\n", "Lizard eats Paper\n", "Paper disproves Spock\n", "Spock vaporizes Rock")
    
    def compare(self, player_1_choice, player_2_choice):
        self.player_1_choice = player_1_choice
        self.player_2_choice = player_2_choice
        self.player_1_wins = player_1_wins
        self.player_2_wins = player_2_wins
        player_1_wins = 0
        player_2_wins = 0
        if player_1_choice == player_2_choice:
            print(f"It's a tie!")
            player_1_wins += 1
        elif player_1_choice == "Rock" and player_2_choice == "Scissors":
            print(f'Player 1 wins!')
            player_1_wins += 1
        elif player_1_choice == "Scissors" and player_2_choice == "Paper":
            print(f'Player 1 wins!')
            player_1_wins += 1
        elif player_1_choice == "Paper" and player_2_choice == "Rock":
            print(f'Player 1 wins!')
            player_1_wins += 1
        elif player_1_choice == "Lizard" and player_2_choice == "Spock":
            print(f'Player 1 wins!')
            player_1_wins += 1
        elif player_1_choice == "Spock" and player_2_choice == "Scissors":
            print(f'Player 1 wins!')
            player_1_wins += 1
        elif player_1_choice == "Scissors" and player_2_choice == "Lizard":
            print(f'Player 1 wins!')
            player_1_wins += 1
        elif player_1_choice == "Lizard" and player_2_choice == "Paper":
            print(f'Player 1 wins!')
            player_1_wins += 1
        elif player_1_choice == "Paper" and player_2_choice == "Spock":
            print(f'Player 1 wins!')
            player_1_wins += 1
        else:
            print(f'Player 2 wins!')
            player_2_wins += 1
    
    # def continue_game(self):
    #     while self.player_1_score < 2 and self.player_2_score < 2:

