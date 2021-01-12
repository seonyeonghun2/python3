# 리스트 선언
list1 = [273, 32, 103, 57, 29]

# 리스트와 반복문
for i in range(len(list1)):
    print(f'{i}번째 반복 : {list1[i]}')

# 역 반복문1
for i in range(4,-1,-1):
    print(f'현재 반복 변수 : {i}')

# 역 반복문2
for i in reversed(range(5)):
    print(f'현재 반복 변수 : {i}')