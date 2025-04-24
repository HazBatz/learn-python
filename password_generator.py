import secrets
import string

def create_pw(pw_length=12):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_chars = '&"#{[(|-`@^*µ%£!§'

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for x in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

        if(any(char in special_chars for char in pwd)and
               sum(char in digits for char in pwd)>=2):
            pw_strong = True

    return pwd

if __name__ == '__main__':
    print(create_pw())