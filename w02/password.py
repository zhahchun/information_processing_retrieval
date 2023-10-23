#! python 3.10.13
# password.py: An insecure password locker program.

PASSWORDS = {'google': 'ftstc451810',
             'my_uw': 'uuu',
             'apple_id': 'aaa'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)