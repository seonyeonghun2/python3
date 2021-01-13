def hello():
    print('hello')
    print('hello')
    print('hello')

hello()

def print_n_times(value, n):
    for i in range(n):
        print(value)

# print_n_times('안녕하세요', 5, 3)

# print_n_times('안녕')

# 가변 매개변수
def print_n(n, *values):
    #n loop
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n(3,'안녕하세요', '즐거운', '밤이에요')