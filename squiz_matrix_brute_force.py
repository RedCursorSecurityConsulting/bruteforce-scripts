import bs4
import requests
import time
from main_handler import main, Attempt

class SquizMatrixLogin:
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

        self.csrf_token = soup.find('input', attrs={"name": "SQ_LOGIN_KEY"})['value']

    def login(self, username, password):
        self.find_csrf_token()

        login_data = {
                "SQ_LOGIN_KEY": self.csrf_token,
                "SQ_LOGIN_REFERER": "",
                "SQ_LOGIN_USERNAME": username,
                "SQ_LOGIN_PASSWORD": password,
                "log_in_out_button": "Login"
        }

        login_attempt = self.session.post(self.login_url, data=login_data)

        #403 -> Forbidden
        if login_attempt.status_code == 403:
            return Attempt.Failed

        return Attempt.Success

if __name__ == '__main__':
    main(SquizMatrixLogin)
