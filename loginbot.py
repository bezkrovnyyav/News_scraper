import requests
from requests import Response
from requests.auth import HTTPDigestAuth

import configparser
from fake_useragent import UserAgent

config = configparser.ConfigParser()
config.read('config.cfg')

USERNAME = config.get("user", "USERMAIL", fallback='')
PASSWORD = config.get("user", "USERPASSWORD", fallback='')
LOGIN_URL = config.get("user", "LOGIN_URL", fallback='')

user_agent = UserAgent()
headers = {'user-agent': user_agent.random}
session = requests.Session()

proxies = {
    # 'http': "",
    # 'https': ""
}


def get_login(login_url, username, userpass, headers=headers, proxies=proxies):
    try:
        response = requests.get(
            login_url,
            auth=HTTPDigestAuth(username, userpass),
            headers=headers,
            proxies=proxies
        )
        if response.status_code == 200:
            print("User is loged in")
            return response
        return f"Unsucces request: {response.status_code}"
    except Exception as exc:
        return exc


def check_login():
    login = get_login(LOGIN_URL, USERNAME, PASSWORD)
    if isinstance(login, Response):
        return (f"auth: {login.status_code}")
    else:
        return (f"auth: {login}")


if __name__ == '__main__':
    pass
