# Create a program that allows the user to convert temperatures between Fahrenheit and Celsius.
# F = C*(9/5)+32
# C = F-32 * (5/9)

while True:
    print('''
    Welcome! you can convert temperatures between Fahrenheit and Celsius.
    1. Celsius to Fahrenheit
    2. Fahrenheit to Celsius
    3. Exit
            ''')
    
    choice = input('Enter an option: ')

    if choice == '1':
        c = input('Enter temperature in degree Celsius: ')
        # Validating user input
        try:
            c = float(c)
            f = c * (9/5) + 32
            print(f'Temperature in degree Fahrenheit: {f}')
        except:
            print('Invalid input')
    
    elif choice == '2':
        f = input('Enter temperature in degree Fahrenheit: ')
        
        # Validating user input
        try:
            f = float(f)
            c = (f - 32) * (5/9)
            print(f'Temperature in degree Celsius: {c}')
        except:
            print('Invalid input')
    
    elif choice == '3':
        print('Goodbye!')
        exit(0)
        
    else:
        print('Whoops! Invalid selection')