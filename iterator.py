# iterator : 이터레이터

iter1 = iter([1,3,5,7,9])
# print(iter1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

# 이제 값이 없어지기 시작

iter2 = iter(range(1,10))
print(iter2)
for x in iter2:
    print(x)
iter3 = zip([1, 2, 3], ('a', 'b', 'c'))
# print(iter3, type(iter3))
# print(list(iter3))
# print(list(iter3))
# dict = {}
# for i,j in iter3:
#     dict[i]=j
#
# print(dict)


L = [1, 2, 3]
iterator_L = iter(L)
print(iterator_L.__next__())  #1
print(iterator_L.__next__())  #2
print(iterator_L.__next__())  #3
#print(iterator_L.__next__())  #StopIteration 에러

print(__name__)