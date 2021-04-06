## Python 核心基础知识



#### 一、python一切皆对象

```python
'''
1. type、object和class的关系:
'''
a = 1
b = "abc"
print(type(1))  # <class 'int'>
print(type(int))  # <class 'type'>
print(type(b))  # <class 'str'>
print(type(str))  # <class 'type'>

# type => int => 1
# 表示 1 是 int 这个类的一个实例, int是type这个类的实例
# 表示 'abc' 是 str 这个类的一个实例, str是type这个类的实例


class Student:
    pass


stu = Student()
print(type(stu))  # <class '__main__.Student'>
print(type(Student))  # <class 'type'>
print(int.__bases__)  # (<class 'object'>,)
print(str.__bases__)  # (<class 'object'>,)
print(Student.__bases__)  # (<class 'object'>,)


# object 是最顶层基类
# type是一个类、同时type也是一个对象
print(type.__bases__)  # (<class 'object'>,)
print(object.__bases__)  # ()
print(type(object))  # <class 'type'>

```

<img src=".\type、object与class.png" alt="type、object与class" style="zoom:50%;" />



#### 二、魔法函数

##### 什么是魔法函数?

- Python里面的魔法函数，是以双下划线开头和结尾
- 魔法函数不依赖任何类，并且可以随时调用
- 一旦类里面加上一些特定的魔法函数，整个类就被附加了一些特定的功能.
- 魔法函数定义了我们不需要显式的调用它，Python解释器自己会知道什么情况下会调用，我们在使用相应的语法的时候就会自动调用。
- 魔法函数和本身的类没有关系，和类的父类，object也没有关系。魔法函数可以写到任意一个类中，跟继不继承没有必然的关系。

##### 实例

- for循环的是可迭代对象, 首先通过\_\_iter\_\_得到一个迭代器, 然后不断调用迭代器的\_\_next\_\_, 但是如果对象没有实现 \_\_iter\_\_或\_\_next\_\_迭代器协议，Python的解释器就会去寻找\_\_getitem\_\_来迭代对象，如果连\_\_getitem\_\_都没有定义，这解释器就会报对象不是可迭代对象的错误.
- 魔法函数是能影响到语法本身的, 本来company是无法进行切片操作, 但是由于实现了\_\_getitem\_\_, 所以在python的语法上我们可以对实例化的对象进行切片操作.(列表也是list这个类实例化得到的一个对象)

```python
class Company(object):
    def __init__(self, employee__list):
        self.employee = employee__list
    # item将传入0、1、2...
    def __getitem__(self, item):
        return self.employee[item]
        
    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])

for em in company:  # __getitem__
    print(em)

for em in company[1:]:  # __getitem__
    print(em)

print(len(company))  # __len__
```



#### 三、鸭子类型

##### 什么是鸭子类型

当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子, 那么这只鸟就可以被称为鸭子.

在下面这段代码中, 所有的类实现了同一个方法, 这些类就可以归为同一种类型, 这样在调用的时候就可以都调用say方法, 从而实现了多态, 一种接口多种实现.

```python
class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a fish")

class Duck(object):
    def say(self):
        print("i am a duck")

animal_list = [Cat, Dog, Duck] # 类也是对象, 可以被添加到列表中, 而且python是动态语言, 对于变量不需要指定类型
for animal in animal_list:
    animal().say()
```

列表的extend

```python
def extend(self, iterable): # real signature unknown; restored from __doc__
    """ L.extend(iterable) -> None -- extend list by appending elements from the iterable """
```

list.extend()
因为传入的只需要是iterable类型即可, 所以list可以扩展tuple、set等都可以. 或者我们实现一个类可以迭代,也可以放到extend中. 

```python
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):   # 可迭代
        return self.employee[item]

company = Company(["tom", "bob", "jane"])

a = ["bobby1", "bobby2"]

a.extend(company)
print(a)
```

我们在几个对象中都实现了某一个方法名, 这些类我们就可以通用, 比如上面的say和\_\_getitem\_\_, 而魔法函数也是利用的python的鸭子类型, 只要实现了\_\_getitem\_\_就可迭代, 就可以传入extend中. 



#### 四、抽象基类

