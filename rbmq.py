import pika

# rabbitmq develop config
rabbit_config_dev = dict(
    username="rabbitadmin",
    password="1GNCQTAuMsLnt1Xw0NSxow",
    host="127.0.0.1",
    port=5672
)
# rabbitmq production config
# rabbit_config_pro = dict(
#     username="rabbitadmin",
#     password="1GNCQTAuMsLnt1Xw0NSxow",
#     host="172.31.42.20",
#     port=5672
# )


class RabbitmqBox(object):
    def __init__(self, username, password, host, port=5672, virtual_host='/'):
        self.cred = pika.PlainCredentials(username=username, password=password)
        self.host = host
        self.port = port
        self.virtual_host = virtual_host
        self.connection = None
        self.channel = None
        self.queues = list()
        self.exchanges = list()

    def connect_server(self):
        if self.connection is None or self.connection.is_closed:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=self.host, port=self.port, virtual_host=self.virtual_host, credentials=self.cred))
            self.channel = self.connection.channel()

    def publish_to_queue(self, queue_name, msg, queue_durable=True, properties=None, mandatory=False):
        if not self.queues or queue_name not in self.queues:
            self.channel.queue_declare(queue_name, durable=queue_durable)
            self.queues.append(queue_name)
        if queue_durable and properties is None:
            properties = pika.BasicProperties(delivery_mode=2)
        self.channel.basic_publish(exchange="", routing_key=queue_name, body=msg, properties=properties,
                                   mandatory=mandatory)

    def consume_from_queue(self, queue_name, queue_durable=True, callback=None, auto_ack=False, **kwargs):
        if queue_name not in self.queues:
            self.channel.queue_declare(queue_name, durable=queue_durable)
            self.queues.append(queue_name)

        self.channel.basic_consume(queue_name, callback, auto_ack=auto_ack, **kwargs)
        self.channel.start_consuming()


client = RabbitmqBox(**rabbit_config_dev)
client.connect_server()
