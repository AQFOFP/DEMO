import json

from rabbit_mq_back.rabbit_mq import RabbitmqBox


def handle_write(channel, method, properties, body):

    data = json.loads(body)
    print("handle body: {},  data:{}".format(body, data))
    stype = data.get('stype')
    uid = data.get('uid')
    source_id = data.get('source_id')
    num = data.get('num')
    diamond = data.get('diamond')
    day = data.get('day')
    act_type = data.get('act_type')
    title = data.get('title')
    act_desc = data.get('act_desc')
    try:
        print("success handle data:{}".format(data))
    except Exception as ex:
        print("handle data error, data: {} ex:{}".format(body, ex))
    else:
        channel.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    rabbit_config = {
        'username': 'guest',
        'password': 'guest',
        'host': '127.0.0.1',
        'port': 5672,
    }
    print("**** start write heart record process ****")
    client = RabbitmqBox(**rabbit_config)
    client.connect_server(exchange='logs_fanout', ex_type='fanout')
    client.consume_from_queue(callback=handle_write)
