import time

def timestamp(func):
    def wrapper():
        print(time.ctime(time.time()))
        return func()
    return wrapper

@timestamp
def hi():
    print('hi')