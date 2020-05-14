import argparse
import contextlib
from enum import Enum, auto
import sys

@contextlib.contextmanager
def smart_open(filename=None):
    if filename and filename != '-':
        fh = open(filename, 'w')
    else:
        fh = sys.stdout

    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()

def main(LoginClass):
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', required=True, help='URL of Login page.')
    parser.add_argument('--csrf-url', required=False, default=None, help='URL of page to get CSRF token from [default: same as --url].')
    parser.add_argument('-o', '--output', help='Output file [default: -].')

    username_group = parser.add_mutually_exclusive_group(required=True)
    password_group = parser.add_mutually_exclusive_group(required=True)

    username_group.add_argument('-u', '--username', help='Username')
    username_group.add_argument('-uF', '--usernameFile', help='File containting list of usernames.')

    password_group.add_argument('-p','--password', help='Password')
    password_group.add_argument('-pF', '--passwordFile', help='File containing list of passwords.')

    args = parser.parse_args()

    login_url = args.url
    csrf_url = args.csrf_url

    if args.usernameFile:
        with open(args.usernameFile, 'r') as userFile:
            usernames = userFile.read().splitlines()
    else:
        usernames = [args.username]

    if args.passwordFile:
        with open(args.passwordFile, 'r') as passFile:
            passwords = passFile.read().splitlines()
    else:
        passwords = [args.password]

    login = LoginClass(login_url, csrf_url)

    with smart_open(args.output) as file_handle:
        for username in usernames:
            for password in passwords:
                result = login.login(username, password)

                print(f"{username}:{password} {result.value}", file=file_handle)

class Attempt(Enum):
    Failed = 'Failed to login'
    Success = 'Successfully logged in'


