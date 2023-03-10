import random

class People:

    def __init__(self):
        pass

    def display_gestures(self):
        self.gestures = ["rock", "paper", "scissors", "Lizard", "Spock"]
    
    def choose_gesture(self):
        """
        Returns a string representing a gesture
        """
        pass

class Player_User(People):
    def __init__(self):
        self.wins = 0
    
    # def choose_gesture_user(self):
    #     print()
    #     print("Below is a list of gestures you may choose from.")
    #     self.display_gestures()
    #     while True:
    #         user_choice = int(input("Please enter the number of the gesture you would like to use. > "))
    #         if user_choice in range(1, len(self.gestures) + 1):
    #             user_choice = self.gestures[user_choice - 1].title()
    #             print(f"User has chosen to play {user_choice}.")
    #             return user_choice
    #         print("I'm sorry, that is not an option. Please select again.")
    #         print()

    def choose_gesture(self):
        print()
        print("Below is a list of gestures you may choose from.")
        self.display_gestures()
        for i, gesture in enumerate(self.gestures):
                print(f"{i+1}. {gesture.title()}")
        possible_options = range(1, len(self.gestures) + 1)
    
        while True:
            user_choice = int(input("Please enter the number of the gesture you would like to use. > "))
            
            if user_choice not in possible_options:
                print("I'm sorry, that is not an option. Please select again.")
            else:
                user_choice = self.gestures[user_choice - 1].title()
                print()
                print(f"User has chosen to play {user_choice}.")
                return user_choice

class Player_Computer(People):
    def __init__(self):
        self.player = "Computer"
        self.wins = 0

    def choose_gesture(self):
        print()
        self.display_gestures()
        computer_choice = random.choice(self.gestures).title()
        print(f"Computer has chosen to play {computer_choice}.")
        print()
        return computer_choice
    

# player_1 = Player_User("Player 1")
# player_1.choose_gesture_user()

# computer = Player_Computer()
# computer.choose_gesture_computer()