- 抽象基类是一个虚拟的类, 相当于一个模板, 定义一些方法, 所有继承这个基类的类必须覆盖抽象基类里面的方法
- 抽象基类是无法用来实例化的

##### 为什么要有抽象基类

因为python是基于鸭子类型的, 所以其实只要实现某些方法就可以了, 那为什么还要抽象基类呢?



##### 第一种应用场景法:检查某个类是否有某一种方法

某些情况之下希望判定某个对象的类型：

1.可以使用`hasattr`判断是否实现某方法或者

2.使用`isinstance`(推荐)去判断一个类是否是指定的类型, `Sized`就是一个实现`__len__`的抽象基类.

```python
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["bobby1","bobby2"])
print(hasattr(com, "__len__"))

from collections.abc import Sized
print(isinstance(com, Sized))
>>> True

# Sized内部的类方法, 在调用isinstance(com, Sized)时cls就是Sized对象, C就是com对象,然后判断com对象有没有实现__len__方法.
@classmethod
def __subclasshook__(cls, C):
    if cls is Sized:
        return _check_methods(C, "__len__")
    return NotImplemented

# isinstance还会找到继承链去进行判断
class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A))
>>> True
```



##### 第二种应用场景法: 强制某个子类必须实现某些方法

假设实现一个web框架，集成Cache(redis、cache、memerycache)

需要设计一个抽象基类，指定子类必须实现某些方法

```python
# 模拟抽象基类, 只有在调用set方法的时候才会抛出异常
class CacheBase():
    def get(self, key):
        raise NotImplementedError
    def set(self, key, value):
        raise NotImplementedError

class RedisCache(CacheBase):
    def set(self, key, value):
        pass

redis_cache = RedisCache()
redis_cache.set("key", "value")

# 在初始化的时候就会去判断有没有重载基类的方法,没有就抛异常，使用abc模块,
import abc

class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    def set(self, key, value):
        pass
    def get(self, key):
        pass

redis_cache = RedisCache()
```

##### collection.abc模块

在这个模块中定义了很多通用的抽象基类, 比如Sized. 但是这些抽象基类定义出来并不是用来继承的, 更多的是让我们理解接口的一些定义. 推荐使用鸭子类型或者多继承(Mixin)实现, 而少用抽象基类.

```python
__all__ = ["Awaitable", "Coroutine",
           "AsyncIterable", "AsyncIterator", "AsyncGenerator",
           "Hashable", "Iterable", "Iterator", "Generator", "Reversible",
           "Sized", "Container", "Callable", "Collection",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",
           "ByteString",
           ]

声明抽象基类

- metaclass = abc.ABCMeta
- @abc.abstractmethod

```



#### 五、类变量和实例变量

```python
class A:
    aa = 1 # 类变量
    def __init__(self, x, y):
        self.x = x # 实例变量
        self.y = y

a = A(2,3)

A.aa = 11 # 会将类A内存中的的aa修改为11
a.aa = 22 # 会在实例a内存中创建新的属性aa赋值22, 类A内存中的aa还是11
print(a.x, a.y, a.aa) # a.aa首先会去实例a的内存中找是否有aa, 如果没有再去类A的内存中找
print(A.aa) # 去类A的内存中找aa, 值为11

b = A(3,5)
print(b.aa) # 类A内存中aa已经修改为11

>>> 2 3 22
>>> 11
>>> 11
```

#### 六、属性查找算法（MRO算法）

##### 为什么不单纯使用深度优先或者广度优先

- 深度优先搜寻

查找顺序是A->B->D->C, 但是如果C重载了D的某个方法(B没有重载该方法), 由于深度优先所以将会使用D中的方法, 这是不合理的

