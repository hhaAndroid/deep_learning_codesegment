# -*- coding:utf-8 -*-
# deep eyes
from library.c6_python_trick import *


def demo_1():
    # 如何将dict自动变成类内部属性,无法递归
    prop = dict(a=1, b=1, c=3)
    lc = LamdaClass(**prop)
    print(lc.a)
    print(lc.c)


def demo_2():
    # 如何将字典变成可以属性访问? 可以递归
    cd = ADict(dict(a=1, b=1, c=dict(d=1, e=[2, 3], f=dict(a=1))))
    # cd = ADict(dict(a=1, b=1))
    print(cd.a)
    print(cd['a'])
    print(cd.c.e)
    print(cd.c.f.a)


if __name__ == '__main__':
    # demo_1()
    demo_2()
