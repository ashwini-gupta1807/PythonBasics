import random
import time

def clear_screen():
    # Print clean terminal space
    print("\n" * 50)

def display_welcome():
    # ANSI escape characters for styling
    gold = "\033[1;33m"
    cyan = "\033[1;36m"
    reset = "\033[0m"
    
    welcome_text = f"""
    {gold}=============================================================
    *                                                           *
    *          WELCOME TO KAUN BANEGA CROREPATI (KBC)           *
    *                                                           *
    ============================================================={reset}
    
    {cyan}Rules of the game:{reset}
    1. There are 10 questions in total.
    2. Each question has 4 options: A, B, C, or D.
    3. You will earn money for every correct answer.
    4. Safe Zones (Milestones):
       - Question 5: Rs. 10,000
       - Question 10: Rs. 3,20,000
       If you cross a Safe Zone and answer incorrectly later, you take home the Safe Zone amount.
    5. You have one lifeline: {gold}50-50{reset} (removes 2 wrong options).
       To use it, type '50-50' when prompted for the answer.
    6. You can type 'quit' at any time to quit and take home your current earnings.
    
    Let's begin! Good Luck!
    =============================================================
    """
    print(welcome_text)
    input("Press Enter to start the game...")

def play_kbc():
    # Questions list (Using Python Lists)
    questions = [
        "What is the capital of India?",
        "Which planet is known as the Red Planet?",
        "Who wrote the national anthem of India, 'Jana Gana Mana'?",
        "Which element has the chemical symbol 'O'?",
        "Which is the largest ocean on Earth?",
        "In which year did India win its first Cricket World Cup?",
        "Which is the tallest mountain in the world?",
        "What is the currency of Japan?",
        "Who is known as the 'Iron Man of India'?",
        "Which country is the largest by land area?",
    ]

    # Options list (Using list of lists)
    options = [
        ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Mahatma Gandhi"],
        ["A. Gold", "B. Oxygen", "C. Osmium", "D. Helium"],
        ["A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        ["A. 1975", "B. 1979", "C. 1983", "D. 2011"],
        ["A. K2", "B. Mount Everest", "C. Kangchenjunga", "D. Lhotse"],
        ["A. Won", "B. Yuan", "C. Yen", "D. Ringgit"],
        ["A. Subhas Chandra Bose", "B. Bhagat Singh", "C. Sardar Vallabhbhai Patel", "D. Lal Bahadur Shastri"],
        ["A. Canada", "B. China", "C. USA", "D. Russia"],
    ]

    # Correct answers list (Using a list matching index-by-index)
    answers = ['B', 'B', 'A', 'B', 'C', 'C', 'B', 'C', 'C', 'D']

    # Prizes list (Using a list matching index-by-index)
    prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

    # Color codes for visual styling
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    purple = "\033[1;35m"
    cyan = "\033[1;36m"
    reset = "\033[0m"

    current_earnings = 0
    guaranteed_amount = 0
    lifeline_used = False

    for i in range(len(questions)):
        clear_screen()
        print(f"\n{purple}Question {i+1} for Rs. {prizes[i]:,}:{reset}")
        print(f"{blue}{questions[i]}{reset}\n")

        # Create copy of options so we don't mutate original options list
        current_options = list(options[i])
        
        # Display current options
        for option in current_options:
            print(f"  {option}")
        print()

        # Input loop to handle validation and lifelines
        while True:
            lifeline_str = f" (or type '50-50' for lifeline)" if not lifeline_used else ""
            prompt = f"Enter your choice (A, B, C, D) or 'quit'{lifeline_str}: "
            user_input = input(prompt).strip().upper()

            if user_input == 'QUIT':
                print(f"\n{yellow}You decided to quit the game. You take home: Rs. {current_earnings:,}{reset}")
                print("Thanks for playing!")
                return

            if user_input == '50-50':
                if lifeline_used:
                    print(f"{red}You have already used the 50-50 lifeline!{reset}\n")
                    continue
                else:
                    lifeline_used = True
                    correct_letter = answers[i]
                    correct_index = ord(correct_letter) - ord('A')
                    
                    # Determine which options are wrong
                    wrong_indexes = [idx for idx in range(4) if idx != correct_index]
                    # Select 2 wrong options at random to remove
                    to_remove = random.sample(wrong_indexes, 2)
                    
                    print(f"\n{yellow}Applying 50-50 lifeline...{reset}")
                    time.sleep(1)
                    print(f"\n{purple}Question {i+1} (50-50 Active):{reset}")
                    print(f"{blue}{questions[i]}{reset}\n")
                    
                    valid_choices = [correct_letter]
                    for idx, option in enumerate(current_options):
                        if idx in to_remove:
                            print("  [Option Removed]")
                        else:
                            print(f"  {option}")
                            option_letter = option[0]
                            if option_letter != correct_letter:
                                valid_choices.append(option_letter)
                    print()
                    
                    # Inner loop to get response after using lifeline
                    while True:
                        user_input_lifeline = input("Enter your choice (A, B, C, D) or 'quit': ").strip().upper()
                        if user_input_lifeline == 'QUIT':
                            print(f"\n{yellow}You decided to quit the game. You take home: Rs. {current_earnings:,}{reset}")
                            print("Thanks for playing!")
                            return
                        if user_input_lifeline in ['A', 'B', 'C', 'D']:
                            if user_input_lifeline in valid_choices:
                                user_input = user_input_lifeline
                                break
                            else:
                                print(f"{red}That option was removed! Choose from the remaining options.{reset}")
                        else:
                            print(f"{red}Invalid input. Please enter A, B, C, D or 'quit'.{reset}")
                    break

            if user_input in ['A', 'B', 'C', 'D']:
                break
            else:
                print(f"{red}Invalid input. Please enter A, B, C, D, 'quit' or '50-50'.{reset}\n")

        # Check answer
        if user_input == answers[i]:
            current_earnings = prizes[i]
            print(f"\n{green}CORRECT ANSWER!{reset}")
            print(f"You have won: Rs. {current_earnings:,}")
            
            # Check milestones / Safe Zones
            # Q5 (index 4) and Q10 (index 9)
            if i == 4:
                guaranteed_amount = prizes[i]
                print(f"{yellow}*** Milestone Reached! You are guaranteed Rs. {guaranteed_amount:,} ***{reset}")
            elif i == 9:
                guaranteed_amount = prizes[i]
                print(f"{yellow}*** Milestone Reached! You are guaranteed Rs. {guaranteed_amount:,} ***{reset}")
                
            time.sleep(2)
        else:
            print(f"\n{red}WRONG ANSWER!{reset}")
            print(f"The correct answer was {answers[i]}.")
            print(f"You take home: Rs. {guaranteed_amount:,}")
            print("Thanks for playing!")
            return

    # Completed all questions successfully
    clear_screen()
    gold = "\033[1;33m"
    print(f"\n{gold}=============================================================")
    print("*                                                           *")
    print("*    CONGRATULATIONS! YOU HAVE BECOME A CROREPATI!          *")
    print(f"*    Total Prize Won: Rs. {current_earnings:,}                   *")
    print("*                                                           *")
    print(f"============================================================={reset}")

if __name__ == "__main__":
    display_welcome()
    play_kbc()
