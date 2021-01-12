i = 0

while True:
    print('{}번째 반복문 입니다'.format(i))
    i += 1
    input_text= input("> 종료 하시겠습니까?(y): ")
    if input_text in ['y','Y']:
        print('반복을 종료합니다')
        break
print(f'{i}번 반복했습니다')