import requests
from bs4 import BeautifulSoup
start = 900
end = 947
for count in range(start, end):
    url = f'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={count}회로또'
    equal_ind = url.rfind('=')
    title = url[equal_ind + 1:]
    res = requests.get(url)
    if res.status_code != 200:
        print('connect error!')
        exit()

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    numbers = soup.select('.num_box > span')
    output = {}
    output['title'] = title
    num = [number.text for number in numbers]
    # for number in numbers:
    #     num.append(number.text)
    output['number'] = str(num)
    with open('lotto2.txt', 'a', encoding='utf-8') as f:
        f.write()
        f.write('\n')
