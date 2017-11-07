import types
import sys
import functools

def fib(times):
    index=0
    a,b=0,1

    while(index<times):
        yield b
        a,b=b,a+b
        index+=1
    return "done"

def outer():
    def inner():
        print("inner")
    return inner


def ref_count():
    x = 10000
    y = sys.getrefcount(x)
    print(y)
    b = x
    print(sys.getrefcount(b))



class Person(object):
    def __init__(self):
        print("init")

    def __getattribute__(self, item):
        if (item=="a"):
            return "redirect a"
        else:
            return self.b

def aaa(self):
    print("+"*30)


def show_args(*args, **kwargs):
    print(args)
    print(kwargs)


p1 = functools.partial(show_args,a="1")

p1(a="2")

