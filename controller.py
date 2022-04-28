import view
import model
import os


def main():
    account1 = model.draw_account()
    account2 = model.draw_account()
    score = 0
    lose_condition = False
    while lose_condition is not True:
        os.system('CLS')
        player_answer = view.print_higher_lower(account1, account2, score)
        right_answer = model.versus_accounts(account1, account2)
        
        if player_answer == right_answer:
            score += 1
            account1 = account2
            account2 = model.draw_account()
        else:
            lose_condition = True
    if lose_condition:
        os.system('CLS')
        print(view.print_final_score(score))
            
        

if __name__ == '__main__':
    main()