![](http://qiniu.rearib.top/FoNwbOtk2Lb9gNBfQMbTk3SQYP8G)

- 广度优先

查找顺序是A->B->C->D->E, 由于优先级关系, B和D的优先级高于C, 但是如果C和D中定义了同一个方法, 由于广度优先所以将会使用C中的方法, 这是不合理的

![](http://qiniu.rearib.top/Fg5VSJjYJjJRJrVawHIfj8PoawGm)

##### C3算法

```python

class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)
>>> (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)





class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)
>>> (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)


```

#### 七、super真正调用的是什么?

super真正调用的是MRO中的下一个类的函数

```python
class A:
    def __init__(self):
        print ("A")

class B(A):
    def __init__(self):
        print ("B")
        super().__init__()

class C(A):
    def __init__(self):
        print ("C")
        super().__init__()
        
class D(B, C):
    def __init__(self):
        print ("D")
        super(D, self).__init__()

if __name__ == "__main__":
    print(D.__mro__)
    d = D()

>>> (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
D
B
C
A
```



#### 八、Mixin继承模式

##### Mixin类

- Python是支持多继承的。我们可以利用 Python 的这种特性，实现一种叫做 Mixin 的类

- **Mixin 类只包含了一组特定的函数集合，而我们将会将其与其他类进行混合，从而生成一个适用于实际需要的新类**

##### Mixin模式特点

1. Mixin类功能单一
2. 不和基类关联，可以和任意基类组合， 基类可以不和mixin关联就能初始化成功
3. 在mixin中不要使用super这种用法



#### 九、上下文管理器

异常捕捉中的return

```python
def exe_try():
    try:
        print ("code started")
        raise KeyError
        return 1 # 不会被执行
    except KeyError as e:
        print ("key error")
        return 2 # 压入堆栈
    else:
        print ("no error")
        return 3
    finally:
        print ("finally")
        return 4 # 压入堆栈, 最后取出栈顶

print(exe_try())

输出:
    code started
    key error
    finally
    4  # 不是输出2, 而是4
```

##### 上下文管理器协议

上下文管理器协议： 实现了_\_enter\_\_、\_\_exit__  方法的类

with语句后面的as得到的是__enter__方法的返回值, 如果`__enter__`返回1, 那么sample就等于1. 

```python
class Sample:
    def __enter__(self):
        # 获取资源
        print ("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        #释放资源
        print ("exit")
    def do_something(self):
        print ("doing something")

with Sample() as sample:
    sample.do_something()

输出:
    enter
    doing something
    exit
    
如果__enter__没有返回值, 那么无法使用as.

class Person:
    def __enter__(self):  # 获取资源
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):  # 释放资源
        print("exit")

    def said(self):
        print("said")


with Person() as P:
    P.said()

>>> AttributeError: 'NoneType' object has no attribute 'said'
```



##### contextlib简化上下文管理器

contextmanager可以简化上下文管理器，不需要我们编写`__enter__`和`__exit__`函数。他给了我们一个机会，让我们把之前一个不是上下文管理器的类变成一个上下文管理器，而不需要我们去修改这个类的源代码. 

其中的yield的作用，是中断当前函数执行流程，先去执行yield出去的部分的代码执行流程

```python
import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print ("file open")
    yield 
    print ("file end")

with file_open("bobby.txt") as f_opened:
    print ("file processing")

输出:
    file open
    file processing
    file end
```



#### 十、序列类型

序列类型的协议： 实现“Sequence”, “MutableSequence”的抽象方法

和容器相关的数据结构的抽象基类都在from collections import abc这个模块，我们打开from _collections_abc import all，在_collections_abc.py模块里面可以看到内容如下：



```python
__all__ = ["Awaitable", "Coroutine",
           "AsyncIterable", "AsyncIterator", "AsyncGenerator",
           "Hashable", "Iterable", "Iterator", "Generator", "Reversible",
           "Sized", "Container", "Callable", "Collection",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",
           "ByteString",
           ]

# 咱们只需要关注“Sequence”, “MutableSequence”, Sequence 是不可变序列类型，MutableSequence 是可变序列类型

'''
1、Sequence
'''
# 
# Sequence 继承的类
# 继承了两个类 Reversible, Collection
# Reversible是序列的翻转，例如ABC变成CBA

class Sequence(Reversible, Collection):
    # 抽象方法的标识，如果用他必须重写这个方法    
    @abstractmethod   

    
class Collection(Sized, Iterable, Container):   
    # Sized里面有魔法函数__len__,可以计算序列的长度
    # Iterable是个迭代对象, 有了它可以进行for循环
    # Container里面有魔法函数__contains__，我们就可以用in这个字段，例如 if i in list()   

    __slots__ = ()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Collection:
            return _check_methods(C,  "__len__", "__iter__", "__contains__")
        return NotImplemented
    
    
#　 Sequence的所有魔法函数构成了序列的协议,	打开Sequence类我们可以看到里面重写了所继承的抽象基类的方法,包括__len__,__iter__和__contains__.





'''
2、MutableSequence
MutableSequence是可变的序列, 他继承了Sequence并新加了一些特性. 如
setitem, delitem, insert, append, clear, reverse, extend, pop, remove, iadd等, 这些都是可变序列的特性.
'''

class MutableSequence(Sequence):

    __slots__ = ()

    """All the operations on a read-write sequence.

    Concrete subclasses must provide __new__ or __init__,
    __getitem__, __setitem__, __delitem__, __len__, and insert().

    """

    @abstractmethod
    def __setitem__(self, index, value):
        raise IndexError

    @abstractmethod
    def __delitem__(self, index):
        raise IndexError

    @abstractmethod
    def insert(self, index, value):
        'S.insert(index, value) -- insert value before index'
        raise IndexError
```

##### 序列协议实例

```python
'''
序列的+、+=和extend的区别
'''
# 区别一: + 和 +=占用空间不一样
a=[1,2,3]
b=[4,5,6]

c=a+b
print(c) # c是产生的新的list

a+=b
print(a) # a还是原来那个list


# 区别二: + 两边的数据类型要一致
# 原因是因为+=是调用MutableSequence中的__iadd__, 它是调用extend, 接收一个iterable并通过for循环append.
a=[1,2,3]
b=(4,5,6)

a+=b
print(a) # a = [1, 2, 3, 4, 5, 6]

c=a+b

# TypeError: can only concatenate list (not "tuple") to list
print(c) 




'''
entend和append的区别
'''
a=[1,2,3]
b=(4,5,6)

a.extend((9,10)) # 利用for循环内的append进行连接
print(a)

a.append(b) # 直接连接的是整体不会拆开合并
print(a)

输出:
    [1, 2, 3, 9, 10]
    [1, 2, 3, 9, 10, (4, 5, 6)]
```



##### 自定义序列类

```python
'''
序列切片操作
切片神操作，你会多少?

首先先讲下切片的公式, 模式[start : end : step]

1. start是切片的起始位置, 不填默认为0
2. end是切片的截至位置, 不填默认为列表的长度
3. step是切片的跨度, 也就是切片跳跃的长度，官方说法是步长，如果不指定值就是默认是1

切片取值

- 对列表进行切片操作是会返回一个新的列表

'''

alist=[1,2,3,4,5,6,7,8,9]
print(alist[::])    # 打印全部
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(alist[:])     # 打印全部
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(alist[::-1])  # 对列表进行反转
>>> [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(alist[1::2])  # 取奇数
>>> [2, 4, 6, 8]

print(alist[::2])   # 取偶数
>>> [1, 3, 5, 7, 9]

print(alist[1:4])   # 取列表位置1到4(不包括4的位置)
>>> [2, 3, 4]

print(alist[1:100]) # 如果截至位置大于列表长度取列表的长度。
>>> [2, 3, 4, 5, 6, 7, 8, 9]

print(alist[100:])  # 如果起始位置大于列表长度取值为空
>>> []



# 切片赋值
alist=[1,2,3,4,5,6,7,8,9]
print(len(alist))         # 打印长度
>>> 9

print(alist[0])           # 取第0个元素
>>> 1

alist[len(alist):]=[10]   # 在尾部增加列表
alist[:0]=[0]             # 在开始位置前增加列表
print(alist)
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(alist[2:2])         # 空值
>>> []

alist[2:2]=[3.3]          # 在第3位置插入列表
print(alist)
>>> [0, 1, 3.3, 2, 3, 4, 5, 6, 7, 8, 9, 10]

alist[:8]=[12]             # 前8个元素全变成[12]
print(alist)
>>> [12, 7, 8, 9, 10]

alist[2:]=[13]             # 从第三个位置到结尾变成[13]
print(alist)
>>> [12, 7, 13]

alist=[1,2,3,4,5,6,7,8,9]
alist[::2]=[0]*5           # 偶数前5个为修改成0, 左边要修改的数量和右边的数量要相等,如果不等就报错
print(alist)
>>> [0, 2, 0, 4, 0, 6, 0, 8, 0]

alist=[1,2,3,4,5,6,7,8,9]
alist[:3]=[]               # 删除前三个元素
print(alist)
>>> [4, 5, 6, 7, 8, 9]

del alist[:3]              # 用del删除前三个
print(alist)
>>> [7, 8, 9]

alist=[1,2,3,4,5,6,7,8,9]
del alist[::2]             # 奇数位置都要删除
print(alist)
>>> [2, 4, 6, 8]
```



##### 编写一个不可变的序列类

之前提到的`Sequence`就是一个不可变序列的抽象基类, 所以我们只要实现了它内部的魔法函数, 就能实现一个不可变的序列类.

```python
from collections import Sequence

class Group(Sequence):
    def __init__(self, group_name, staffs):
        self.group_name = group_name
        self.staffs = staffs

    def __getitem__(self, item):
        pass

    def __len__(self):
        return len(self.staffs)

group = Group(group_name='user', staffs=['rib1', 'rib2', 'rib3'])

print(group[1])

# 首先根据源码可知我们必须实现__getitem__和__len__, 我们来好好研究一下__getitem__这个魔法函数.
#　如果是group[1], 那么item是int(1), 如果group[:2], 那么item是一个slice(None, 2, None), 所以我们可以通过item进行切片返回.

def __getitem__(self, item):
    return self.staffs[item]

#　但是如果想返回的还是Group对象:
def __getitem__(self, item):
	return Group(group_name='user',staffs = self.staffs[item])

# 但是Group直接写死了不好, 因为是通过group调用, 所以self指向group对象, 而且传入的是int的时候我们需要返回[]:
def __getitem__(self, item):
    cls = type(self)
    if isinstance(item, slice):
        return cls(group_name='user',staffs = self.staffs[item])
    if isinstance(item, int):
        return cls(group_name='user',staffs = [self.staffs[item]])
    

# 同理我们如果还需要实现其他功能:
    def __reversed__(self):
        self.staffs.reverse()

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

>>> reversed(group)
>>> print('rib1' in group)
```

#### 十一、元类编程

##### 1、property装饰器(属性方法)

```python
class Student:
    def __init__(self, name):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if isinstance(age,int):
            if 0<age<120:
                self._age=age
        else:
            print("请输入合法的年龄")

stu=Student("Lady")
stu.age=10
print(stu.age)

1. get和set的方法名称都要一样（age）
2. set方法返回的属性前面加个"_"
3. @property是针对get方法
4. @age.setter是针对set方法，是@property本身又创建了另一个装饰器
5. 直接可以这样stu.age=10对象名.方法名进行赋值，
6. 只定义getter方法，不定义setter方法是一个只读属性
```

##### 2、getattr__和__getattribute__的区别

\__getattr__:   当实例化对象调用属性不存在的时候调用

_\_getattribute__:  无条件进入该魔法函数, 即使所查找的属性不存在

```python
class A:
    def __init__(self):
        pass

a=A()
print(a.age)
# >>> AttributeError: 'A' object has no attribute 'age'

    
    
class A:
    def __init__(self):
        pass
    def __getattr__(self, item):
        print("即使你没有属性也不会报错")

a=A()
print(a.age)
# >>> 即使你没有属性也不会报错
# >>> None
    
# 当实例化对象调用属性不存在的时候调用

# 作用: 我们可以指定在找不到该属性的时候实现的操作, 比如修改查找的名称, 重新指定查找的区域等

__getattribute__

执行查找, 无条件进入该魔法函数, 即使所查找的属性不存在

```



##### 3、属性描述符

前面提到的age在输入的时候需要校验, 实现是通过property的setter, 但是如果很多输入字段那么就要写很多重复的代码.这里就要用到属性描述符

```python
# 一个对象只要实现__get__、__set__或者__delete__就是一个属性描述符对象
class IntField:
    # 数据描述符
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value
    def __delete__(self, instance):
        pass

class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value

class User:
    age = IntField() # age本来是个对象，放在类里当作了User类属性

user = User()
user.age = 12 # 会进入IntField的__set__

instance
>>> <__main__.User object at 0x00000259359F9128>
self
>>> <__main__.IntField object at 0x00000259359F9E48>
```

###### user.age的查找顺序

- 如果user是某个类的实例，那么`user.age`（以及等价的`getattr(user,’age’)`）
- 首先调用`__getattribute__`, 如果在`__getattribute__`找不到属性就会抛出`AttributeError`
- 如果类定义了`__getattr__`方法，在抛出`AttributeError`的时候就会调用到`__getattr__`
- 而对于描述符`__get__`的调用，则是发生在`__getattribute__`内部的。

user = User(), 那么user.age 顺序如下：

1. 如果“age”是出现在User或其基类的`__dict__`中，且age是data descriptor，那么调用其`__get__`方法
2. 如果“age”出现在user(对象)的`__dict__`中， 那么直接返回 `obj.__dict__[‘age’]`
3. 如果“age”出现在User(类)或其基类的`__dict__`中

- 如果age是non-data descriptor，那么调用其`__get__`方法
- 返回`__dict__[‘age’]`

4. 如果User有`__getattr__`方法，调用`__getattr__`方法，否则
5. 抛出AttributeError

- 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类.__dict__里的
- 对象.__dict__中存储了一些self.xxx的一些东西

```python
import numbers

class IntField:
    #数据描述符
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value
    def __delete__(self, instance):
        pass

class User:
    age = IntField()


if __name__ == "__main__":
    user = User()
    # user.age = 30           # 进入数据描述符的__set__
    # setattr(user, 'age',18) # 进入数据描述符的__get__
    # print(user.age)         # 进入数据描述符的__get__
    user.__dict__["age"] = 18
    print(user.__dict__["age"])

    user.__dict__["age"] = 18
    print(user.age)
    >>> 'IntField' object has no attribute 'value'
    

    
    
 class User:
    age = 1

if __name__ == "__main__":
    user = User()
    user.name = 30         # 保存在user对象的内存中
    print(user.name)       # 从user对象的内存中去取
    user.age = 30          # 保存在user对象的内存中, 不影响类的内存中的值
    print(user.age)       # 进入数据描述符的__get__
    user.__dict__["age"] = 18
    print(user.__dict__["age"])
    print (user.__dict__)
```



##### 4、new__和__init__魔法函数区别

- \_\_new\_\_的功能是在生成对象之前所做的动作, 接受的参数是cls 类
- \_\_init\_\_是在对象生成之后完善对象的属性, 它接受的是self 对象
- 对象生成是在new里面return(返回一个对象)

```python
class  User:
    def __new__(cls, *args, **kwargs):
        print("new")
        # return super().__new__(cls) 创建并返回一个类对象

    def __init__(self,name):
        self.name=name
        print("init")

user=User()
>>> new
print(type(user))
>>> <class 'NoneType'>
cls
>>> <class '__main__.User'>

# 在执行user = User时, 首先调用User类中的__new__, 其中cls就是User类, 然后继承父类object的中__new__将创建并返回一个类对象, 然后再执行__init__完善对象属性.
```



##### 5、创建类的方法

###### Type动态创建类

```python
Company=type（“类名称”，（继承的基类），{类的属性 }）

class Baseclass:
    def say(self):
        print("basecalss say")

# 要有self
def run(self):
    return "i am running"

Company=type("Company",(Baseclass, ),{"name":"ebaotech","Adress":"杨浦区","run":run})
co=Company()
print(co.name, co.Adress, co.run())
co.say()

>>> ebaotech 杨浦区 i am running
>>> basecalss say
```

**元类就是创建类的类, 刚才的type就是一个元类.**  type ==>  class(对象)  ==> 对象

##### 6、自定义元类

```python
1、

class Metaclass(type):
    def __new__(cls, *args, **kwargs):
        # 此时参数：cls, *args, **kwargs
        # "User",(),{}
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=Metaclass):
    pass



# 在User实例化的过程中， 先通过元类Metaclass创建User类对象(即__new__)， 此时可以做很多的检查，
# 比如有没有实现抽象方法，检查不通过可以抛异常
# 控制User类实例化的过程



# 2、自定义类的实例化过程
class Foo(Bar):
    pass

#　创建Foo会先寻找Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象。如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。

```



#####  通过元类实现orm

```python
import numbers

class Field:
    pass

class IntField(Field):
    # 数据描述符
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField(Field):
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        if max_length is None:
            raise ValueError("you must spcify max_lenth for charfiled")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        # BaseModel类的创建也是通过该元类, 但是不需要执行下面的内容
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        # 在attrs中有传入的参数, Meta等, 需要进行处理
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    # 在__new__中只是对参数进行处理, 并返回cls, 并没有赋给user对象
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    # 生成sql语句保存到数据库中
    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))

        sql = f"insert {self._meta['db_table']}({','.join(fields)}) value({','.join(values)})"
        pass

class User(BaseModel):
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=1, max_value=100)

    class Meta:
        db_table = "user"


if __name__ == "__main__":
    # user = User(name="bobby", age=28)
    user = User()
    user.name = "bobby"
    user.age = 28
    user.save()
```



#### 十二、迭代协议

可迭代协议： 实现`__iter__`方法（通常`__iter__`方法的类的实例叫做可迭代对象）

迭代器协议：实现`__iter__`和`__next__`（通常`__iter__`方法的类的实例叫做迭代器）

迭代器的作用：

1、迭代器是访问集合内元素的一种方式，一般用来遍历数据

2、迭代器提供了一种惰性方式数据的方式、可迭代对象调用`iter(a)`返回一个迭代器



##### 1、for循环机制

在调用for循环的时候会尝试调用`iter()`, 然后`iter()`首先会去找有没有`__iter__`, 如果有将返回一个迭代器, 如果没有将查看有没有`__getitem__`, 如果有将创建默认的迭代器使用`__getitem__`进行迭代输出

##### 2、自己实现一个迭代器

```python
from collections.abc import Iterator

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 可迭代对象中的__iter__返回迭代器
    def __iter__(self):
        return MyIterator(self.employee)

class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0 # 需要在内部维护一个取值位置

    # 继承了Iterator可以不写该方法, 如果重写那么return self
    # def __iter__(self):
    #     return self

    def __next__(self):
        #真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration # 抛出的异常应该是StopIteration
        self.index += 1
        return word
    
 
if __name__ == "__main__":
	company = Company(employee_list=['tom', 'bob', 'jane'])
    for item in company:
        print(item)
    
    # 根据设计模式的迭代模式，通常把迭代器和可迭代对象分开, 把维护取值放在迭代器中
```



##### 3、生成器

python中函数的工作原理

```python
def foo():
    bar()
def bar():
    pass

import dis
print(dis.dis(foo))

2           0 LOAD_GLOBAL              0 (bar)
            2 CALL_FUNCTION            0
            4 POP_TOP
            6 LOAD_CONST               0 (None)
            8 RETURN_VALUE
None
```

![](http://qiniu.rearib.top/FiCM74pMYvC5Xz3gPHcSVLs5SFZt)

- python的解释器会用`PyEval_EvalFramEx(C语言)`函数去执行我们的foo函数.
- 在运行foo函数的时候首先会创建一个栈帧(Stack frame), 这个栈帧是一个上下文, 也是一个对象.
- 栈帧会将foo函数变成一个字节码对象, 使用dis查看字节码
- 然后栈帧的上下文中去运行字节码(字节码是全局唯一的)

- 当foo调用bar, 又会创建一个新的栈帧, 然后运行bar的字节码
- 所有的栈帧都是分配在堆的内存上, 如果不释放会一直存在, 所以栈帧可以独立于调用者存在, 就比如调用者foo不存在也没关系, 只要指针指向bar的栈帧就可以控制

```python
import inspect
frame = None
def foo():
    bar()
def bar():
    pass
    global frame
    # 获取当前函数的栈帧并赋给全局变量frame
    frame = inspect.currentframe()

foo()
print(frame.f_code.co_name)
>>> bar
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)
>>> foo
```



![](http://qiniu.rearib.top/FvNYTPLMxcqeAfZruBN-2CoaHOKV)

python解释器会编译字节码, 如果发现有yeild, 就会标记该函数, 然后再调用的时候会返回一个生成器对象. 而这个生成器对象实际上是把这个frame对象做了一个封装

- 生成器可以在任何时候、任何函数中恢复运行，因为它的栈帧并不在真正的栈中，而是堆中
- f_lasti指向“最后执行指令”的指针。初始化为 -1，意味着它没开始运行



```python
'''
读取大文件
有一个文件 大概有500G，并且只有一行，行之间有分隔符，我们需要把文件内的数据一行一行的读取出来，然后写入数据库里面。
- file.read()
可以传入 int 参数，代表读取的字符数
'''

f = open('input.txt','r')

def myreadline(new_line):
    buf = ''
    while True:
        # 如果现在的缓存中有了分隔符, 取出前面的数据发送出去
        while new_line in buf:
            line_index = buf.index(new_line)
            yield buf[:line_index]
            # 去掉已经发送出去的数据并去掉分隔符
            buf = buf[line_index + len(new_line):]
            
        # 读取1024个字节数据并判断, 如果读到结尾那么把剩余buf发送出去并break
        check = f.read(1024)
        if not check:
            yield buf
            break
        buf += check


for i in myreadline('{|}'):
    print(i)

```



#### 十三、异步IO

##### 1、并发, 并行、同步，异步、 阻塞，非阻塞

```python
'''
并发：指一个时间段内，有几个程序在同一个cpu上运行，但是任意时刻只有一个程序在cpu上运行
并行：指任意时刻点上，有多个程序同时运行在多个cpu上

同步：指代码调用IO操作时，必须等待IO操作完成才返回的调用方式
异步：指代码调用IO操作时，不必等待IO操作完成才返回的调用方式

阻塞：指调用函数时候当前线程挂起
非阻塞：指调用函数时候当前线程不会被挂起，而是立即返回
'''
```



##### 2、IO多路复用

![1617639486980](F:\quhong\DEMO\python核心笔记\c10k.png)

![1617639601075](F:\quhong\DEMO\python核心笔记\io模型.png)

![1617639708981](F:\quhong\DEMO\python核心笔记\阻塞IO.png)

阻塞式IO弊端：cpu大量时间浪费在IO操作



![1617639957819](F:\quhong\DEMO\python核心笔记\非阻塞IO.png)

非阻塞式IO弊端：虽然非阻塞不消耗cpu，但是会不停的检查状态会消耗cpu



![1617640821375](F:\quhong\DEMO\python核心笔记\selectIO.png)



![1617640919045](F:\quhong\DEMO\python核心笔记\异步IO.png)



![1617641029468](F:\quhong\DEMO\python核心笔记\select_poll_epoll_IO.png)



![1617641068543](F:\quhong\DEMO\python核心笔记\select_IO.png)



![1617641177711](F:\quhong\DEMO\python核心笔记\poll_IO.png)

![1617641223820](F:\quhong\DEMO\python核心笔记\epoll_IO.png)

###### 非阻塞IO

```python
#通过非阻塞io实现http请求

import socket
from urllib.parse import urlparse


#使用非阻塞io完成http请求

def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    #建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80)) #阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    #不停的询问连接是否建立好， 需要while循环不停的去检查状态
    #做计算任务或者再次发起其他的连接请求

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass


    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    get_url("http://www.baidu.com")


```





###### select + 回调 + 事件循环

```python
#1. epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高， epoll比select
# 并发性不高，同时连接很活跃， select比epoll好

#通过非阻塞io实现http请求
# select + 回调 + 事件循环
#  并发性高
# 使用单线程

# 事件循环，不停的请求socket的状态并调用对应的回调函数
# 1. select本身是不支持register模式
# 2. socket状态变化以后的回调是由程序员完成的

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


selector = DefaultSelector()
#使用select完成http请求
urls = []
stop = False


class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        #注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    #事件循环，不停的请求socket的状态并调用对应的回调函数
    #1. select本身是不支持register模式
    #2. socket状态变化以后的回调是由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
    #回调+事件循环+select(poll\epoll)

if __name__ == "__main__":
    fetcher = Fetcher()
    import time
    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print(time.time()-start_time)

```



回调模式、同步编程、多线程处理IO的缺点：

1.回调模式（回调+事件循环+select(poll\epoll)） 编码复杂度高

2.同步编程并发性不高

3.多线程编程需要线程间同步，lock



最理想的方式：

1.采用同步的方式去编写异步的代码

2.使用单线程去切换任务

​	由于线程由操作系统调度切换的，单线程切换意味着我们需要程序员自己去调度任务

​	且不再需要锁，并发性高；如果单线程内切换函数，性能远高于线程切换，并发性更高