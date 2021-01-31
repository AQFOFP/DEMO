### 第一部分 Python基础篇（80题）

1. 为什么学习Python？

2. 通过什么途径学习的Python？

3. Python和Java、PHP、C、C#、C++等其他语言的对比？

4. 简述解释型和编译型编程语言？

5. Python解释器种类以及特点？

6. 位和字节的关系？

7. b、B、KB、MB、GB 的关系？

8. 请至少列举5个 PEP8 规范（越多越好）。

   答：

   1.   每一级缩进使用4个空格 

   2.  空格是首选的缩进方式 

   3.  所有行限制的最大字符数为79 

   4.  顶层函数和类的定义，前后用两个空行隔开 

   5.  类里的方法定义用一个空行隔开 

   6. 导入通常在分开的行，例如：

      推荐: import os
           	import sys

   7.  模块应该用简短全小写的名字 

   8.  类名一般使用首字母大写的约定 

   9.  函数名应该小写，如果想提高可读性可以用下划线分隔 

   

9. 通过代码实现如下转换：

   二进制转换成十进制：v = “0b1111011” 
   十进制转换成二进制：v = 18 
   八进制转换成十进制：v = “011” 
   十进制转换成八进制：v = 30 
   十六进制转换成十进制：v = “0x12” 
   十进制转换成十六进制：v = 87

10. 请编写一个函数实现将IP地址转换成一个整数。

   如 10.3.9.12 转换规则为：

   ​    10      00001010

         3      00000011 

   ​     9      00001001

        12      00001100 

   再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？

11. python递归的最大层数？

    答：

    1. 在window上的最大递归层数是998

       可以通过sys.setrecursionlimit()进行设置,但是一般默认不会超过3925-3929这个范围

12. 求结果：
      v1 = 1 or 3      1
      v2 = 1 and 3    1
      v3 = 0 and 2 and 1   0
      v4 = 0 and 2 or 1    1
      v5 = 0 and 2 or 1 or 4   1
      v6 = 0 or Flase and 1   Flase

13. ascii、unicode、utf-8、gbk 区别？

    ascii
    8位一个字节,1个字节表示一个字符.即: 2 ** 8 = 256,所以ASCII码最多只能表示256个字符.

    unicode
    俗称万国码,把所有的语言统一到一个编码里.解决了ascii码的限制以及乱码的问题.
    unicode码一般是用两个字节表示一个字符,特别生僻的用四个字节表示一个字符.

    utf-8
    新的问题出现了,如果统一成unicode编码,乱码问题从此消失了.但是如果你写的文本基本上都是英文的,
    用Unicode编码比ascii编码需要多一倍的存储空间,在存储和传输上十分不方便.
    utf-8应用而生,它是一个"可变长的编码方式",如果是英文字符,则采用ascii编码,占用一个字节.
    如果是常用汉字,就占用三个字节,如果是生僻的字就占用4~6个字节.

    gbk
    国内版本,一个中文字符 == 两个字节 英文是一个字节

    

14. 字节码和机器码的区别？

    答：

    1.  机器码就是计算机可以直接执行，并且执行速度最快的代码 
    2. 字节码是一种中间码，它比机器码更抽象，需要直译器转译后才能成为机器码的中间代码

15. 三元运算规则以及应用场景？

    答：

     三元运算符就是在赋值变量的时候，可以直接加判断，然后赋值格式 

     res = 值1 if 条件 else 值2  

    如：

     a = 6 if True else 5 

    

16. 用一行代码实现数值交换：
        a = 1
        b = 2

   ​	a, b = b, a

17. Python3的数据类型？

    答：

    Python3 的六个标准数据类型中：

    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

    

    Python3 支持 **int、float、bool、complex（复数）**。

    在Python 3里，只有一种整数类型 int，表示为长整型long，没有python2的long类型

    

18. 列举布尔值为False的常见值？

    0、[]、()、{}、None

    

19. 字符串、列表、元组、字典每个常用的5个方法？

  

20. 两个列表并成字典

    l1 = ['a','b','c','d'] , l2 = [1,2,3,4]

    dict(zip(l1,l2))

      

21. lambda表达式格式以及应用场景？

     lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数 

     add = lambda x, y : x+y

     

22. pass的作用？

    答：

    pass是空语句，是为了保持程序结构的完整性。

    pass 不做任何事情，一般用做占位语句

    

23. *arg和**kwarg作用

     允许我们在调用函数的时候传入多个位置参数和关键字参数

     *arg：元组或列表“出现”
     **kwarg：字典“出没”

     

24. is和==的区别

    答：

     ==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等 

     is也被叫做同一性运算符，这个运算符比较判断的是对象间的唯一身份标识，也就是id是否相同 

    

25. 简述Python的深浅拷贝以及应用场景？

    深浅拷贝用法来自copy模块。

    导入模块：import copy

    浅拷贝：copy.copy

    深拷贝：copy.deepcopy

    　　对于 数字 和 字符串 而言，赋值、浅拷贝和深拷贝无意义，因为其永远指向同一个内存地址

    

26. Python垃圾回收机制？

    答：简单的回答：以引用计数器为主，标记清除和分代回收为辅

    首先在Python中维护了一个refchain的双向环状链表，这个链表中存储程序创建的所有对象，每种类型的对象中都有一个ob_refcnt引用计数器的值，引用个数+1、-1，最后当引用计数器变为0时会进行垃圾回收（对象销毁、refchain中消除）

    

    但是，在python中对于那些有多个元素的对象可能存在循环引用的问题，为了解决这个问题python又引入了标记清除和分代回收，即在其内部有4个链表

    - refchain
    - 0代   700个对象
    - 1代    10次
    - 2代    10次

    在源码内部当达到各自的阀值时，就会触发扫描链表进行标记清除的动作（有循环则计数器各自-1）

    

27. Python的可变类型和不可变类型？

    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

    

    

