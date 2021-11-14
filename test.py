import requests

headers = {
    "User-agent": 'Nigger'
}
response = requests.get("https://httpbin.org/",headers=headers)


if response.ok:
    print('with response all ok')
