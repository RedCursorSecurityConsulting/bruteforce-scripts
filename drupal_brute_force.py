import requests
import bs4
from main_handler import main, Attempt

import random
import string

class DrupalLogin():
    def __init__(self, login_url, csrf_url):
        self.session = requests.Session()
        self.login_url = login_url

        if not csrf_url:
            self.csrf_url = login_url
        else:
            self.csrf_url = csrf_url

    def find_csrf_token(self):
        response = self.session.get(self.csrf_url).text
        soup = bs4.BeautifulSoup(response, 'lxml')

        self.token = soup.find('input', attrs={"name":"form_build_id"})['value']

    def login(self, username, password):
        self.find_csrf_token()

        data = {
            "form_build_id": self.token,
            "name": username,
            "pass": password,
            "form_id": "user_login_form",
            "op": "Log+in"
        }

        response = self.session.post(self.login_url, data=data, allow_redirects=False)

        if "Unrecognised username or password" in response.text:
            return Attempt.Failed

        return Attempt.Success

if __name__ == '__main__':
    main(DrupalLogin)
