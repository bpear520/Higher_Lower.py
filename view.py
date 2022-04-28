import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def print_account_stats(account):
    return f"{account['name']}, {account['description']}, from {account['country']}"

def print_higher_lower(account1, account2, score):
    os.system('CLS')
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {print_account_stats(account1)}")
    print(vs)
    print(f"Against B: {print_account_stats(account2)}")
    return input("Who has more followers? Type 'A' or 'B': ")

def print_final_score(score):
    os.system('CLS')
    print(logo)
    return f"Sorry, that's wrong. Final Score: {score}"