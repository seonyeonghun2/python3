import requests
url = 'https://api.github.com'
res = requests.get(url, auth=('userId','userPw'))
print(res.status_code)
print(res.headers['Content-Type'])
print(res.encoding)
print(res.json())
