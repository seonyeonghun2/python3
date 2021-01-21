# list
# a --> array
a = [i for i in range(1, 6)]
print(a)

# tuple
# b --> pointer (c)
b = (j for j in range(1, 6))
print(b)
# print(b[0])
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

c = iter(a)
print(c, type(c))
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())

# for i in c:
#     print(i)
print('-'*100)
print(2 & 3)
print('{:0<b}'.format(2))

import iterator

print(__name__)