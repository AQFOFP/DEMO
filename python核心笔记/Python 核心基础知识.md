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

