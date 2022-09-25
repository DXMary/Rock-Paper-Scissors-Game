import random

class color:
    BOLD = '\033[1m'
    END = '\033[0m'
print(color.BOLD + "\nWELCOME TO ROCK, PAPER, SCISSORS!" + color.END)
print("\n-------------------------------------------------------------------------------")

player_wins = 0
computer_wins = 0

keep_going = True
while keep_going:

    rounds = int(input("\nHow many rounds would you like to play? (Type a number between 3 and 10): "))
    counter = 0
    while counter <= rounds-1:
        while rounds not in range(3,11):
            try:
                class color:
                    ITALIC = '\x1B[3m'
                    PURPLE = '\033[95m'
                    END = '\x1B[0m'
                rounds = int(input(color.ITALIC + color.PURPLE + "\nSorry! You can only play between 3 to 10 rounds. Try again: " + color.END))
            except:
                class color:
                    ITALIC = '\x1B[3m'
                    PURPLE = '\033[95m'
                    END = '\x1B[0m'
                print (color.ITALIC + color.PURPLE + "\nInvalid input. Out of range or wrong type of data." + color.END)
        if rounds in range(3,11):
            class color:
                BOLD = '\033[1m'
                END = '\033[0m'
            print (color.BOLD + "\nChallenge accepted. Let's goooo!!" + color.END)
            print("\nType 'quit' at any time if you want to exit the game.")
            break

    for i in range(rounds):
        choices = ["rock", "paper", "scissors"]

        computer = random.choice(choices)
        player = None
        print("\n-------------------------------------------------------------------------------")
        player = input("\nRock, Paper, or Scissors?: ").lower()

        while player != "rock" and player != "paper" and player != "scissors" and player != "quit":
            class color:
                ITALIC = '\x1B[3m'
                PURPLE = '\033[95m'
                END = '\x1B[0m'
            player = input(color.ITALIC + color.PURPLE + "\nInvalid input, please try again: " + color.END).lower()

        if player == "quit":
            class color:
                        BOLD = '\033[1m'
                        END = '\033[0m'
            print(color.BOLD + "\nThank you for playing. Goodbye!\n" + color.END)
            quit()

        if player == computer:
            print("\nYour choice:", player)
            print("Computer's choice:", computer)
            class color:
                BOLD = '\033[1m'
                LIGHTBLUE = '\033[1;34m'
                END = '\033[0m'
            print(color.BOLD + color.LIGHTBLUE + "\nIt's a tie!\n" + color.END)

        elif player == "rock":
            if computer == "paper":
                print("\nYour choice:", player)
                print("Computer's choice:", computer)
                class color:
                    BOLD = '\033[1m'
                    RED = '\033[91m'
                    END = '\033[0m'
                print(color.BOLD + color.RED + "\nYou Lose!", computer, "beats", player, "\n" + color.END)
                computer_wins += 1

            if computer == "scissors":
                print("\nYour choice:", player)
                print("Computer's choice:", computer)
                class color:
                    BOLD = '\033[1m'
                    GREEN = '\033[92m'
                    END = '\033[0m'
                print(color.BOLD + color.GREEN + "\nYou Win!", player, "beats", computer, "\n" + color.END)
                player_wins += 1

        elif player == "scissors":
            if computer == "rock":
                print("\nYour choice:", player)
                print("Computer's choice:", computer)
                class color:
                    BOLD = '\033[1m'
                    RED = '\033[91m'
                    END = '\033[0m'
                print(color.BOLD + color.RED + "\nYou Lose!", computer, "beats", player, "\n" + color.END)
                computer_wins += 1

            if computer == "paper":
                print("\nYour choice:", player)
                print("Computer's choice:", computer)
                class color:
                    BOLD = '\033[1m'
                    GREEN = '\033[92m'
                    END = '\033[0m'
                print(color.BOLD + color.GREEN + "\nYou Win!", player, "beats", computer, "\n" + color.END)
                player_wins += 1

        elif player == "paper":
            if computer == "scissors":
                print("\nYour choice:", player)
                print("Computer's choice:", computer)
                class color:
                    BOLD = '\033[1m'
                    RED = '\033[91m'
                    END = '\033[0m'
                print(color.BOLD + color.RED + "\nYou Lose!", computer, "beats", player, "\n" + color.END)
                computer_wins += 1

            if computer == "rock":
                print("\nYour choice:", player)
                print("Computer's choice:", computer)
                class color:
                    BOLD = '\033[1m'
                    GREEN = '\033[92m'
                    END = '\033[0m'
                print(color.BOLD + color.GREEN + "\nYou Win!", player, "beats", computer, "\n" + color.END)
                player_wins += 1
        
        print("Your score is:", player_wins)
        print("The computer score is:", computer_wins)

    if player_wins > computer_wins:
        print("\n-------------------------------------------------------------------------------")
        class color:
            BOLD = '\033[1m'
            GREEN = '\033[92m'
            END = '\033[0m'
        print(color.BOLD + color.GREEN + "\nCONGRATS! YOU WON THE GAME" + color.END)
        print("\n-------------------------------------------------------------------------------")
            
    elif computer_wins > player_wins:
        print("\n-------------------------------------------------------------------------------")
        class color:
            BOLD = '\033[1m'
            RED = '\033[91m'
            END = '\033[0m'
        print(color.BOLD + color.RED + "\nSORRY, YOU LOST THE GAME" + color.END)
        print("\n-------------------------------------------------------------------------------")

    else:
        print("\n-------------------------------------------------------------------------------")
        class color:
            BOLD = '\033[1m'
            LIGHTBLUE = '\033[1;34m'
            END = '\033[0m'
        print(color.BOLD + color.LIGHTBLUE + "\nIT'S A TIE, NO ONE WON" + color.END)
        print("\n-------------------------------------------------------------------------------")

    response = input("\nDo you want to play another game? (yes/no) ").lower()
    if keep_going == (response == 'yes'):
        player_wins = 0
        computer_wins = 0
        class color:
            BOLD = '\033[1m'
            END = '\033[0m'

    if response == "no":
        class color:
            BOLD = '\033[1m'
            END = '\033[0m'
        print(color.BOLD + "\nThank you for playing. Goodbye!\n" + color.END)
        quit()



   

    

