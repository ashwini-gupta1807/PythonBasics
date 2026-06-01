import random

def play_game():
    # Choices mapping
    # 0 -> Snake, 1 -> Water, 2 -> Gun
    choices = {0: "Snake", 1: "Water", 2: "Gun"}
    
    # 2D Matrix representing game outcomes
    # Rows (first index): Player Choice (0: Snake, 1: Water, 2: Gun)
    # Columns (second index): Computer Choice (0: Snake, 1: Water, 2: Gun)
    # Values: 
    #   0 -> Draw
    #   1 -> Player Wins (User wins)
    #  -1 -> Computer Wins (User loses)
    outcome_matrix = [
        [0,  1, -1],  # Row 0: Player chooses Snake (S vs S: Draw, S vs W: Win, S vs G: Lose)
        [-1, 0,  1],  # Row 1: Player chooses Water (W vs S: Lose, W vs W: Draw, W vs G: Win)
        [1, -1,  0]   # Row 2: Player chooses Gun   (G vs S: Win, G vs W: Lose, G vs G: Draw)
    ]
    
    # Text colors using ANSI escape sequences
    green = "\033[1;32m"
    red = "\033[1;31m"
    yellow = "\033[1;33m"
    cyan = "\033[1;36m"
    reset = "\033[0m"
    
    print(f"{cyan}============================================")
    print("      SNAKE, WATER & GUN - MATRIX GAME")
    print(f"============================================{reset}")
    print("Rules:")
    print("  - Snake vs Water -> Snake wins")
    print("  - Water vs Gun -> Water wins")
    print("  - Gun vs Snake -> Gun wins")
    print("-" * 44)
    
    while True:
        # Get player input
        print("\nChoose your action:")
        print("0: Snake")
        print("1: Water")
        print("2: Gun")
        print("Type 'q' to quit")
        
        user_input = input("Enter choice (0/1/2/q): ").strip().lower()
        
        if user_input in ['q', 'quit', 'exit']:
            print(f"\n{yellow}Thanks for playing! Goodbye!{reset}")
            break
            
        if user_input not in ['0', '1', '2']:
            print(f"{red}Invalid choice. Please enter 0, 1, or 2.{reset}")
            continue
            
        player_choice = int(user_input)
        computer_choice = random.randint(0, 2)
        
        print(f"\nYour choice: {choices[player_choice]}")
        print(f"Computer's choice: {choices[computer_choice]}")
        
        # Calculate outcome using the 2D Matrix
        result = outcome_matrix[player_choice][computer_choice]
        
        if result == 0:
            print(f"{yellow}It's a Draw! 🤝{reset}")
        elif result == 1:
            print(f"{green}You Win! 🎉{reset}")
        else:
            print(f"{red}You Lose! 😢{reset}")
            
        print("-" * 44)

if __name__ == "__main__":
    play_game()
