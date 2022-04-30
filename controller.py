from operator import mod
import view
import model
import random


def get_correct_answer(account1, account2):
    if account1['follower_count'] > account2['follower_count']:
        return 'a'
    else:
        return 'b'


def higher_lower():
    account1 = random.sample(model.data, 1)[0]
    account2 = random.sample(model.data, 1)[0]
    score = 0
    playing = True

    while playing:
        view.print_accounts(account1, account2, score)

        player_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        right_answer = get_correct_answer(account1, account2)
        
        if player_answer == right_answer:
            score += 1
            account1 = account2
            account2 = random.sample(model.data, 1)[0]
        else:
            playing = False
    
    view.print_final_score(score)


def main():
    higher_lower()


if __name__ == '__main__':
    main()