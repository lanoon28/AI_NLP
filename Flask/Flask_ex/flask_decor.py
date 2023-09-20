# def hello():
#     print('hello start')
#     print('hello')
#     print('hello end')

# def world():
#     print('world start')
#     print('world')
#     print('world end')

# hello()
# world()

# 데코레이터 적용
def check(func):
    def wrapper():
        print(func.__name__, 'start')
        func()
        print(func.__name__, 'end')
    return wrapper

@check
def hello():
    print('hello')

@check
def world():
    print('world')

hello()
world()