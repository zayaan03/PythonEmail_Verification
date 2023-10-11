# zayaanscherg06@gmail.com
# conditions: length, dot position, @ sign position with domain and count, no space in email, no uppercase in email
def email_verification():
    k, j = 0, 0

    email = input('Enter the email for verification: ')  # enter email
    print('Checking your email....')
    print('Verifying....')
# checking conditions with if-else statements
    if len(email) >= 6:
        if email[0].isalpha():
            if ('@' in email) and (email.count('@') == 1):
                if email[-4] == '.' or email[-3] == '.':
                    for i in email:
                        if i == ' ':
                            k = 1

                    if k == 1 or j == 1:
                        print('Wrong email 5')
                    else:
                        print('Verification passed')
                else:
                    print('wrong email 4')
            else:
                print('Wrong email 3')
        else:
            print('Wrong email 2')
    else:
        print('Wrong email 1')


email_verification()
