import random
import time

import requests


TOKENS = [
    'affe4849c9207b32c08c1547fc969052eb2b2fb1',  # SMIT
    '387d7a59dbaaef002e0f9ac69ecd4443b9c5cef2',  # ON
    '69dd0c01b854bf79805e09bc825ab4cd69e27e8c',  # TORE
    '2f3e40e176df4b97b1e9f25bcf8cd7716a6f6bb9',  # TÖÖKOHT
    '0ab8318acaf6e678dd02e2b5c343ed41111b393d'   # !
]


def make_dummy_request() -> None:
    requests.get(f'localhost:8080/agents?token={random.choice(TOKENS)}')


def make_dummy_requests() -> None:
    while True:
        try:
            make_dummy_request()
        except Exception as e:
            pass
        finally:
            time.sleep(5)


if __name__ == '__main__':
    make_dummy_requests()