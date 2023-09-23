x = int(input("Enter a number of repetitions: "))
def repeat_hello(func):
    def wrapper():
        for _ in range(x):
            func()
    return wrapper
@repeat_hello
def hello():
    print('Hello')
hello()
