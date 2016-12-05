# -*- coding=utf-8 -*-

import functools

def vaildation_parameter(func):
    """deco func: check whether parameters are none or nots

    
    ref
    ---
    .. [1] http://stackoverflow.com/questions/10724854/how-to-do-a-conditional-decorator-in-python-2-6
    """
    @functools.wraps(func)
    def _inner(target_class, **kwargs):
        """using para by kwagrs!!!
        """
        for k,v in kwargs.items():
            if v == None:
                raise Exception("PARAMETER %s IS None" % (k))
        result = func(target_class, **kwargs)
        return result
    return _inner