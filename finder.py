import random
import os
import sys
import time

def finder():
    acc = input('Account Name: ')
    if acc == '':
        print('No account name entered')
        sys.exit(0)
    print('Searching for accounts...')
    time.sleep(3)
    print('Accounts found!')
    time.sleep(1)
    print('Accounts:')
    time.sleep(1)
    print(f'Instagram: https://www.instagram.com/{acc}/?hl=en')
    print(f'Github: https://github.com/{acc}')
    print(f'Twitter: https://twitter.com/{acc}')
    print(f'Reddit: https://reddit.com/u/{acc}')
    print(f'Twitch: https://twitch.tv/{acc}')
    print('Complete!')

def main():
    finder()

if __name__ == '__main__':
    main()