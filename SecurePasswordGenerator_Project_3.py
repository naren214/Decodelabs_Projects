import secrets
import string

def get_choice(prompt):
    while True:
        c=input(prompt).strip().lower()
        if c in ('y','n'):
            return c=='y'
        print('Please enter Y or N.')

def password_strength(length):
    return 'Weak' if length<8 else 'Medium' if length<12 else 'Strong'

def generate_password():
    print('\n===== Secure Password Generator =====')
    while True:
        try:
            length=int(input('Enter password length: '))
            if length<4:
                print('Password length must be at least 4.')
                continue
            break
        except ValueError:
            print('Please enter a valid number.')
    cats=[]
    if get_choice('Include uppercase letters? (Y/N): '): cats.append(string.ascii_uppercase)
    if get_choice('Include lowercase letters? (Y/N): '): cats.append(string.ascii_lowercase)
    if get_choice('Include numbers? (Y/N): '): cats.append(string.digits)
    if get_choice('Include special characters? (Y/N): '): cats.append(string.punctuation)
    if not cats:
        print('You must select at least one character type.')
        return
    if length<len(cats):
        print(f'Password length must be at least {len(cats)}.')
        return
    pwd=[secrets.choice(cat) for cat in cats]
    allchars=''.join(cats)
    while len(pwd)<length:
        pwd.append(secrets.choice(allchars))
    secrets.SystemRandom().shuffle(pwd)
    print('\nGenerated Password:', ''.join(pwd))
    print('Password Strength:', password_strength(length))

def main():
    while True:
        generate_password()
        if input('\nGenerate another password? (Y/N): ').strip().lower()!='y':
            print('\nThank you for using the Secure Password Generator!')
            break

if __name__=='__main__':
    main()
