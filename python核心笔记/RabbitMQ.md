## RabbitMQ

### 一、Python 的 pika 库常用函数及参数说明

```python
1. pika.PlainCredentials(username, password, erase_on_connect)
功能:创建连接时的登录凭证
参数:
username: MQ 账号
password: MQ 密码
erase_on_connect: 删除连接上的凭据, 默认为 False
    
credentials = pika.PlainCredentials(username="guest", password="guest")



2. pika.ConnectionParameters(host, port, virtual_host, credentials)
功能: 连接 MQ 的参数设置
参数:
host: RabbitMQ IP 地址
port: RabbitMQ 端口
virtual_host: RabbitMQ 虚拟主机
credentials: 登录凭证
    
pika.ConnectionParameters(host='127.0.0.1', port=5672, virtual_host='/', credentials=credentials)


3. pika.BlockingConnection(parameters)
功能: 阻塞式连接 MQ
参数:
parameters: 连接参数(包含主机/端口/虚拟主机/账号/密码等凭证信息)
    
connect = pika.BlockingConnection(pika.ConnectionParameters(
    host='127.0.0.1', port=5672, virtual_host='/', credentials=credentials))

4. pika.channel(channel_number)
功能: 创建信道
参数:
channel_number: 信道个数, 一般采用默认值 None
    
channel = connect.channel()




5. channel.exchange_declare(callback,exchange,exchange_type,passive,durable,auto_delete,internal,nowait,arguments)
功能: 声明交换器
参数:
callback=None : 当 Exchange.DeclareOk 时 调用该方法, 当 nowait=True 该值必须为 None
exchange=None: 交换器名称,保持非空,由字母、数字、连字符、下划线、句号组成
exchange_type=‘direct’: 交换器类型
passive=False: 执行一个声明或检查它是否存在
durable=False: RabbitMQ 重启时保持该交换器的持久性,即不会丢失
auto_delete=False: 没有队列绑定到该交换器时,自动删除该交换器
internal=False: 只能由其它交换器发布-Can only be published to by other exchanges
nowait=False: 不需要 Exchange.DeclareOk 的响应-Do not expect an Exchange.DeclareOk response
arguments=None: 对该交换器自定义的键/值对, 默认为空

channel.exchange_declare(exchange='hello', exchange_type='direct', passive=False, durable=True, auto_delete=False)


6. channel.queue_declare(callback,queue,passive,durable,exclusive,auto_delete,nowait,arguments)
功能: 声明队列
参数:
callback : 当 Queue.DeclareOk 时的回调方法; 当 nowait=True 时必须为 None.
queue=’’ : 队列名称
passive=False : 只检查队列是否存在
durable=False : 当 RabbitMQ 重启时,队列保持持久性
exclusive=False : 仅仅允许当前的连接访问
auto_delete=False : 当消费者取消或者断开连接时, 自动删除该队列
nowait=False : 当 Queue.DeclareOk 时不需要等待
arguments=None : 对该队列自定义键/值对

channel.queue_declare(queue='hello')



7. channel.queue_bind(callback, queue, exchange,routing_key,nowait,arguments)
功能: 通过路由键将队列和交换器绑定
参数:
callback: 当 Queue.BindOk 时的回调函数, 当 nowait=True 时必须为 None
queue: 要绑定到交换器的队列名称
exchange: 要绑定的源交换器
routing_key=None: 绑定的路由键
nowait=False: 不需要 Queue.BindOk 的响应
arguments=None: 对该绑定自定义键/值对

 channel.queue_bind(queue='hello', exchange='hello', routing_key='world')


8. channel.basic_publish(exchange, routing_key, body, properties, mandatory, immediate)
功能: 将消息发布到 RabbitMQ 交换器上
参数:
exchange: 要发布的目标交换器
routing_key: 该交换器所绑定的路由键
body: 携带的消息主体
properties=None: 消息的属性,即文本/二进制等等
mandatory=False: 当 mandatory 参数设置为 true 时，交换机无法根据自身的路由键找到一个符合的队列，
那么 RabbitMQ 会调用 Basic.Return 命令将消息返回给生产者，
当 mandatory 参数设置为 false 时，出现上述情况，消息会被丢弃
immediate=False: 立即性标志

channel.basic_publish(exchange='hello',  routing_key='world',  properties=msg_props, body=message)


9. channel.basic_consume(consumer_callback, queue, no_ack, exclusive, consumer_tag, arguments)
功能: 从队列中拿到消息开始消费
参数:
consumer_callback: 意思是说,当要消费时,调用该回调函数 consumer_callback, 函数的参数有channel, method, properties,body

queue=’’: 要消费的消息队列
no_ack=False: 自动确认已经消费成功
exclusive=False: 不允许其它的消费者消费该队列
consumer_tag=None: 指定自己的消费标记
arguments=None: 对该消费者自定义设置键值对
    
def callback(channel, method, properties, body):
    # 消息确认
    channel.basic_ack(delivery_tag=method.delivery_tag)

    if body.decode('utf-8') == "quit":
        # 停止消费，并退出
        channel.basic_cancel(consumer_tag='hello-consumer')
        channel.close()
        connect.close()
    else:
        print("msg is {}".format(body))


channel.basic_consume(callback, queue='hello', no_ack=False)



10. channel.basic_ack()
功能: 消息确认
参数:
delivery_tag=0 : 服务端分配的传递标识
multiple=False
channel.basic_ack(delivery_tag=method.delivery_tag)


11. channel.basic_cancel(callback, consumer_tag, nowait)
功能: 取消消费, 该方法不会影响已经发送的消息,但是不会再发送新的消息给消费者
参数:
callback=None : 当 Basic.CancelOk 响应时的回调函数; 当 nowait=True 时必须为 None. 当 nowait=False 时必须是可回调的函数
consumer_tag=’’: 消费标识
nowait=False : 不期望得到 Basic.CancelOk response
    
channel.basic_cancel(consumer_tag='hello-consumer')



12. channel.start_consuming()
功能: 处理 I/O 事件和 basic_consume 的回调, 直到所有的消费者被取消
参数:
NA
channel.start_consuming()


13. channel.basic_reject(delivery_tag, requeue=True)
功能: 拒绝单条消息
参数:
delivery_tag : 传递标签
requeue=True : 是否重新放回到队列中去
channel.basic_reject()


14. channel.basic_nack(delivery_tag=None, multiple=False, requeue=True)
功能: 拒绝单条或者多条消息
参数:
delivery_tag=None : 传递标签
multiple=False : 是否批量,即多条消息   
requeue=True: 是否重新放回到队列中去
    
channel.basic_nack()


15. channel.exchange_delete(callback=None,exchange=None,if_unused=False,nowait=False)
功能: 删除已声明的交换器
参数:
callback=None: The function to call on Exchange.DeleteOk; MUST be None when nowait=True.
exchange=None: The exchange name
if_unused=False: only delete if the exchange is unused
nowait=False: Do not wait for an Exchange.DeleteOk
channel.exchange_delete()


16. pika.BasicProperties()
功能: 发送消息的属性
参数:
content_type=None,
content_encoding=None,
headers=None,
delivery_mode=None, 声明信息持久化, 使信息持久化，需要声明queue持久化和delivery_mode=2信息持久化
priority=None,
correlation_id=None,
reply_to=None,
expiration=None,
message_id=None,
timestamp=None,
type=None,
user_id=None,
app_id=None,
cluster_id=None

msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'


17. 回调函数 callback
功能: 回调函数
参数:
channel: 包含channel的一切属性和方法
method: 包含 consumer_tag, delivery_tag, exchange, redelivered, routing_key
properties: basic_publish 通过 properties 传入的参数
body: basic_publish发送的消息
def callback(channel, method, properties, body):
    # 消息确认
    channel.basic_ack(delivery_tag=method.delivery_tag)

    if body.decode('utf-8') == "quit":
        # 停止消费，并退出
        channel.basic_cancel(consumer_tag='hello-consumer')
        channel.close()
        connect.close()
    else:
        print("msg is {}".format(body))
```



