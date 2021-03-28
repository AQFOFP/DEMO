import json

# from rabbit_mq import RabbitmqBox
from rabbit_mq_back.rabbit_mq import RabbitmqBox

if __name__ == '__main__':
    rabbit_config = {
        'username': 'guest',
        'password': 'guest',
        'host': '127.0.0.1',
        'port': 5672,
    }

    print("**** start write fanout process ****")
    client = RabbitmqBox(**rabbit_config)
    client.connect_server(exchange='logs_topic', ex_type='topic')
    for item in range(1, 10):

        data = {
            'stype': 'mic',
            'uid': 'adbbddd',
            'source_id': '123' + str(item),
        }

        client.publish_to_queue(msg=json.dumps(data), routing_key='anonymous.info')

    client.connection.close()
