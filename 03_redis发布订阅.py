import os
import pickle
import threading
import time
import uuid

import redis
from rediscluster import RedisCluster

cache_startup_nodes = [
    {"host": "149.129.109.88", "port": "6390"},
    {"host": "149.129.109.88", "port": "6391"},
    {"host": "149.129.109.88", "port": "6392"},
]


sub_rds = RedisCluster(startup_nodes=cache_startup_nodes, password="123456")


# # redis的发布订阅模式

def broadcast_message(channel, msg_body):  # 广播消息
    """
    广播消息
    :param channel:
    :param msg_body:
    :return:
    """
    a = 0

    while True:

        msg_id = uuid.uuid1().hex
        message = {"msg_id": msg_id, "msg_body": msg_body}
        _channel = "message:{}".format(channel)
        _message = pickle.dumps(message)
        sub_rds.publish(_channel, _message)  # 向频道_channel 发送message消息

        threadid = threading.current_thread().ident
        print(f'线程{threadid}发布消息：{message}')
        time.sleep(5)
        a += 1

        if a == 5:
            break


def subscribe_recevice(channel):  # 订阅消息
    ps = sub_rds.pubsub()  # redis的发布订阅模式
    ps.subscribe(f"message:{channel}")  # 订阅消息send_gift

    while True:
        try:
            ps_message = ps.get_message(ignore_subscribe_messages=True)  # 获取消息
            time.sleep(1)
            if not ps_message:
                time.sleep(0.04)
                continue

            _message_data = ps_message.get('data', b'') or b''

            if not _message_data:
                continue

            else:
                threadid = threading.current_thread().ident  # 获取当前线程信息
                _message = pickle.loads(_message_data)
                print(f'线程{threadid}接受到消息：', _message, type(_message))

        except Exception as e:
            # log.exception(e)
            print(e)
            time.sleep(1)


if __name__ == '__main__':
    '''
    # 实现功能：两个线程
    线程1：给redis每5秒发布一个消息
    线程2：订阅线程1发布的消息
    线程3：订阅线程1发布的消息
    '''
    message = {'name': 'zhangsan'}
    t1 = threading.Thread(target=broadcast_message, args=('send_gift', message))
    t2 = threading.Thread(target=subscribe_recevice, args=('send_gift',))
    t3 = threading.Thread(target=subscribe_recevice, args=('send_gift',))
    t1.start()
    t2.start()
    t3.start()

    t1.join()   # 主线程等待线程t1结束才往下执行
    print('1111111111111')

    t2.join()
    t3.join()