### 二、exchange类型

```python
发布与订阅
RabbitMQ的发布与订阅，借助于交换机(Exchange)来实现。
交换机的工作原理：消息发送端先将消息发送给交换机，交换机再将消息发送到绑定的消息队列，而后每个接收端(consumer)都能从各自的消息队列里接收到信息。



Exchange有三种工作模式，分别为：Fanout, Direct, Topic
'''
模式1 Fanout

任何发送到Fanout Exchange的消息都会被转发到与该Exchange绑定(Binding)的所有Queue上
　　1.可以理解为路由表的模式
　　2.这种模式不需要routing_key(即使指定，也是无效的)
　　3.这种模式需要提前将Exchange与Queue进行绑定，一个Exchange可以绑定多个Queue，一个Queue可以同多个Exchange进行绑定。
　　4.如果接受到消息的Exchange没有与任何Queue绑定，则消息会被抛弃。

　　注意：这个时候必须先启动消费者，即订阅者。因为随机队列是在consumer启动的时候随机生成的，并且进行绑定的。producer仅仅是发送至exchange，并不直接与随机队列进行通信
'''


'''
模式2  Direct
路由键的工作原理：每个接收端的消息队列在绑定交换机的时候，可以设定相应的路由键。发送端通过交换机发送信息时，可以指明路由键 ，交换机会根据路由键把消息发送到相应的消息队列，这样接收端就能接收到消息了。　　

　　任何发送到Direct Exchange的消息都会被转发到routing_key中指定的Queue：
　　1.一般情况可以使用rabbitMQ自带的Exchange：””  (该Exchange的名字为空字符串)， 也可以自定义Exchange   
　　2.这种模式下不需要将Exchange进行任何绑定(bind)操作。当然也可以进行绑定。可以将不同的routing_key与不同的queue进行绑定，不同的queue与不同exchange进行绑定
　　3.消息传递时需要一个“routing_key”
　　4.如果消息中中不存在routing_key中绑定的队列名，则该消息会被抛弃。
　　如果一个exchange 声明为direct，并且bind中指定了routing_key,那么发送消息时需要同时指明该exchange和routing_key.
'''


'''
模式3 Topic
路由键模糊匹配，其实是路由键(routing_key)的扩展，就是可以使用正则表达式，和常用的正则表示式不同，这里的话“#”表示所有、全部的意思；“*”只匹配到一个词。

　　任何发送到Topic Exchange的消息都会被转发到所有关心routing_key中指定话题的Queue上
　　1.这种模式较为复杂，简单来说，就是每个队列都有其关心的主题，所有的消息都带有一个“标题”(routing_key)，Exchange会将消息转发到所有关注主题能与　　routing_key模糊匹配的队列。
　　2.这种模式需要routing_key，也许要提前绑定Exchange与Queue。
　　3.在进行绑定时，要提供一个该队列关心的主题，如“#.log.#”表示该队列关心所有涉及log的消息(一个routing_key为”MQ.log.error”的消息会被转发到该队列)。
　　4.“#”表示0个或若干个关键字，“*”表示一个关键字。如“log.*”能与“log.warn”匹配，无法与“log.warn.timeout”匹配；但是“log.#”能与上述两者匹配。
　　5.同样，如果Exchange没有发现能够与routing_key匹配的Queue，则会抛弃此消息。

　　具体代码这里不在多余写，参照第二种模式的就可以，唯一变动的地方就是exchange type的声明，以及进行绑定和发送的时候routing_key使用正则模式即可。
'''

```

