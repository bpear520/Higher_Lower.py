import game_data
import random


def draw_account():
    return random.sample(game_data.data, 1)[0]

def versus_accounts(account1, account2):
    if account1['follower_count'] > account2['follower_count']:
        return "a"
    else:
        return "b"
    