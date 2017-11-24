#http://ichitcltk.hustle.ne.jp/gudon2/index.php?pageType=file&id=python_class_meta1.md

class ConstMeta(type):
    class ConstError(TypeError): pass        
    """
    @classmethod
    def __prepare__(metacls, name, bases): return {}

    def __call__(self):
    def __call__(self, arg):
        print("__call__", arg)
        super(ConstMeta, self).__call__()

    def __new__(cls, name, bases, dict):
        print("__new__", name, bases, dict)
        return super(ConstMeta, cls).__new__(cls, name, bases, dict)
    """
    def __init__(self, name, bases, dict):
        print('__init__', name, bases, dict, self, type(self))
        super(ConstMeta, self).__init__(name, bases, dict)
        import sys
        sys.modules[name]=self()#ConstMetaを継承したクラスのモジュールに、そのクラスのインスタンスを代入する
        
    def __setattr__(self, name, value):
        if name in self.__dict__.keys(): raise self.ConstError('readonly。再代入禁止。')
        super(ConstMeta, self).__setattr__(name, value)