28. 求结果：
    ![img](https://images2018.cnblogs.com/blog/425762/201805/425762-20180523191729906-771120081.png)

    答：[6, 6, 6, 6]

29. 列举常见的内置函数？

    abs()、all()、any()、eval()、float()

    list()、tuple()、dict()、set()、str()

    id() 、isinstance() 与 type() 、len()、range()

    

30. filter、map、reduce的作用？

    1. map是用同样方法把所有数据都改成别的..字面意思是映射

       map(lambda x:x*x,[0,1,2,3,4,5,6])        #  [0, 1, 4, 9, 16, 25, 36]

       

    2. reduce是用某种方法依次把所有数据丢进去最后得到一个结果

       reduce(lambda x,y:x+y,[0,1,2,3,4,5,6])    # 21

       

    3. filter是筛选出其中满足某个条件的那些数据..字面意思是过滤

       filter(lambda x:x&1,[0,1,2,3,4,5,6])    # [1, 3, 5]

       

31. 一行代码实现9*9乘法表

    print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

    

32. 如何安装第三方模块？以及用过哪些第三方模块？

    在Python中，安装第三方模块，是通过setuptools这个工具完成的。Python有两个封装了setuptools的包管理工具：easy_install和pip。目前官方推荐使用pip

    

33. 至少列举8个常用模块都有那些？

    math、requests、urllib、functiontools、re、time、datetime、json、lxml、os

    

34. re的match和search区别？

    match()函数只检测RE是不是在string的开始位置匹配，search()会扫描整个string查找匹配；

    

35. 什么是正则的贪婪匹配？

    1、贪婪匹配

    总是尝试匹配尽可能多的字符

    

    2、非贪婪匹配

    是尝试匹配尽可能少的字符

    

36. 求结果：  

    a. [ i % 2 for i in range(10) ]    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

    b. ( i % 2 for i in range(10) )   # 生成器对象

37. 求结果： 

     a. 1 or 2      # 1

     b. 1 and 2   #  2

     c. 1 < (2==2)    # Flase

     d. 1 < 2 == 2   # TRUE  

     

38. def func(a,b=[]) 这种写法有什么坑？

    答：

    ```
    def func(a,b=[]):
        b.append(a)
        print(b)
    func(1)
    func(1)
    func(1)
    func(1)
    
    
     [1]
     [1, 1]
     [1, 1, 1]
     [1, 1, 1, 1]
    ```

     当第一次执行的时候实例化了一个list，第二次执行还是用第一次执行的时候实例化的地址存储 

    

39. 如何实现 “1,2,3” 变成 [‘1’,’2’,’3’] ?

    a = "1,2,3"

    b = a.split(',')

    

40. 如何实现[‘1’,’2’,’3’]变成[1,2,3] ?

    a = [‘1’,’2’,’3’]

    b = [int(i) for i in a]

    

41. 比较： a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 c = [(1,),(2,),(3,) ] 的区别？

    a与b相等     a==b  True

    a == c  False

    

42. 如何用一行代码生成[1,4,9,16,25,36,49,64,81,100] ?

    a = [i**2 for i in range(1, 11)]

    

43. 一行代码实现删除列表中重复的值 ?

    a = [1, 3, 1, 4, 3, 5, 1]

    b = list(set(a))

    

44. 如何在函数中设置一个全局变量 ?

    def func():

    ​    global   b = 6

    

45. logging模块的作用？以及应用场景？

    ```python
    # 日志模块
    
    import logging
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    logger.debug("Do something 调试信息")   # 调试信息
    logger.info("Start print log 普通信息")  # 普通信息
    logger.warning("Something maybe 警告")  # 警告
    logger.error("error 错误")  # 错误信息
    logger.critical("critical 致命错误")  # 致命错误
    ```

    

46. 请用代码简答实现stack 。

    ```python
    # 栈的特点：先进后出
    
    class Stack(object):
        def __init__(self):
            self.stack = []
    
        def push(self, value):    # 进栈
            self.stack.append(value)
    
        def pop(self):  #出栈
            if self.stack:
                self.stack.pop()
            else:
                raise LookupError('stack is empty!')
    
        def is_empty(self): # 如果栈为空
            return bool(self.stack)
    
        def top(self): 
            #取出目前stack中最新的元素
            return self.stack[-1]
    ```

    

47. 常用字符串格式化哪几种？

    ```python
    print('hello %s and %s'%('df','another df'))
    print('hello %(first)s and %(second)s'%{'first':'df' , 'second':'another df'})
    print('hello {first} and {second}'.format(first='df',second='another df'))
    ```

    

48. 简述 生成器、迭代器、可迭代对象 以及应用场景？

      

    可迭代对象：

     实现了迭代器协议的对象就是可迭代对象(实现方式是,实现**iter**方法) 

    实现了iter方法，可以使用for进行遍历的是可迭代对象

    

    迭代器：

    就是实现了iter() 和 next()方法的对象.其中iter()返回迭代器本身,而next()返回容器的下一个元素,在结尾处引发StopInteration异常.

    迭代器的优点:省内存.它是一种通过延时创建的方式生成一个序列,只有在需要的时候才被创建.

    

    生成器：

    在Python中，这种一边循环一边计算的机制，减少内存的消耗， 称为生成器，生成器是通过yield语句进行实现

    数据库中有非常大的数据，可以使用生成器返回给浏览器

    

    Python有两种不同的方式提供生成器:
    生成器表达式、 生成器函数 

    

49. 用Python实现一个二分查找的函数。

    ```python
    def BinarySearch(arr,num):
        l,r = 0, len(arr)-1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == num:
                return mid
            elif arr[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    ```

    

50. 谈谈你对闭包的理解？

    答：

    在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用

    这样就构成了一个闭包。

    特点：

    一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，就把这个临时变量绑定给了内部函数，然后自己再结束。

    

51. os和sys模块的作用？

    答：

    os:这个模块提供了一种方便的使用操作系统函数的方法。

    sys:这个模块可供访问由解释器使用或维护的变量和与解释器进行交互的函数。

    　　总结:os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境

    

52. 如何生成一个随机数？

    random.random()   # [0, 1)  伪随机数

    

53. 如何使用python删除一个文件？

    ```python
    import os
    my_file = 'D:/text.txt' # 文件路径
    if os.path.exists(my_file): # 如果文件存在
        #删除文件，可使用以下两种方法。
        os.remove(my_file) # 则删除
        #os.unlink(my_file)
    else:
        print('no such file:%s'%my_file)
    ```

    

54. 谈谈你对面向对象的理解？

    ```
    封装、继承、多态
    ```

    

55. Python面向对象中的继承有什么特点？

    ```
    继承的特点：
    
    1、在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。有别于C#
    
    2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
    
    3、Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找
    ```

    

    

56. 面向对象中super的作用？

    ```
    super() 函数是用于调用父类(超类)的一个方法。
    
    super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
    
    MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表
    ```

    

57. 类的菱形继承

    ```python
    class A:
        def run(self):
            print('---A---')
    
    class B(A):
        def run(self):
            super().run()
            print('---B---')
    
    class C(A):
        def run(self):
            super().run()
            print('---C---')
    
    class D(B, C):
        def run(self):
            super().run()
            print('---D---')
    
    d = D()
    d.run()
    
    print(D.__mro__)   # 继承关系
    
    '''
    ---A---
    ---C---
    ---B---
    ---D---
    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    '''
    ```

    

58. Mixin继承

    ```python
    class A:
        def run(self):
            print('A')
    
    
    class B:
        def run(self):
            super().run()
            print('B')
    
    class C:
        def run(self):
            super().run()
            print('C')
    
    
    class D(B, C, A):
        def run(self):
            super().run()
            print('D')
    
    d = D()
    d.run()
    print(D.__mro__)
    
    '''
    A
    C
    B
    D
    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    '''
    ```

    

59. 用于模块导入限制

    ```python
    # 文件  a.py
    
    __all__ = ('a', 'e', '_d')   # 用于模块导入时限制， 其他模块只能导入里面的
    
    a = 123
    _b = 456
    c = 'asdfghjkl'
    _d = [1,2,3,4,5,6]
    e = (9,8,7,6,5,4)
    
    
    # 文件 b.py
    from a import *
    print(a)
    print(_b)  # 报错
    print(c)   # 报错
    print(_d)
    print(e) 
    ```

    

60. 是否使用过functools中的函数？其作用是什么？

    ```python
    functools.partial(func, 32)  # 给函数传递一个固定值
    functools.wraps  # 使装饰器修饰的函数名不变
    ```

    

61. 列举面向对象中带下划线的特殊方法，如：\_\_new\_\_、\_\_init\_\_

    ```
    __str__ 、__dict__
    __new__ 、__metaclass__
    
    
    class Foo(object):  
        def __init__(self, name, age):  
            self.name = name  
            self.age = age  
      
    foo = Foo("UserPython", 17)  
      
    print(Foo.__dict__) #打印类里的所有属性，不包括实例属性  
    print(foo.__dict__) #打印所有实例属性，不包括类属性
    ```

    

62. 如何判断是函数还是方法？

    ```python
    如果不在类里定义的明显是函数[Function]
    
    在类里定义的，如果是使用对象调用的形式为方法[Method]  obj.display
    使用类名调用的是函数[Function] Foo.display
    ```

    

63. 静态方法和类方法区别？

    ```python
    实例方法:
        定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
       
    类方法:
        定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
       
    
    静态方法:
        定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    
    实例方法，类方法，静态方法都可以通过实例或者类调用，只不过实例方法通过类调用时需要传递实例的引用    
    三种方法从不同层次上来对方法进行了描述：实例方法针对的是实例，类方法针对的是类，而静态方法可以认为是全局函数，不能使用类的属性和方法，他们都可以继承和重新定义，  
       
    
    ```

    

64. 列举面向对象中的特殊成员以及应用场景

    ```python
    __new__、__init__、__str__ 、__dict__
    __new__ 、__metaclass__
    
    __new__ 和 __init__ 的区别
    
    这两个方法的主要区别在于：__new__ 负责对象的创建， 而 __init__ 负责对象的初始化
    __new__ 是在我们调用类名进行实例化时自动调用的，__init__ 是在这个类的每一次实例化对象之后调用的，__new__ 方法创建一个实例之后返回这个实例对象并传递给 __init__ 方法的 self 参数
    
    
    
    class A(object):
        def __new__(cls):
            print("A.__new__ called")
            return 29
    
    
    if __name__ == '__main__':
        a = A()
        print(a, type(a))  # 29 <class 'int'>
        
    
        
        
        
    class B():
        def __init__(self,*args, **kwargs):
            print("init B")
    
        def __new__(cls, *args, **kwargs):
            print("new B %s"%cls)
            return super().__new__(cls, *args, **kwargs)
        
    if __name__ == '__main__':
        b = B()
        print(b, type(b))  # <__main__.B object at 0x0000000002097588> <class '__main__.B'>
            
    ```

    

65. 什么是反射？以及应用场景？

    ```python
    '''
    8.反射
    反射是一个很重要的概念，它可以把字符串映射到实例的变量或者实例的方法然后可以去执行调用、修改等操作
    它有四个重要的方法：
    getattr 获取指定字符串名称的对象属性
    setattr 为对象设置一个对象
    hasattr 判断对象是否有对应的对象（字符串）
    delattr 删除指定属性
    '''
    
    def test(request):
    	from app01 import models
    
    	list_display = ['id','title']
    	
        # 通过模型的_meta获取模型的字段，再通过字段获取字段的属性
    	header_list = []
    	for name in list_display:
    		header_list.append(models.UserInfo._meta.get_field(name).verbose_name)
    	print(header_list)
    
        # 通过反射获取指定显示的列
    	user_queryset = models.UserInfo.objects.all()
    	for item in user_queryset:
    		row = []
    		for field in list_display:
    			row.append(getattr(item,field))
    		print(row)
    
    	return HttpResponse('...')
    ```

    

66. metaclass作用？以及应用场景？

    ```
    https://www.liaoxuefeng.com/wiki/897692888725344/923030550637312
    ```

    

67. 用尽量多的方法实现单例模式。

    ```python
    # 一个模块就是一个单例模式
    # zhaosen.py
    class AdminSite(object):
    
        def __init__(self):
            self._registry = {}
    
    obj1 = AdminSite()
    ```

    ```python
    import threading
    class Singleton(object):
        _lock = threading.Lock()
    
        def __init__(self):
            pass
    
        def __new__(cls, *args, **kwargs):
            if not hasattr(Singleton, "_instance"):
                with Singleton._lock:
                    if not hasattr(Singleton, "_instance"):
                        Singleton._instance = super().__new__(cls)  
            return Singleton._instance
    
    ```

    

68. 装饰器的写法以及应用场景。

    ```python
    '''
    装饰器：
    在代码运行的期间动态的增加功能的方式我们称之为装饰器。
    '''
    
    '''
    1、最简单的装饰器：
    
    def outer(func):
        def inner():
            #增强的功能
            #在内函数中执行func函数
            return func()
        return inner
    
    在装饰器中，分为外函数与内函数：
    外函数（outer）：
    1.将被装饰的函数传递进来--》func
    2.将装饰好的函数返回给调用者 --》inner
    内函数：
    1.添加动态增加的功能
    2.执行被装饰的函数
    
    内函数中return什么时候可以省略？
    注意：当被装饰的函数没有返回值的时候，内函数的return可以省略，
    若被装饰的函数中存在返回值，则内函数的return则不能省略。
    
    @装饰器
    def func():
        pass
    
    @的功能：将被装饰的函数的函数名作为参数传递给外函数，将外函数返回的
    替代版的函数赋值给原本的函数。
    '''
    def outer(func):
        def inner():
            print("*********")
            # print("*********")
            return func()
        return inner
    
    
    @outer
    def now():
        print("2019-6-13")
        return True
    
    # now = outer(now)
    # 调用
    print(now())
    '''
    *********
    2019-6-13
    True
    '''
    
    
    '''
    2、有参数的情况下
    def outer(func):
        def inner(参数列表):
            #添加增加的功能
            return func(参数列表)
        return inner
    
    注意：
    1.使用内函数来接收被装饰函数的参数
    2.调用被装饰的函数的时候，需要将参数传递进去。
    '''
    
    def outer(func):
        def inner(age):
            if age>=0 and age<=160:
                func(age)
            else:
                print("年龄有误")
        return inner
    '''
    使用装饰器，给函数添加一个对年龄的限制：
    年龄[0,160]
    '''
    @outer
    def getAge(age):
        print("您的年龄为%d"%age)
        
    getAge(-100)  # 年龄有误
    getAge(100)  # 您的年龄为100
    getAge(200)  # 年龄有误
    
    
    # 3、通用装饰器
    
    def outer(func):
        def inner(*args, **kwargs):
            # 添加修改的功能
            print("&&&&&&&&&&&&&")
            func(*args, **kwargs)
        return inner
    
    
    @outer # say = outer(say)
    def say(name, age): # 函数的参数力理论上是无限制的，但实际上最好不要超过6、7个
        print("my name is %s, I am %d years old" % (name, age))
        
    # 4、带参装饰器
    def dec(n):
        def outer3(fn):
            def inner():
                print('before3, n=', n)
                fn()
                print('after3, n=', n)
            return inner
    
        return outer3
    
    @dec(8)
    # dec(8) == outer3
    # @dec(8) == @outer3
    def say3():
        print('say3...')
    
    
    say3()    
    ```

    

69. 异常处理写法以及如何主动抛出异常（应用场景）

    ```python
    # 捕获异常
    def func(a,b):
        try:
            res = a/b
        except Exception as e:
            res = e
        return res
    ```

    ```python
    # 自定义异常及抛出异常
    class FooError(Exception):
        pass
    
    
    def func(n):
        if n==0:
            raise FooError("0没有阶乘！！！")
        else:
            res = 1
            for x in range(1,n+1):
                res *= x
    
            return res
    
    
    if __name__ == '__main__':
        try:
            print(func("3"))
        except TypeError as e:
            print(e)
        except FooError as e2:
            print(e2)
    ```

    

70. 什么是面向对象的mro

    ```
    对于定义的每一个类，python会计算出一个方法解析顺序（MRO）列表，这个MRO列表就是一个简单的所有基类的线性顺序列表。
    
    为了实现继承，python会再MRO列表上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止。
    
    MRO列表的构造是通过一个C3线性化算法来实现的。
    
    合并所有父类的MRO列表遵循如下三条准则：
    
    子类会先于父类被检查
    多个父类会根据它们再列表中的顺序被检查
    如果对下一个类存在两个合法的选择，选择第一个父类
    
    ```

    

71. isinstance作用以及应用场景？

72. 写代码并实现：
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would 
    have exactly one solution, and you may not use the same element twice.
    Example: 
         Given nums = [2, 7, 11, 15], target = 9,
          Because nums[0] + nums[1] = 2 + 7 = 9, 
          return [0, 1]

73. json序列化时，可以处理的数据类型有哪些？如何定制支持datetime类型？

74. json序列化时，默认遇到中文会转换成unicode，如果想要保留中文怎么办？

75. 什么是断言？应用场景？

76. 有用过with statement吗？它的好处是什么？

77. 使用代码实现查看列举目录下的所有文件。

78. 简述 yield和yield from关键字。



### 第二部分 网络编程和并发（34题）

1. 简述 OSI 七层协议。

2. 什么是C/S和B/S架构？

3. 简述 三次握手、四次挥手的流程。

    ![三次握手四次挥手示意图](https://img-blog.csdn.net/20160809153521584) 

   ```
   三次握手过程说明： 
   1、由客户端发送建立TCP连接的请求报文，其中报文中包含seq序列号，是由发送端随机生成的，并且将报文中的SYN字段置为1，表示需要建立TCP连接。（SYN=1，seq=x，x为随机生成数值）
   2、由服务端回复客户端发送的TCP连接请求报文，其中包含seq序列号，是由回复端随机生成的，并且将SYN置为1，而且会产生ACK字段，ACK字段数值是在客户端发送过来的序列号seq的基础上加1进行回复，以便客户端收到信息时，知晓自己的TCP建立请求已得到验证。（SYN=1，ACK=x+1，seq=y，y为随机生成数值）这里的ack加1可以理解为是确认和谁建立连接。
   3、客户端收到服务端发送的TCP建立验证请求后，会使自己的序列号加1表示，并且再次回复ACK验证请求，在服务端发过来的seq上加1进行回复。（SYN=1，ACK=y+1，seq=x+1）
   
   
   
   四次挥手过程说明： 
   1、客户端发送断开TCP连接请求的报文，其中报文中包含seq序列号，是由发送端随机生成的，并且还将报文中的FIN字段置为1，表示需要断开TCP连接。（FIN=1，seq=x，x由客户端随机生成）
   
   2、服务端会回复客户端发送的TCP断开请求报文，其包含seq序列号，是由回复端随机生成的，而且会产生ACK字段，ACK字段数值是在客户端发过来的seq序列号基础上加1进行回复，以便客户端收到信息时，知晓自己的TCP断开请求已经得到验证。（FIN=1，ACK=x+1，seq=y，y由服务端随机生成）
   3、服务端在回复完客户端的TCP断开请求后，不会马上进行TCP连接的断开，服务端会先确保断开前，所有传输到A的数据是否已经传输完毕，一旦确认传输数据完毕，就会将回复报文的FIN字段置1，并且产生随机seq序列号。（FIN=1，ACK=x+1，seq=z，z由服务端随机生成）
   4、客户端收到服务端的TCP断开请求后，会回复服务端的断开请求，包含随机生成的seq字段和ACK字段，ACK字段会在服务端的TCP断开请求的seq基础上加1，从而完成服务端请求的验证回复。（FIN=1，ACK=z+1，seq=h，h为客户端随机生成） 
   ```

   

4. 什么是arp协议？

5. TCP和UDP的区别？

    ![img](https://img-blog.csdn.net/20180714082449355?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Jlbmxpbnl1MzQ5NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70) 

6. 什么是局域网和广域网？

7. 为何基于tcp协议的通信比基于udp协议的通信更可靠？

8. 什么是socket？简述基于tcp协议的套接字通信流程。

9. 什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？

10. IO多路复用的作用？

11. 什么是防火墙以及作用？

12. select、poll、epoll 模型的区别？

13. 简述 进程、线程、协程的区别 以及应用场景？

14. GIL锁是什么鬼？

15. Python中如何使用线程池和进程池？

16. threading.local的作用？

17. 进程之间如何进行通信？

18. 什么是并发和并行？

19. 进程锁和线程锁的作用？

20. 解释什么是异步非阻塞？

21. 路由器和交换机的区别？

22. 什么是域名解析？

23. 如何修改本地hosts文件？

24. 生产者消费者模型应用场景及优势？

25. 什么是cdn？

26. LVS是什么及作用？

27. Nginx是什么及作用？

28. keepalived是什么及作用?

29. haproxy是什么以及作用？

30. 什么是负载均衡？

31. 什么是rpc及应用场景？

32. 简述 asynio模块的作用和应用场景。

33. 简述 gevent模块的作用和应用场景。

34. twisted框架的使用和应用？



### 第三部分 数据库和缓存（46题）

1. 列举常见的关系型数据库和非关系型都有那些？
2. MySQL常见数据库引擎及比较？
3. 简述数据三大范式？
4. 什么是事务？MySQL如何支持事务？
5. 简述数据库设计中一对多和多对多的应用场景？
6. 如何基于数据库实现商城商品计数器？
7. 常见SQL（必备）
   详见武沛齐博客：https://www.cnblogs.com/wupeiqi/articles/5729934.html
8. 简述触发器、函数、视图、存储过程？
9. MySQL索引种类
10. 索引在什么情况下遵循最左前缀的规则？
11. 主键和外键的区别？
12. MySQL常见的函数？
13. 列举 创建索引但是无法命中索引的8种情况。
14. 如何开启慢日志查询？
15. 数据库导入导出命令（结构+数据）？
16. 数据库优化方案？
17. char和varchar的区别？
18. 简述MySQL的执行计划？
19. 在对name做了唯一索引前提下，简述以下区别： 
        select * from tb where name = ‘Oldboy-Wupeiqi’  
        select * from tb where name = ‘Oldboy-Wupeiqi’ limit 1
20. 1000w条数据，使用limit offset 分页时，为什么越往后翻越慢？如何解决？
21. 什么是索引合并？
22. 什么是覆盖索引？
23. 简述数据库读写分离？
24. 简述数据库分库分表？（水平、垂直）
25. redis和memcached比较？
26. redis中数据库默认是多少个db 及作用？
27. python操作redis的模块？
28. 如果redis中的某个列表中的数据量非常大，如果实现循环显示每一个值？
29. redis如何实现主从复制？以及数据同步机制？
30. redis中的sentinel的作用？
31. 如何实现redis集群？
32. redis中默认有多少个哈希槽？
33. 简述redis的有哪几种持久化策略及比较？
34. 列举redis支持的过期策略。
35. MySQL 里有 2000w 数据，redis 中只存 20w 的数据，如何保证 redis 中都是热点数据？ 
36. 写代码，基于redis的列表实现 先进先出、后进先出队列、优先级队列。
37. 如何基于redis实现消息队列？
38. 如何基于redis实现发布和订阅？以及发布订阅和消息队列的区别？
39. 什么是codis及作用？
40. 什么是twemproxy及作用？
41. 写代码实现redis事务操作。
42. redis中的watch的命令的作用？
43. 基于redis如何实现商城商品数量计数器？
44. 简述redis分布式锁和redlock的实现机制。
45. 什么是一致性哈希？Python中是否有相应模块？
46. 如何高效的找到redis中所有以oldboy开头的key？



### 第四部分 前端、框架和其他（155题）

1. 谈谈你对http协议的认识。

2. 谈谈你对websocket协议的认识。

3. 什么是magic string ？

4. 如何创建响应式布局？

5. 你曾经使用过哪些前端框架？

6. 什么是ajax请求？并使用jQuery和XMLHttpRequest对象实现一个ajax请求。

7. 如何在前端实现轮训？

8. 如何在前端实现长轮训？

9. vuex的作用？

10. vue中的路由的拦截器的作用？

11. axios的作用？

12. 列举vue的常见指令。

13. 简述jsonp及实现原理？

14. 是什么cors ？

15. 列举Http请求中常见的请求方式？

16. 列举Http请求中的状态码？

17. 列举Http请求中常见的请求头？

18. 看图写结果：
    ![img](https://images2018.cnblogs.com/blog/425762/201805/425762-20180523193331193-1780213562.png)

19. 看图写结果：
    ![img](https://images2018.cnblogs.com/blog/425762/201805/425762-20180523193350024-1394121124.png)

20. 看图写结果：
    ![img](https://images2018.cnblogs.com/blog/425762/201805/425762-20180523193402254-925709250.png)

21. 看图写结果：
    ![img](https://images2018.cnblogs.com/blog/425762/201805/425762-20180523193412085-688600397.png) 

22. 看图写结果：
    ![img](https://images2018.cnblogs.com/blog/425762/201805/425762-20180523193421487-536908496.png)

23. 看图写结果：
    ![img](https://images2018.cnblogs.com/blog/425762/201805/425762-20180523193433388-1947519928.png)

24. django、flask、tornado框架的比较？

25. 什么是wsgi？

26. django请求的生命周期？

27. 列举django的内置组件？

28. 列举django中间件的5个方法？以及django中间件的应用场景？

29. 简述什么是FBV和CBV？

30. django的request对象是在什么时候创建的？

31. 如何给CBV的程序添加装饰器？

32. 列举django orm 中所有的方法（QuerySet对象的所有方法）

33. only和defer的区别？

34. select_related和prefetch_related的区别？

35. filter和exclude的区别？

36. 列举django orm中三种能写sql语句的方法。

37. django orm 中如何设置读写分离？

38. F和Q的作用?

39. values和values_list的区别？

40. 如何使用django orm批量创建数据？

41. django的Form和ModeForm的作用？

42. django的Form组件中，如果字段中包含choices参数，请使用两种方式实现数据源实时更新。

43. django的Model中的ForeignKey字段中的on_delete参数有什么作用？

44. django中csrf的实现机制？

45. django如何实现websocket？

46. 基于django使用ajax发送post请求时，都可以使用哪种方法携带csrf token？

47. django中如何实现orm表中添加数据时创建一条日志记录。

48. django缓存如何设置？

49. django的缓存能使用redis吗？如果可以的话，如何配置？

50. django路由系统中name的作用？

51. django的模板中filter和simple_tag的区别？

52. django-debug-toolbar的作用？

53. django中如何实现单元测试？

54. 解释orm中 db first 和 code first的含义？

55. django中如何根据数据库表生成model中的类？

56. 使用orm和原生sql的优缺点？

57. 简述MVC和MTV

58. django的contenttype组件的作用？

59. 谈谈你对restfull 规范的认识？

60. 接口的幂等性是什么意思？

61. 什么是RPC？

62. Http和Https的区别？

63. 为什么要使用django rest framework框架？

64. django rest framework框架中都有那些组件？

65. django rest framework框架中的视图都可以继承哪些类？

66. 简述 django rest framework框架的认证流程。

67. django rest framework如何实现的用户访问频率控制？

68. Flask框架的优势？

69. Flask框架依赖组件？

70. Flask蓝图的作用？

71. 列举使用过的Flask第三方组件？

72. 简述Flask上下文管理流程?

73. Flask中的g的作用？

74. Flask中上下文管理主要涉及到了那些相关的类？并描述类主要作用？

75. 为什么要Flask把Local对象中的的值stack 维护成一个列表？

76. Flask中多app应用是怎么完成？

77. 在Flask中实现WebSocket需要什么组件？

78. wtforms组件的作用？

79. Flask框架默认session处理机制？

80. 解释Flask框架中的Local对象和threading.local对象的区别？

81. Flask中 blinker 是什么？

82. SQLAlchemy中的 session和scoped_session 的区别？

83. SQLAlchemy如何执行原生SQL？

84. ORM的实现原理？

85. DBUtils模块的作用？

86. 以下SQLAlchemy的字段是否正确？如果不正确请更正：

    

87. SQLAchemy中如何为表设置引擎和字符编码？

88. SQLAchemy中如何设置联合唯一索引？

89. 简述Tornado框架的特点。

90. 简述Tornado框架中Future对象的作用？

91. Tornado框架中如何编写WebSocket程序？

92. Tornado中静态文件是如何处理的？ 如： <link href="{{static_url("commons.css")}}" rel="stylesheet" />

93. Tornado操作MySQL使用的模块？

94. Tornado操作redis使用的模块？

95. 简述Tornado框架的适用场景？

96. git常见命令作用：

97. 简述以下git中stash命令作用以及相关其他命令。

98. git 中 merge 和 rebase命令 的区别。

99. 公司如何基于git做的协同开发？

100. 如何基于git实现代码review？

101. git如何实现v1.0 、v2.0 等版本的管理？

102. 什么是gitlab？

103. github和gitlab的区别？

104. 如何为github上牛逼的开源项目贡献代码？

105. git中 .gitignore文件的作用?

106. 什么是敏捷开发？

107. 简述 jenkins 工具的作用?

108. 公司如何实现代码发布？

109. 简述 RabbitMQ、Kafka、ZeroMQ的区别？

110. RabbitMQ如何在消费者获取任务后未处理完前就挂掉时，保证数据不丢失？

111. RabbitMQ如何对消息做持久化？

112. RabbitMQ如何控制消息被消费的顺序？

113. 以下RabbitMQ的exchange type分别代表什么意思？如：fanout、direct、topic。

114. 简述 celery 是什么以及应用场景？

115. 简述celery运行机制。

116. celery如何实现定时任务？

117. 简述 celery多任务结构目录？

118. celery中装饰器 @app.task 和 @shared_task的区别？

119. 简述 requests模块的作用及基本使用？

120. 简述 beautifulsoup模块的作用及基本使用？

121. 简述 seleninu模块的作用及基本使用?

122. scrapy框架中各组件的工作流程？

123. 在scrapy框架中如何设置代理（两种方法）？

124. scrapy框架中如何实现大文件的下载？

125. scrapy中如何实现限速？

126. scrapy中如何实现暂定爬虫？

127. scrapy中如何进行自定制命令？

128. scrapy中如何实现的记录爬虫的深度？

129. scrapy中的pipelines工作原理？

130. scrapy的pipelines如何丢弃一个item对象？

131. 简述scrapy中爬虫中间件和下载中间件的作用？

132. scrapy-redis组件的作用？

133. scrapy-redis组件中如何实现的任务的去重？

134. scrapy-redis的调度器如何实现任务的深度优先和广度优先？

135. 简述 vitualenv 及应用场景?

136. 简述 pipreqs 及应用场景？

137. 在Python中使用过什么代码检查工具？

138. 简述 saltstack、ansible、fabric、puppet工具的作用？

139. B Tree和B+ Tree的区别？

140. 请列举常见排序并通过代码实现任意三种。

141. 请列举常见查找并通过代码实现任意三种。

142. 请列举你熟悉的设计模式？

143. 有没有刷过leetcode？

144. 列举熟悉的的Linux命令。

145. 公司线上服务器是什么系统？

146. 解释 PV、UV 的含义？

147. 解释 QPS的含义？

148. uwsgi和wsgi的区别？

149. supervisor的作用？

150. 什么是反向代理？

151. 简述SSH的整个过程。

152. 有问题都去那些找解决方案？

153. 是否有关注什么技术类的公众号？

154. 最近在研究什么新技术？

155. 是否了解过领域驱动模型？



### 第五部分 其他同学现场面试题集锦（限web）

#### web及python相关

1. 近期是什么项目，做了多久，从什么时候到什么时候

2. 团队有多少人？

3. python闭包原理、装饰器应用场景

4. 客户端向服务器端请求数据，要怎么取到

5. 讲一下uWGSI，（详介）

6. 讲一下迭代器和生成器

7. 了解python源码吗（前后问了3次）

8. 讲讲线程进程协程、进程直接通信的办法、python的全局锁GIL

9. 使用django还是django RESTful

10. 数据结构你都涉及那些？

11. 编码书写规范有哪些？   PEP8 风格哪些, 说几个  

12. Django的工作流程

13. Django中间件的使用

14. Django中ORM的工作原理

15. 单例模式,工厂模式、python的设计模式有了解么 ?举例

16. uWSGI 的工作原理

17. 你的app前端的开发的工具

18. 装饰器迭代器生成器应用场景

19. django 设置session 过期时间

20. 对线程进程有什么了解+GIL

21. \_\_new\_\_和\_\_init\_\_的区别

22. Linux 的一些命令, 查看进程的命令  

23.   多进程，多线程，多协程 区别  

24.   多线程，那请你简述一下在你项目中多线程的运用 

25.   你项目的第三方登录是怎么实现的  

26.   项目牵扯到用户敏感信息的时候，你是怎么处理的，直接存入数据库么  

27.   对nginx的性能了解有多少，说说你的理解  

28.   开发过程中遇到过什么问题，怎么解决的，花了多久  

29.   有没有研究过数据库优化这方面的知识  

30.   项目中，你是怎么实现用户权限管理的  

31.    对redis的很了解么，说说你的理解，平时都怎么用redis的  

32.    对linux很熟悉么，都写过什么shell脚本  

33.  如果一个web我只允许100人来访问,如果有1000个人来同时访问,怎么处理?  （消息队列）

34. a=[1], 则令a[15]=20, 结果是什么（索引越界）

35. 讲下XXX项目是怎么做的  

36. 用vi怎么查询含有a的字段

37. 怎么查Linux程序

38. 怎么查Linux端口

39. session cookie jwt区别

40. cookie 的最大值

41. redis的雪崩是什么

42. redis的数据类型

43. 说一下对称加密和非对称加密算法有哪些

44. Django中你是怎么使用异步任务的

45. 深浅拷贝的区别

46. python内存管理机制

47. 讲一下awk命令的主要用法和运用场景

48. Django和Flask中的事务怎么调用（这块主要我提到了db.sessoin）

49. Flask中的flush()和commit()的区别

50. TCP、UDP的区别

51. Nginx配置文件的http和server字段（这块主要要讲到Nginx可以做负载均衡，还可以做反向代理，可以配置很多个server）

52. 了解哪些MySQL索引

53. http和https的区别

54. 为什么用uWSGi，而不是用flask测试用的服务器

55. 装饰器，手写一个计算时间的装饰器，同时需要用funtools中的wrapper装饰

56. 给字段建索引，比如说age、sex、name这个三个字段，你会怎么建立索引

57. 如果网络出现了异常，你是怎么进行调试的

58. 讲一下查看运行的程序，如果我们想杀掉它，怎么弄

59. 通过celery定时任务，讲一下为什么采用异步，你给定的时间是多少，前端设置的时间是多少，如果网络出现了异常，你会怎么处理

60. 为什么采用JWT进行身份验证

61. 调用支付宝的API，那如果支付成功后，商城APP的界面还是未付款，这时候你是怎么处理的

62. 做过定时任务嘛，你是怎么实现的

63. 数据库三范式

64.  数据库事务

65.  僵尸进程和守护进程 怎么实现

66.  字典的底层原理  

67. 正则匹配ip

68. 了解哪些查找算法

69. 了解哪些排序算法

70. 实现单例模式

71. 实现list去重

72. 数据库左连接查询

73. 写一个快速排序

74. 函数的值传递和应用传递

75.  项目多少人每个人的主要职责你主要负责什么  

76. 具体说一下你负责模块的某个功能

77.  你的团队协作开发流程,(git分支)

78. 简单介绍一下继承封装多态

79. Redis怎么存放购物车的，Redis常用来做什么

80. 为什么要使用中间件进行登录验证，如果写在逻辑代码中会有什么问题么

81. 简单说一下RSA，是如何使用的？使用场景呢？见到那聊一聊对称加密和非对称加密

82. 为什么要设置IP池和UA池

83. 电商：

    1.用户模块：用户的个人信息验证我采用了JWT,密码采用了RSA+AES加密，然后经过加盐处理。

    面试官：JWT是什么，是自动生成的还是自己构造的，保存了用户那些信息，攻击者拿到相对于的token后，是不是可以获取数据，发起攻击呢？在这块怎么处理的？ 密码加密解密的过程是怎么样的，加盐后你是怎么存放到数据库中，如果数据库脱库了，怎么能够防止攻击者撞库

    2.商品模块：我主要讲了将商品图片的信息存放到第三方平台，存在哪些字段  
     面试官：你的数据库设计是多大的数量，怎么处理相关的数据的，处理过商品和商品之间存在关联之类的，举一个列子，12306中的购票订单，（这一块我没有理解到，我就说了各个商品没有太大的关联，我设计数据库的时候只是存在层级的联系，比如分类的等级这块。然后就过去了）

    3.订单模块：我主要将了事务，用户下单的过程是怎么样子的
     面试官：你是怎么开启事务的，订单号是怎么生成的（我主要将通过hashlib生成相关的订单），他说这样生成的订单会不会太长了，然后我就开始了解释。问了我在这里为什么要执行回滚操作，因为这里我解释的很模糊（但后面强行解析了，很在理。）

     

    4.购物车模块：主要将用户的购物车信息存放在Redis中，历史记录等信息。
       面试官：具体是怎么存入到Redis中的，如果服务器宕机了，是怎么处理的。对于热数据你这边是怎么解决的

    

       A:用户的数据量超大时怎么处理？
       B：分表（按照用户的id分）

       A:怎么保证数据的高可用：
       B:主要讲了主从复制，当主数据库挂掉后，从服务器启动。

       A:项目上线部署了在一台，还是几台服务器？
       B:我讲了是部署在多台服务器，（然后他开始问了，你部署在多台服务器上，怎么解决用户的并发的执行下单操作），我主要将利用锁，（这里一直跟他在争，说代码的怎么保证数据的一致性），我主要讲到，ORM操作会转为sql语句执行，最终去数据库中都会需要拿到锁才能执行。

       A:服务器的机房是怎么管理的？
       B:我在项目搭建的时候，选择了云服务器（买的哪里的服务器），腾讯云。

    

84. 在10M的log日志文件中，查找某个用户的错误操作

85. 熟悉什么后端框架，Django的核心是什么

86. ORM是什么，他的优缺点有哪些方面

87. 能够修改元组的值吗？会报什么异常错误

88. 元组和列表的区别

89. 正则中match和search的区别

90. SQL注入有了解过吗？

91. 谈谈restful风格的理解

92. 字典转为元组怎么转，结果是怎么样的

93. 数据库的优化怎么做

94.  那个框架比较熟悉，Django和flask的基本原理，或者核心的东西是什么  

95. Django和Flask并发是怎么处理

96. Django的orm是怎么样的，事物是怎么管理的？

97.  经常使用的python模块有哪些  

98.   购物车有什么字段  

99.   有没有接触过高并发 还有django的什么点列什么搜索的  

100.   会不会做Python的微服务  

101.    HTTP响应组成部分？  

102.    TCP解包方法知道吗？  

103.   写过基于TCP协议的客户端与服务端吗？  

104.   HTTP是如何基于TCP协议传输数据的？  

105.    非对称加密知道吗  ？

106.    你这个支付接口的调用是怎么做的  

107.   那你怎么保证这个回调的地址不是别人恶意伪造的呢（验证token？  

108.    RPC框架知道吗？  

109.    微信接口怎么调用的？要哪些参数？

110.    装饰器带参数情况用过吗    

111.    怎么部署项目的  

112. 讲下进程启动，讲下消费者生产者模式

113. 讲一下scrapy和selenium中间件

114. 讲一下python中字符串的常用方法

115. 写个正则，匹配一下手机号

116.   *args **kwargs的使用场景 还有是什么来着  

117.    了解TCP、UDP协议，那你说说ping命令是基于什么协议，DNS解析是什么协议  

118.    写一个验证邮箱的正则表达式  

119.    基于你了解的restful架构思想，你会如何搭建一个博客的url  



#### 爬虫相关

1. scrapy的工作原理
2. 对爬取阿里系网站遇到什么困难，怎么解决的？
3. 在爬虫项目的过程中都遇到过什么反爬措施，你是怎么解决的   
4. 问了爬数据被限制了IP和账号，每次只能爬10页，怎么处理
5.  怎么清洗数据
6. 在爬虫项目中遇到哪些防爬措施
7. 说一下Scrapy的中间件， 你用过哪些中间件
8. Scrapy在怎么设置ip代理池， 具体代码



#### 数据库相关

1.redis事务了解吗？

2.redis哨兵机制了解吗？

3.mysql索引了解多少、什么时候会失效？





### 第六部分必须熟悉的问题

基础：

1. 多进程，多线程，多协程 区别  

   ```
   面试官：对Python的进程、线程、协程有哪些认识？
   
   Alex：先说进程吧，我们写的代码并不能直接运行，只有将程序装载到内存中，操作系统为它分配资源才能运行，这种执行的程序就叫进程，进程是计算机最小的资源分配单位；而线程是操作系统能够进行运算调度的最小单位，它被包含在进程之中，是进程中实际工作的单位，一个进程可以并发多个线程，每条线程并行执行不同的任务，当然是在不考虑GIL锁的情况下；而协程一种基于单线程实现并发的手段，是由用户程序自己控制调度的，在单线程内开启协程，一旦遇到IO操作，就会从应用程序级别控制切换，以此来提升效率。
   
   面试官：你刚刚提到了GIL锁，可以简单说一下么？
   
   Alex：GIL，就是Global Interpreter Lock，中文名叫全局解释器锁，这是一个互斥锁，用来防止多个本机线程同时进入cpu执行。GIL只存在于CPython中，存在即合理，CPython的内存管理不是线程安全的，所以GIL锁也是必要的。每次执行Python程序，都会产生一个独立的进程，在这个进程中，不仅有该进程开启的线程，还有解释器开启的线程，比如垃圾回收这种解释器级别的线程。所有的线程运行在一个进程内，线程的任务需要将代码传给解释器去执行，而数据都是共享的，这样就到导致线程不安全。举个简单的例子：对于同一个数据100，可能线程1执行x=100的同时，而垃圾回收执行的是回收100的操作，解决这种问题没有什么高明的方法，就是加锁处理。所以GIL可以保证Python解释器同一时间只能执行一个线程。
   
   ```

   
   
2. python闭包原理、装饰器应用场景

3. 讲一下可迭代对象、迭代器和生成器

   ```
   面试官：然后你说一下什么是装饰器、生成器和迭代器。
   
   Alex：首先说一下迭代器吧，迭代器对象就是实现了iter() 和 next()方法的对象，其中iter()返回迭代器本身，而next()返回容器的下一个元素，在结尾处引发StopInteration异常。而生成器是创建迭代器的工具，在Python中，一边循环一边计算的机制，称为生成器（Generator）。生成器对延迟操作提供了支持，所谓延迟操作，是指在需要的时候才产生结果，而不是立即产生结果。装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能。装饰器就有很多应用场景了，比如可以在Web开发中用于检查某个用户是否有权限去做某件事，这种授权检测被大量使用在Django、Flask这种Web框架中。另外装饰器也可以用于打印日志，记录程序运行时间。
   
   ```

   

   

4. 三次握手与四次挥手

   ```
   三次握手：
   
   第1次握手：建立连接时，客户端发送syn包（syn=x）到服务器，并进入同步已发送状态，等待服务器确认；SYN：同步序列编号。
   
   第2次握手：服务器收到syn包，必须确认客户的SYN（ack=x+1），同时自己也发送一个SYN包（syn=y），即SYN+ACK包，此时服务器进入同步已接受状态。
   
   第3次握手：客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=y+1），此包发送完毕，客户端和服务器进入ESTABLISHED（TCP连接成功）状态，完成三次握手。
   
   
   
   
   四次挥手：
   
   第1次挥手：客户端进程发出连接释放报文，并且停止发送数据。此时，客户端进入FIN-WAIT-1（终止等待1）状态。
   
   第2次挥手：服务器收到连接释放报文，发出确认报文。服务端就进入了CLOSE-WAIT（关闭等待）状态。TCP服务器通知高层的应用进程，客户端向服务器的方向就释放了，这时候处于半关闭状态，即客户端已经没有数据要发送了，但是服务器若发送数据，客户端依然要接受。这个状态还要持续一段时间，也就是整个CLOSE-WAIT状态持续的时间。
   
   客户端收到服务器的确认请求后，此时，客户端就进入FIN-WAIT-2（终止等待2）状态，等待服务器发送连接释放报文（在这之前还需要接受服务器发送的最后的数据）。
   
   第3次挥手：服务器将最后的数据发送完毕后，就向客户端发送连接释放报文，FIN=1，ack=u+1，由于在半关闭状态，服务器很可能又发送了一些数据，假定此时的序列号为seq=w，此时，服务器就进入了LAST-ACK（最后确认）状态，等待客户端的确认。
   
   第4次挥手：客户端收到服务器的连接释放报文后，必须发出确认，ACK=1，ack=w+1，而自己的序列号是seq=u+1，此时，客户端就进入了TIME-WAIT（时间等待）状态。注意此时TCP连接还没有释放，必须经过2MSL（最长报文段寿命）的时间后，当客户端撤销相应的TCp后，才进入CLOSED状态
   ```

   

   

   

   

   

   

   

5. 单例模式,工厂模式、python的设计模式有了解么 ?举例

   ```python
   class singleton():
       def __new__(cls, *args, **kwargs):
           if not hasattr(cls, 'instance'):
               instance = super().__new__(cls, *args, **kwargs)
           return instance
   ```

   

6. \_\_new\_\_和\_\_init\_\_的区别

7. 单元测试

8. 深浅拷贝的区别

9. python内存管理机制

10. 讲一下python中字符串的常用方法

11. 写个正则，匹配一下手机号

12. 写一个验证邮箱的正则表达式  



数据库：

1. mysql的事务

   ```
   原子性、一致性、隔离性、持久性
   
   在mysql中用的最多的存储引擎有：innodb，bdb，myisam ,memory 等。其中innodb和bdb支持事务而myisam等不支持事务。
   ```

   

2. mysql存储引擎

   ```
   答：InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。 
   
   MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比较低，也可以使用。
   
   ```

   

3. mysql主从复制

   

4. 主键和外键的区别？

   答：主键：唯一标识一条记录，不能有重复的，不允许为空

   外键：表的外键是另一表的主键, 外键可以有重复的, 可以是空值

   

5. 数据库的范式

   ```
   第一范式：当关系模式R的所有属性都不能在分解为更基本的数据单位时，称R是满足第一范式的，简记为1NF。满足第一范式是关系模式规范化的最低要求，否则，将有很多基本操作在这样的关系模式中实现不了。
   
   第二范式：如果关系模式R满足第一范式，并且R得所有非主属性都完全依赖于R的每一个候选关键属性，称R满足第二范式，简记为2NF。
   
   第三范式：设R是一个满足第一范式条件的关系模式，X是R的任意属性集，如果X非传递依赖于R的任意一个候选关键字，称R满足第三范式，简记为3NF.
   
   
   第一范式：（1NF）列不可拆分
   第二范式：（2NF）属性完全依赖于主键
   第三范式：（3NF）属性不依赖于其它非主属性
   
   
   
    第一范式（1NF）：强调的是列的原子性，即列不能够再分成其他几列。 
   考虑这样一个表：【联系人】（姓名，性别，电话） 
   如果在实际场景中，一个联系人有家庭电话和公司电话，那么这种表结构设计就没有达到 1NF。要符合 1NF 我们只需把列（电话）拆分，即：【联系人】（姓名，性别，家庭电话，公司电话）。1NF 很好辨别，但是 2NF 和 3NF 就容易搞混淆。 
   
   ◆ 第二范式（2NF）：首先是 1NF，另外包含两部分内容，一是表必须有一个主键；二是没有包含在主键中的列必须完全依赖于主键，而不能只依赖于主键的一部分。 
   考虑一个订单明细表：【OrderDetail】（OrderID，ProductID，UnitPrice，Discount，Quantity，ProductName）。 
   因为我们知道在一个订单中可以订购多种产品，所以单单一个 OrderID 是不足以成为主键的，主键应该是（OrderID，ProductID）。显而易见 Discount（折扣），Quantity（数量）完全依赖（取决）于主键（OderID，ProductID），而 UnitPrice，ProductName 只依赖于 ProductID。所以 OrderDetail 表不符合 2NF。不符合 2NF 的设计容易产生冗余数据。 
   可以把【OrderDetail】表拆分为【OrderDetail】（OrderID，ProductID，Discount，Quantity）和【Product】（ProductID，UnitPrice，ProductName）来消除原订单表中UnitPrice，ProductName多次重复的情况。 
   
   ◆ 第三范式（3NF）：首先是 2NF，另外非主键列必须直接依赖于主键，不能存在传递依赖。即不能存在：非主键列 A 依赖于非主键列 B，非主键列 B 依赖于主键的情况。 
   考虑一个订单表【Order】（OrderID，OrderDate，CustomerID，CustomerName，CustomerAddr，CustomerCity）主键是（OrderID）。 
   其中 OrderDate，CustomerID，CustomerName，CustomerAddr，CustomerCity 等非主键列都完全依赖于主键（OrderID），所以符合 2NF。不过问题是 CustomerName，CustomerAddr，CustomerCity 直接依赖的是 CustomerID（非主键列），而不是直接依赖于主键，它是通过传递才依赖于主键，所以不符合 3NF。 
   通过拆分【Order】为【Order】（OrderID，OrderDate，CustomerID）和【Customer】（CustomerID，CustomerName，CustomerAddr，CustomerCity）从而达到 3NF。 
   第二范式（2NF）和第三范式（3NF）的概念很容易混淆，区分它们的关键点在于，2NF：非主键列是否完全依赖于主键，还是依赖于主键的一部分；3NF：非主键列是直接依赖于主键，还是直接依赖于非主键列。
   ```

   

6. redis

   ```
   https://www.php.cn/redis/425002.html
   Redis有哪些数据结构呀？
   字符串String、字典Hash、列表List、集合Set、有序集合SortedSet
   
   
   
   什么是Redis持久化？Redis有哪几种持久化方式？优缺点是什么？
   持久化就是把内存的数据写到磁盘中去，防止服务宕机了内存数据丢失。
   Redis 提供了两种持久化方式:RDB（默认） 和AOF
   
   RDB是一个非常紧凑的文件,它保存了某个时间点得数据集,非常适用于数据集的备份,比如你可以在每个小时报保存一下过去24小时内的数据,同时每天保存过去30天的数据,这样即使出了问题你也可以根据需求恢复到不同版本的数据集
   
   如果你希望在redis意外停止工作（例如电源中断）的情况下丢失的数据最少的话，那么RDB不适合你.虽然你可以配置不同的save时间点(例如每隔5分钟并且对数据集有100个写的操作),是Redis要完整的保存整个数据集是一个比较繁重的工作,你通常会每隔5分钟或者更久做一次完整的保存,万一在Redis意外宕机,你可能会丢失几分钟的数据
   
   
   AOF持久化方式记录每次对服务器写的操作,当服务器重启的时候会重新执行这些命令来恢复原始的数据,AOF命令以redis协议追加保存每次写的操作到文件末尾.Redis还能对AOF文件进行后台重写,使得AOF文件的体积不至于过大
   
   
   什么是缓存穿透？如何避免？什么是缓存雪崩？何如避免？
   缓存穿透
   一般的缓存系统，都是按照key去缓存查询，如果不存在对应的value，就应该去后端系统查找（比如DB）。一些恶意的请求会故意查询不存在的key,请求量很大，就会对后端系统造成很大的压力。这就叫做缓存穿透。
   如何避免？
   1：对查询结果为空的情况也进行缓存，缓存时间设置短一点，或者该key对应的数据insert了之后清理缓存。
   2：对一定不存在的key进行过滤。可以把所有的可能存在的key放到一个大的Bitmap中，查询时通过该bitmap过滤。
   
   
   缓存雪崩
当缓存服务器重启或者大量缓存集中在某一个时间段失效，这样在失效的时候，会给后端系统带来很大压力。导致系统崩溃。
   如何避免？
   
   1：在缓存失效后，通过加锁或者队列来控制读数据库写缓存的线程数量。比如对某个key只允许一个线程查询数据和写缓存，其他线程等待。
   2：做二级缓存，A1为原始缓存，A2为拷贝缓存，A1失效时，可以访问A2，A1缓存失效时间设置为短期，A2设置为长期
   3：不同的key，设置不同的过期时间，让缓存失效的时间点尽量均匀
   ```
   
   



框架：

1. Django的工作流程
2. Django中间件的使用
3. Django中ORM的工作原理
4. 
5. uWSGI 的工作原理



爬虫：
1, User-Agent--- UA池
2, cookies ---带着cookies, 高级一点用cookies
3, 根据访问频率 --- ip代理池,或者放慢爬取速度,加一个延迟.
4, 字体加密 ---- 找到字体文件, 使用fonttools加载字体文件.生成映射表.
5, 验证码 ---- 简单验证码可以使用ocr工具进行识别,复杂的验证码使用第三方的打码平台,比如超级鹰.
6, JS加密 ---- 找到加密的js文件,分析加密算法.Pyexecjs
7, 蜜罐抓猪 ---- 分析蜜罐的策略.
8, 页面懒加载 ---splash