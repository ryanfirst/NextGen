i = 1
while i == 1:
    password = input('Please create a password: ')
    correct_pass = input('Please re-enter password: ')
    while len(password) < 8 or password.lower() == password and i == 1 or correct_pass != password:
        print('password must contain at least 8 characters and have at least one uppercase letter. Or passwords do '
              'not match')
        password = input('Please create a password: ')
        correct_pass = input('Please re-enter password')
        if correct_pass == password and len(password) > 8 and password.lower() != password:
            i = 2
            print('password created')