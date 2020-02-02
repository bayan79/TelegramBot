import requests
import time

from conf import api_token

url = 'https://api.telegram.org/bot{api_token}/{method}'

def query(method):
    return url.format(api_token=api_token, method=method)

request = query('getMe')
print(requests.get(request).content)
