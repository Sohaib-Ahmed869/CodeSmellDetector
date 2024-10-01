import time


def do_stuff(x, y, z):
    result = 0
    for i in range(10):
        time.sleep(0.5)
        if i % 2 == 0:
            result += x + y + z
        else:
            result -= x - y - z
        print("Result so far: ", result)


def work(a, b):
    a = a + b
    b = b - a
    a = a * b
    print(a)


class Person:
    def _init_(self):
        self.name = ''
        self.age = 0
        self.phone = ''
        self.salary = 100
        self.list = []

    def do_work(self, x):
        if x > 10:
            for i in range(x):
                print(i)
        else:
            for i in range(x):
                print(x)

    def calc_salary(self):
        for i in range(100):
            self.salary += 1
        return self.salary


def some_random_func():
    print('Hello world!')
    return 42


some_random_func()  # Why is this here?

do_stuff(5, 'string', None)  # Whoops, this will break
p = Person()
p.name = 'John'
p.age = 'Twenty'  # Incorrect type
p.phone = 123456  # Incorrect type
p.do_work('10')  # Should be int but passed string
work(1, 2)