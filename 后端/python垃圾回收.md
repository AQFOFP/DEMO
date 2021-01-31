## Python垃圾回收

基于C语言源码底层，真正了解垃圾回收机制的实现

- 引用计数器

- 标记清除

- 分代回收

- 缓存机制

- Python的C源码（3.8.2）

  

## 1.引用计数器

### 1.1 双向环状链表refchain

![1589992930937](C:\Users\Administrator\Desktop\简历\image\垃圾回收01.png) 

 在python程序中创建的任何对象都会放在refchain链表中

```python
name = 'zs'
age = 18
hobby = ['篮球', '美女']
```

```python
name = 'zs'   内部会创建一些数据【上一个对象、下一个对象、类型、引用个数】
name2 = name   引用计数器+1

内部会创建一些数据【上一个对象、下一个对象、类型、引用个数、val=18】
age = 18 

内部会创建一些数据【上一个对象、下一个对象、类型、引用个数、items=元素、元素个数】
hobby = ['篮球', '美女'] 
```





```c
#define PyObject_HEAD       PyObject ob_base;
#define PyObject_VAR_HEAD      PyVarObject ob_base;

// 宏定义，包含上一个、下一个，用于构造双向链表用。（放到refchain链表中，要用到）
#define _PyObject_HEAD_EXTRA            
    struct _object *_ob_next;           
    struct _object *_ob_prev;
      
typedef struct _object {
    _PyObject_HEAD_EXTRA // 用于构造双向链表
    Py_ssize_t ob_refcnt;  // 引用计数器
    struct _typeobject *ob_type;    // 数据类型
} PyObject;
 
 
typedef struct {
    PyObject ob_base;   // PyObject对象
    Py_ssize_t ob_size; /* Number of items in variable part，即：元素个数 */
} PyVarObject;
```

在C源码中如何体现每个对象中都有的相同的值：PyObject结构体（封装4个值）

有多个元素（如：列表）组成的对象：PyObject结构体（封装4个值） + ob_size = PyVarObject



### 1.2 类型封装结构体解析

```c
// float类型

typedef struct {
    PyObject_HEAD
    double ob_fval;
} PyFloatObject;

data = 3.14
内部会创建：
    _ob_next = refchain中的上一个对象
    _ob_prev = refchain中的下一个对象
    ob_refcnt = 1
    ob_type = float
    ob_fval = 3.14
```



```c
// int类型

// longintrepr.h

struct _longobject {
    PyObject_VAR_HEAD
    digit ob_digit[1];
};

// longobject.h

/* Long (arbitrary precision) integer object interface */
typedef struct _longobject PyLongObject; /* Revealed in longintrepr.h */

/*
1. python3中没有long类型，只有int类型，但py3内部的int是基于long实现。
2. python3中对int/long长度没有限制，因其内部不是用long存储而是使用类似于“字符串”存储。
*/
```



```c
// list类型

typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;
    Py_ssize_t allocated;
} PyListObject;
```



```c
// tuple类型

typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];
} PyTupleObject;
```



```c
// dict类型

typedef struct {
    PyObject_HEAD
    Py_ssize_t ma_used;
    PyDictKeysObject *ma_keys;
    PyObject **ma_values;
} PyDictObject;
```



### 1.3 引用计数器

```python
v1 = 3.14
v2 = 999
v3 = (1, 2, 3)
```

当python程序运行时，会根据数据类型的不同找到其对应的结构体，根据结构体中的字段来进行创建相关的数据，然后将对象添加到refchain双向链表中

在C源码中有两个关键的结构体：PyObject、PyVarObject

每个对象中有ob_refcnt就是引用计数器，值默认为1，当有其他变量引用对象时，引用计数器就会发生变化

```python
a = 999
b = a   # 引用计数器 +1

# 计数器-1
del b   # b变量删除：b对应对象引用计数器-1
del a   # a变量删除：a对应对象引用计数器-1

# 当一个对象的引用计数器为0时，意味着没有人再使用这个对象，这个对象就是垃圾，垃圾回收

# 回收：1.对象从refchain链表移除， 2.将对象销毁，内存归还给操作系统
```



### 1.4  循环引用 

```python
v1 = [11,22,33]        # refchain中创建一个列表对象，由于v1=对象，所以列表引对象用计数器为1.
v2 = [44,55,66]        # refchain中再创建一个列表对象，因v2=对象，所以列表对象引用计数器为1.
v1.append(v2)        # 把v2追加到v1中，则v2对应的[44,55,66]对象的引用计数器加1，最终为2.
v2.append(v1)        # 把v1追加到v1中，则v1对应的[11,22,33]对象的引用计数器加1，最终为2.


del v1    # 引用计数器-1
del v2    # 引用计数器-1
```

对于上述代码会发现，执行`del`操作之后，没有变量再会去使用那两个列表对象，但由于循环引用的问题，他们的引用计数器不为0，所以他们的状态：永远不会被使用、也不会被销毁。项目中如果这种代码太多，就会导致内存一直被消耗，直到内存被耗尽，程序崩溃。

为了解决循环引用的问题，引入了`标记清除`技术，专门针对那些可能存在循环引用的对象进行特殊处理，可能存在循环应用的类型有：列表、元组、字典、集合、自定义类等那些能进行数据嵌套的类型。



## 2.标记清除

目的：为了解决引用计数器循环引用的不足

实现：在python底层再维护一个链表，链表中专门放那些可能存在循环引用的对象（list/tuple/dict/set）

![1589996801884](C:\Users\Administrator\Desktop\简历\image\垃圾回收02.png)

