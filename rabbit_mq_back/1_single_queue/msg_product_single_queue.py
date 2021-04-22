import json

from rabbit_mq_back.rabbit_mq import RabbitmqBox

if __name__ == '__main__':
    rabbit_config = {
        'username': 'guest',
        'password': 'guest',
        'host': '127.0.0.1',
        'port': 5672,
    }

    print("**** start write heart record process ****")
    # client = RabbitmqBox(**rabbit_config)
    # client.connect_server()
    # queue_name = "resource_distribute"
    # for item in range(1, 10):
    #
    #     data = {
    #         'stype': 'mic',
    #         'uid': 'adbbddd',
    #         'source_id': '123' + str(item),
    #     }
    #
    #     client.publish_to_queue(queue_name=queue_name, msg=json.dumps(data))
    #
    # client.connection.close()
    with RabbitmqBox(**rabbit_config) as client:
        client.connect_server()
        queue_name = "resource_distribute"
        # for item in range(1, 10):

        data = {
            'stype': 'mic',
            'uid': 'adbbddd',
            'source_id': '123' + str(111),
        }

        client.publish_to_queue(queue_name=queue_name, msg=json.dumps(data))