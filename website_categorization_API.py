try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from base64 import urlsafe_b64encode
import hashlib
import requests
import json


def webshrinker_categories_v3(access_key, secret_key, url=b"", params={}):
    params['key'] = access_key
    request = "categories/v3/{}?{}".format(urlsafe_b64encode(
        url).decode('utf-8'), urlencode(params, True))
    request_to_sign = "{}:{}".format(secret_key, request).encode('utf-8')
    signed_request = hashlib.md5(request_to_sign).hexdigest()
    return "https://api.webshrinker.com/{}&hash={}".format(
        request, signed_request)


def find_categories(url):
    print(url)
    access_key = "G3pg6qDzboaOdP9nX1XI"
    secret_key = "vQjLFU6mKhnutMgaPjED"
    url = url.encode('utf-8')
    api_url = webshrinker_categories_v3(access_key, secret_key, url)
    response = requests.get(api_url)
    data = response.text
    status_code = response.status_code
    categories = []

    if status_code == 200 or status_code == 202:
        for x in json.loads(data)['data'][0]['categories']:
            categories.append(x['label'])
        print('succeed')
    elif status_code == 400:
        print("Bad or malformed HTTP request")
    elif status_code == 401:
        print("Unauthorized - check your access and secret key permissions")
    elif status_code == 402:
        print("Account request limit reached")
    else:
        print("A general error occurred, try the request again")
    lenth = len(categories)
    if lenth == 0:
        categories.append('Uncategorized')
        categories.append('Uncategorized')
    if lenth == 1:
        categories.append('Uncategorized')
    return categories[0:2]


if __name__ == '__main__':
    while True:
        url = input('web:')
        print('categories:', find_categories(url))
