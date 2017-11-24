#import sub
import MyConst
print('MyConst:', MyConst, type(MyConst))#<const._const object at 0xb7162f4c>
MyConst.test = 'test'
print(MyConst.test)
#MyConst.test = 'test' #Const.ConstError: readonly。再代入禁止。

import MyConst
#MyConst.test = 'test' #Const.ConstError: readonly。再代入禁止。


import MyReadOnly
print('MyReadOnly:', MyReadOnly, type(MyReadOnly))#<const._const object at 0xb7162f4c>
MyReadOnly.test = 'test'
print(MyReadOnly.test)
#MyReadOnly.test = 'test'# Const.ConstError: readonly。再代入禁止。

#MyReadOnlyはインスタンスでありクラスの型ではない
#ro = MyReadOnly()  #TypeError: 'MyReadOnly' object is not callable
#シングルトンとして使うイメージか。

MyReadOnly.InstanceMethod()
MyReadOnly.StaticMethod()
MyReadOnly.ClassMethod()
MyReadOnly.Property
