from random import choice

def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = choice(['r','s','p'])

    if user == computer:
        return "It's a Tie"
    
    if is_user_win(user, computer):
        return "you won!!!...."
    
    return "you lose...."

def is_user_win(player, oponent):
    # r>s, s>p, p>r
    if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') or (player == 'p' and oponent == 'r'):
        return True
    
print(play())