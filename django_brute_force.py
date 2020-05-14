import requests
import bs4
from main_handler import main, Attempt

class DjangoLogin():
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

        self.token = soup.find('input', attrs={"name":"csrfmiddlewaretoken"})['value']

    def login(self, username, password):
        self.find_csrf_token()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.4086.0 Safari/537.36",
            "Referer": self.csrf_url
        }

        data = {
            "csrfmiddlewaretoken": self.token,
            "username": username,
            "password": password,
        }

        response = self.session.post(self.login_url, headers=headers, data=data)

        bad_patterns = [
                "are not correct",
                "Please enter the correct username and password"
        ]

        for pattern in bad_patterns:
            if pattern in response.text:
                return Attempt.Failed

        return Attempt.Success

if __name__ == '__main__':
    main(DjangoLogin)
