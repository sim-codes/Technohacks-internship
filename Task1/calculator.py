# Task Instruction
# Create a basic calculator that can perform basic arithmetic operations such as addition,
# subtraction, multiplication, and division using functions

def add():
    '''A function that prompt user for 2 operands and perform addition'''
    a = input('Enter first operand: ')
    b = input('Enter second operand: ')
    try:
        ans = int(a) + int(b)
    except:
        print('\nComputaional error!')
        return
    print(f'{a} + {b} = {ans}')

def sub():
    '''A function that prompt user for 2 operands and perform subtraction'''
    a = input('Enter first operand: ')
    b = input('Enter second operand: ')
    try:
        ans = int(a) - int(b)
    except:
        print('\nComputaional error!')
        return
    print(f'{a} - {b} = {ans}')

def mul():
    '''A function that prompt user for 2 operands and perform multiplication'''
    a = input('Enter first operand: ')
    b = input('Enter second operand: ')
    try:
        ans = int(a) * int(b)
    except:
        print('\nComputaional error!')
        return
    print(f'{a} * {b} = {ans}')

def div():
    '''A function that prompt user for 2 operands and perform division'''
    a = input('Enter first operand: ')
    b = input('Enter second operand: ')
    try:
        ans = int(a) / int(b)
    except:
        print('\nComputaional error!')
        return
    print(f'{a} / {b} = {ans}')


def mul_op():
    '''A function that prompt user for a mathematcal expression and perform the computation'''
    exp = input('Enter expression: ')
    try:
        ans = eval(exp)
    except:
        print('\nComputaional error!')
        return
    print(f'{exp} = {ans}')


def main_menu():
    menu = '''
===============================================================
    Welcome selection any option to continue
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Multiple operations (+,/,*,-)
    6. Exit
===============================================================
'''
    print(menu)
    opt = input('Enter choice: ')

    if opt == '1':
        add()
    elif opt == '2':
        sub()
    elif opt == '3':
        mul()
    elif opt == '4':
        div()
    elif opt == '5':
        mul_op()
    elif opt == '6':
        exit()
    else:
        print('Invalid option')

    
while True:
    main_menu()