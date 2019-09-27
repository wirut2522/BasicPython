print('Log in page')
username = input('Username: ')
password = input('Password: ')
if (username == 'admin' and password == '1234'):
    print('Welcome admin, you\'ve logged in.')
else:
    print('Invalid username or password.')
