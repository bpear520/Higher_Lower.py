import view
import model

def higher_lower():
    account1 = model.draw_account()
    account2 = model.draw_account()
    score = 0
    lose_condition = False
    while lose_condition is not True:
        player_answer = (view.print_higher_lower(account1, account2, score)).lower()
        right_answer = model.versus_accounts(account1, account2)
        
        if model.check_answer(player_answer, right_answer):
            score += 1
            account1 = account2
            account2 = model.draw_account()
        else:
            lose_condition = True
    print(view.print_final_score(score))


def main():
    higher_lower()
            
        

if __name__ == '__main__':
    main()