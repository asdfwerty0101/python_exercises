import lib1
import sys
import os

from datetime import time

from lib1 import say_hello1 as sh1, say_hello2
from lib2 import say1, say2
import lib1
MY_CONSTANT = "my constant name"


def say_hello1():
    print('already existing function')


sh1()
say_hello2()
say1()
say2()
print('start.__name__', __name__)
s = "asdf"
say_hello1()
