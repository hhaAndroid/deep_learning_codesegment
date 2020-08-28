# -*- coding:utf-8 -*-
# deep eyes

# 汇集 python 相关的trick写法
try:
    from yapf.yapflib.yapf_api import FormatCode
except:
    FormatCode = None


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


# 3. 复杂dict如何打印的漂亮，更有层次感？
# from mmcv 简化版本
def pretty_text(src_dict):

    def _format_basic_types(k, v):
        if isinstance(v, str):
            v_str = f"'{v}'"
        else:
            v_str = str(v)

        attr_str = f'{str(k)}={v_str}'

        return attr_str

    def _format_list(k, v):
        if all(isinstance(_, dict) for _ in v):
            v_str = '[\n'
            v_str += '\n'.join(
                f'dict({_format_dict(v_)}),'
                for v_ in v).rstrip(',')
            attr_str = f'{str(k)}={v_str}'
            attr_str = attr_str + ']'
        else:
            attr_str = _format_basic_types(k, v)
        return attr_str

    def _format_dict(input_dict, outest_level=False):
        r = ''
        s = []

        for idx, (k, v) in enumerate(input_dict.items()):
            end = '' if outest_level else ','  # 需要符合pep8格式
            if isinstance(v, dict):
                v_str = '\n' + _format_dict(v)  # 递归调用
                attr_str = f'{str(k)}=dict({v_str}'
                attr_str = attr_str + ')' + end
            elif isinstance(v, list):
                attr_str = _format_list(k, v) + end
            else:
                attr_str = _format_basic_types(k, v) + end

            s.append(attr_str)
        r += '\n'.join(s)
        return r
    # outest_level 最外层
    # 仅仅需要把dict按照行排列切割好就行，后面的每行如何格式化采用pep8标准自动执行
    text = _format_dict(src_dict, outest_level=True)
    # 借助yapf库实现的pep8格式化字符串功能实现
    yapf_style = dict(
        based_on_style='pep8',
        blank_line_before_nested_class_or_def=True,
        split_before_expression_after_opening_paren=True)
    text, _ = FormatCode(text, style_config=yapf_style, verify=True)

    return text