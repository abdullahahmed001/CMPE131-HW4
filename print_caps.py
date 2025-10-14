#from print_caps import allcaps
def allcaps(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@allcaps
def greet():
    return "hello World!"