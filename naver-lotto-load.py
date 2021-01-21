import requests
from bs4 import BeautifulSoup
que='로또당첨번호'
params = {'where':'news', 'sm':'tab_jum','query':que}
# ?where=news&sm=tab_jum&query=로또
url = 'https://search.naver.com/search.naver'
res = requests.get(url, params=params)
# print(res.url)
soup = BeautifulSoup(res.text, 'html.parser')
html = soup.prettify()
html_imgs = soup.select('.dsc_thumb')
print(len(html_imgs))
# with open('naver2.html', 'w', encoding='utf-8') as f:
#     f.write(html)


