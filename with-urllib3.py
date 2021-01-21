import requests
url = 'https://api.github.com'
res = requests.get(url, auth=('seonyeonghun2','aosqkf30x%0*0'))
print(res.status_code)
print(res.headers['Content-Type'])
print(res.encoding)
print(res.json())