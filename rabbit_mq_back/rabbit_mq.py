"""
pip3 install pika=1.1.0
"""
import json

import pika

'''
任何发送到Fanout Exchange的消息都会被转发到与该Exchange绑定(Binding)的所有Queue上
　　1.可以理解为路由表的模式
　　2.这种模式不需要routing_key(即使指定，也是无效的)
　　3.这种模式需要提前将Exchange与Queue进行绑定，一个Exchange可以绑定多个Queue，一个Queue可以同多个Exchange进行绑定。
　　4.如果接受到消息的Exchange没有与任何Queue绑定，则消息会被抛弃。

　　注意：这个时候必须先启动消费者，即订阅者。因为随机队列是在consumer启动的时候随机生成的，并且进行绑定的。producer仅仅是发送至exchange，并不直接与随机队列进行通信。
'''


class RabbitmqBox(object):
    def __init__(self, username, password, host, port=5672, virtual_host='/'):
        self.cred = pika.PlainCredentials(username=username, password=password)
        self.host = host
        self.port = port
        self.virtual_host = virtual_host
        self.connection = None
        self.channel = None
        self.queues = list()
        self.exchange = ''
        self.routing_key = ''

    def connect_server(self, exchange='', ex_type=''):
        '''

        :param exchange: exchange表示交换机名称
        :param ex_type: type表示类型  主要三种: fanout, direct, topic
        1、默认交换机情况下：消息放到一个队列中，只能给一个消费者消费
        2、fanout模式的交换机：发送到Fanout Exchange的消息都会被转发到与该Exchange绑定(Binding)的所有Queue上
        :return:
        '''
        if self.connection is None or self.connection.is_closed:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=self.host, port=self.port, virtual_host=self.virtual_host, credentials=self.cred))
            self.channel = self.connection.channel()

        if exchange and ex_type:
            self.channel.exchange_declare(exchange=exchange, exchange_type=ex_type)
            self.exchange = exchange

    def publish_to_queue(self, msg, queue_name=None, routing_key='', queue_durable=True, properties=None, mandatory=False):
        '''

        :param queue_name: 队列名称, 在fanout, direct, topic可不传
        :param routing_key: 关键字
        :param msg:
        :param queue_durable: 当 RabbitMQ 重启时,队列保持持久性
        :param properties:
        :param mandatory:
        :return:
        1、声明队列：queue_declare(queue_name, durable=queue_durable)  # durable=True: 声明队列持久化
        如果仅仅是设置了队列的持久化，仅队列本身可以在rabbit-server宕机后保留，
        队列中的信息依然会丢失，\

        2: 如果想让队列中的信息或者任务保留，还需要做以下设置：
        channel.basic_publish(exchange='',
                              routing_key="test_queue",
                              body=message,
                              properties=pika.BasicProperties(
                                 delivery_mode = 2, # 使消息或任务也持久化存储
                              ))

        3:
            消息队列持久化包括3个部分：
            　　（1）exchange持久化，在声明时指定durable => 1
            　　（2）queue持久化，在声明时指定durable => 1
            　　（3）消息持久化，在投递时指定delivery_mode=> 2（1是非持久化）

            如果exchange和queue都是持久化的，那么它们之间的binding也是持久化的。
            如果exchange和queue两者之间有一个持久化，一个非持久化，就不允许建立绑定。
        '''
        if not self.exchange:
            self.routing_key = queue_name

            if not self.queues or queue_name not in self.queues:
                self.channel.queue_declare(queue_name, durable=queue_durable)  # durable=True: 声明队列持久化
                self.queues.append(queue_name)

            if queue_durable and properties is None:
                properties = pika.BasicProperties(delivery_mode=2)
        else:
            self.routing_key = routing_key

        self.channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=msg, properties=properties,
                                   mandatory=mandatory)

    def consume_from_queue(self, queue_name='', routing_keys='', queue_durable=True, callback=None, auto_ack=False, **kwargs):
        '''

        :param queue_name:
        :param routing_keys:
        :param queue_durable:
        :param callback:
        :param auto_ack:
        :param kwargs:
        :return:
        '''
        if not self.exchange:
            if queue_name not in self.queues:
                self.channel.queue_declare(queue_name, durable=queue_durable)
                self.queues.append(queue_name)

        else:
            # 随机创建队列, exclusive=True表示建立临时队列，当consumer关闭后，该队列就会被删除
            queue_name = self.channel.queue_declare(queue=queue_name, exclusive=True).method.queue

            if isinstance(routing_keys, str):
                # 将队列与exchange进行绑定
                self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=routing_keys)
            else:
                for item in routing_keys:
                    self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=item)

        # no_ack=True表示在回调函数中不需要发送确认标识
        self.channel.basic_consume(queue_name, callback, auto_ack=auto_ack, **kwargs)
        self.channel.start_consuming()
        self.channel.stop_consuming()

    def __enter__(self):
        print('open-----------------------')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print('close----------------------')
        self.connection.close()


