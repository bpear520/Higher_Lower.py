import game_data
import random
import model


def draw_account():
    return random.sample(game_data.data, 1)[0]

def versus_accounts(account1, account2):
    if account1['follower_count'] > account2['follower_count']:
        return 'a'
    else:
        return 'b'
    

def check_answer(player_answer, right_answer):
    if player_answer == right_answer:
        return False
    else:
        return True