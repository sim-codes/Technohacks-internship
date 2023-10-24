# Create a program that allows the user to play
# the classic game of rock, paper, scissors
# against the computer.

from random import choice

game_list = ['Rock', 'Paper', 'Scissors']

rd = usr = pc = 0


def check_win():
    """Checks and return winner using all possible combinations"""

    if usr_choice == pc_choice:
        return 'Draw'

    elif (usr_choice == 'Rock' and pc_choice == 'Scissors')\
        or (usr_choice == 'Paper' and pc_choice == 'Rock')\
        or (usr_choice == 'Scissors' and pc_choice == 'Paper'):
        return 'User'
    
    elif (pc_choice == 'Rock' and usr_choice == 'Scissors')\
        or (pc_choice == 'Paper' and usr_choice == 'Rock')\
        or (pc_choice == 'Scissors' and usr_choice == 'Paper'):
        return 'Computer'
    
    else:
        return False
    

while rd != 5:
    print(f'Round {rd+1} of 5')

    print('''
    1. Rock
    2. Paper
    3. Scissors
    4. Exit
            ''')

    usr_choice = input('Pick your weapon: ')

    if usr_choice == '4':
        exit()

    # Check if user input is valid
    try:
        usr_choice = game_list[int(usr_choice)-1]
    except:
        print('Invalid weapon selection')
        continue

    # Allow computer make random selection
    pc_choice = choice(game_list)

    print(f'''
    You choose: {usr_choice}
    Computer choose: {pc_choice}
        ''')


    if check_win() == 'User':
        print('--- You won! ---')
        usr += 1
    elif check_win() == 'Computer':
        print('--- Computer won ---!')
        pc += 1
    elif check_win() == 'Draw':
        print('It\'s a tie!')
    else:
        print('Invalid weapon selection!')

    print(f'\nComputer: {pc}\nUser: {usr}\n')
    rd += 1