import random

# ASCII art for Rock, Paper, and Scissors
Rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
'''

Paper = '''
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
'''

Scissors = '''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
'''

# List of choices
choices = [Rock, Paper, Scissors]
choice_names = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    return random.randint(0, 2)

def display_choices(user_choice, computer_choice):
    print(f'Your choice is {choice_names[user_choice]}:\n{choices[user_choice]}')
    print(f'Computer choice is {choice_names[computer_choice]}:\n{choices[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It is a Tie!'
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return 'You win!'
    else:
        return 'You lose!'

def play_game():
    while True:
        print('Welcome to the World Best Rock Paper Scissors Game!\n')
        print('0: Rock\n1: Paper\n2: Scissors')

        try:
            user_choice = int(input('Select 0 for Rock, 1 for Paper, and 2 for Scissors: '))
            if user_choice not in [0, 1, 2]:
                raise ValueError("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter 0, 1, or 2.")
            continue

        computer_choice = get_computer_choice()

        display_choices(user_choice, computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to continue playing 'Y' or 'N': ").strip().upper()
        if play_again != 'Y':
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()