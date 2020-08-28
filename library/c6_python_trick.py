# -*- coding:utf-8 -*-
# deep eyes

# 汇集 python 相关的trick写法


# 1. 如何将dict参数自动变成类内部属性？
class LamdaClass(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # 通过内置属性实现


# 2. 如何将字典变成可以属性访问?
try:
    # 2.1直接按照第三方库addict即可
    from addict import Dict


    class ADict(Dict):
        pass
except:
    # 2.2 仿照addict库，最简写法，目的是学习，没有其他好处
    class ADict(dict):
        def __init__(self, *args):
            super().__init__()
            for arg in args:
                for key, val in arg.items():
                    self[key] = self._hook(val)

        def _hook(self, item):
            if isinstance(item, dict):
                return ADict(item)  # 递归调用
            return item

        # 在.a和['a']时候自动调用
        def __getattr__(self, item):
            return self[item]
