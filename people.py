import random

class People:

    def __init__(self):
        self.wins = 0

    def display_gestures(self):
        self.gestures = ["rock", "paper", "scissors", "Lizard", "Spock"]
        for i, gesture in enumerate(self.gestures):
                print(f"{i+1}. {gesture.title()}")
        print()

class Player_User(People):
    def __init__(self, player):
        self.player = player 
    

    def choose_gesture_user(self):
        print()
        print("Below is a list of gestures you may choose from.")
        self.display_gestures()
        while True:
            user_choice = int(input("Please enter the number of the gesture you would like to use. > "))
            if user_choice in range(1, len(self.gestures) + 1):
                user_choice = self.gestures[user_choice - 1]
                print(f"{self.player} has chosen to play {user_choice.title()}.")
                return user_choice
            print("I'm sorry, that is not an option. Please select again.")

class Player_Computer(People):
    def __init__(self):
        self.player = "Computer"

    def choose_gesture_computer(self):
        print()
        print("Of the below options:")
        self.display_gestures()
        computer_choice = random.choice(self.gestures)
        print(f"Computer has chosen to play {computer_choice.title()}.")
        print()
        return computer_choice

player_1 = Player_User("Player 1")
player_1.choose_gesture_user()

# computer = Player_Computer()
# computer.choose_gesture_computer()