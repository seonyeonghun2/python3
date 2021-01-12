list_a = [1, 2, 3, 1, 2, 4]
value = 2
while value in list_a:
    list_a.remove(value)

print(list_a)

import time
number = 0
tg_tick = time.time() + 5
while time.time() < tg_tick:
    number += 1

print('5초 동안 {}번 반복했습니다.'.format(number))