# 리스트, 튜플, 딕셔너리, 셋
# list(), tuple(), dict()

# p.72  / 85 /  88 / 97
# 리스트 vs 튜플 : 수정이 가능 vs 수정 불가능
# 튜플의 선언
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t1, type(t1))
print(t2)
print(t3)
print(t4, type(t4))
print(t5)

# 튜플의 값을 수정, 삭제할때 (p.86)
t1 = (1, 2, 'a', 'b')
del t1[0]
# 튜플 --> 리스트 변경 --> 원소를 조작 --> 튜플
t2 = list(t1)
t2[0] = 99
print(t2)
