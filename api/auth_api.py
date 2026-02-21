import requests

from data.urls import Urls

API_BASE = Urls.url_main.rstrip('/')


def register_user(name: str, email: str, password: str) -> requests.Response:
    return requests.post(
        f'{API_BASE}/api/auth/register',
        json={'name': name, 'email': email, 'password': password}
    )


def login_user(email: str, password: str) -> requests.Response:
    return requests.post(
        f'{API_BASE}/api/auth/login',
        json={'email': email, 'password': password}
    )


def get_token(email: str, password: str) -> str:
    resp = login_user(email, password)
    return resp.json()['accessToken']


def delete_user(token: str) -> requests.Response:
    return requests.delete(
        f'{API_BASE}/api/auth/user',
        headers={'Authorization': f'Bearer {token}'}
    )
