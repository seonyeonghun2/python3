# file object
#
# f = open('some_file.txt', 'w', encoding='utf-8')
# f.write('당신은 사랑받기 위해 태어난 사람')
# f.close()

with open('basic.txt', 'a') as f:
    f.write('hello python world!....!')
    f.write('처음 만드는 파이썬 파일')