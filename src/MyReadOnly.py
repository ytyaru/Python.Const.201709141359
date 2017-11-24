from ConstMeta import ConstMeta

class MyReadOnly(metaclass=ConstMeta):
    __class_var = 'class_value'
    def __init__(self):
        self.__instance_var = 'instance_value'
    def InstanceMethod(self): print('self.__instance_var:', self.__instance_var, hasattr(self, 'test'))
    @staticmethod
    def StaticMethod(): print('StaticMethod.')
    @classmethod
    def ClassMethod(cls): print('cls._MyReadOnly__class_var:', cls._MyReadOnly__class_var)
    @property
    def Property(self): print('Property:', self.__instance_var)
    