在Python内部【某种情况】下触发，会去扫描【可能存在循环应用的链表】中的每一个元素，检查是否有循环引用，如果有则让双方引用计数器-1；如果是0则是垃圾回收。



问题：

- 什么时候扫描？
- 可能存在循环引用的链表扫描代价大，每次扫描耗时久



## 3.分代回收

![1589997206121](C:\Users\Administrator\Desktop\简历\image\垃圾回收03.png)

将可能存在循环应用的对象维护成3个链表

- 0代：0代中对象个数达到700个扫描一次
- 1代：0代扫描10次，则1代扫描一次
- 2代：1代扫描10次，则2代扫描一次



```c
// 分代的C源码
#define NUM_GENERATIONS 3
struct gc_generation generations[NUM_GENERATIONS] = {
    /* PyGC_Head,                                    threshold,    count */
    {{(uintptr_t)_GEN_HEAD(0), (uintptr_t)_GEN_HEAD(0)},   700,        0}, // 0代
    {{(uintptr_t)_GEN_HEAD(1), (uintptr_t)_GEN_HEAD(1)},   10,         0}, // 1代
    {{(uintptr_t)_GEN_HEAD(2), (uintptr_t)_GEN_HEAD(2)},   10,         0}, // 2代
};
```

特别注意：0代和1、2代的threshold和count表示的意义不同。

- 0代，count表示0代链表中对象的数量，threshold表示0代链表对象个数阈值，超过则执行一次0代扫描检查。
- 1代，count表示0代链表扫描的次数，threshold表示0代链表扫描的次数阈值，超过则执行一次1代扫描检查。
- 2代，count表示1代链表扫描的次数，threshold表示1代链表扫描的次数阈值，超过则执行一2代扫描检查。



```
第一步：当创建对象age=19时，会将对象添加到refchain链表中
第二步：当创建对象num_list = [11,22]时，会将列表对象添加到 refchain 和 generations 0代中
第三步：新创建对象使generations的0代链表上的对象数量大于阈值700时，要对链表上的对象进行扫描检查。

当0代大于阈值后，底层不是直接扫描0代，而是先判断2、1是否也超过了阈值。

如果2、1代未达到阈值，则扫描0代，并让1代的 count + 1 。
如果2代已达到阈值，则将2、1、0三个链表拼接起来进行全扫描，并将2、1、0代的count重置为0.
如果1代已达到阈值，则讲1、0两个链表拼接起来进行扫描，并将所有1、0代的count重置为0.


对拼接起来的链表在进行扫描时，主要就是剔除循环引用和销毁垃圾，详细过程为：

扫描链表，把每个对象的引用计数器拷贝一份并保存到 gc_refs中，保护原引用计数器。
再次扫描链表中的每个对象，并检查是否存在循环引用，如果存在则让各自的gc_refs减 1 。
再次扫描链表，将 gc_refs 为 0 的对象移动到unreachable链表中；不为0的对象直接升级到下一代链表中。
处理unreachable链表中的对象的 析构函数 和 弱引用，不能被销毁的对象升级到下一代链表，能销毁的保留在此链表。
析构函数，指的就是那些定义了__del__方法的对象，需要执行之后再进行销毁处理。
弱引用，
最后将 unreachable 中的每个对象销毁并在refchain链表中移除（不考虑缓存机制）。
至此，垃圾回收的过程结束。

https://pythonav.com/wiki/detail/6/88/#1.%20%E7%99%BD%E8%AF%9D%E5%9E%83%E5%9C%BE%E5%9B%9E%E6%94%B6
```



## 4.面试如何讲垃圾回收

 Python垃圾回收主要以引用计数为主，标记清除、分代回收为辅 



首先在Python中维护了一个refchain的双向环状链表，这个链表中存储程序创建的所有对象，每种类型的对象中都有一个ob_refcnt引用计数器的值，引用个数+1、-1，最后当引用计数器变为0时会进行垃圾回收（对象销毁、refchain中消除）



但是，在python中对于那些有多个元素的对象可能存在循环引用的问题，为了解决这个问题python又引入了标记清除和分代回收，即在其内部有4个链表

- refchain
- 0代   700个对象
- 1代    10次
- 2代    10次

在源码内部当达到各自的阀值时，就会触发扫描链表进行标记清除的动作（有循环则计数器各自-1）



但是，源码内部在上述的流程中提出了优化机制



## 5.Python缓存

#### 5.1 池(int类型)

为了避免重复创建和销毁常见对象，维护了一个池

```python
v1 = 7  # 内部不会开辟内存，直接去池中获取
v2 = 9  # 内部不会开辟内存，直接去池中获取
v3 = 9  # 内部不会开辟内存，直接去池中获取

# 按道理会创建两个对象加入到refchain链表中
# 但是启动解析器时，python内部帮我们创建：-5、-4、......257
# 内部不会开辟内存，直接去池中获取

print(id(v2), id(v3))
```



#### 5.2 free_list（float/list/tuple/dict）

当一个对象的引用计数器为0时，按理说应该回收，但是内部不会直接回收，而是将对象添加到free_list链表中当缓存，以后再去创建对象时，不再重新开辟内存，而是直接使用free_list

```python
v1 = 3.14   # 开辟内存，内部存储结构体中定义的那几个值，并添加到refchain中

del v1  # refchain中移除，将对象添加到free_list中（大小：80个对象左右）、free_list满了则销毁


v9 = 99.99  # 不会重新开辟内存，去free_list中获取对象，对象内部数据初始化，再放到refchain中
```

