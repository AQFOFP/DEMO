from rediscluster import RedisCluster

# from qh_public.redis_tools import fun_cache_rds

import socket

'''

"""根据db_server区分正式服和测试服"""
is_debug = True
db_server = socket.gethostbyname('db_server')
# 此处默认正式服在finder上
if db_server == '172.31.11.226':
    is_debug = False

startup_nodes = [
    {"host": "172.31.7.70", "port": "6379"},
    {"host": "172.31.7.70", "port": "6380"},
    {"host": "172.31.7.70", "port": "6381"},
]
'''
cache_startup_nodes = [
    {"host": "149.129.109.88", "port": "6390"},
    {"host": "149.129.109.88", "port": "6391"},
    {"host": "149.129.109.88", "port": "6392"},
]

cache_startup_nodes = [
    {"host": "149.129.109.88", "port": "6380"},
    {"host": "149.129.109.88", "port": "6381"},
    {"host": "149.129.109.88", "port": "6382"},
]


# redis_conn = fun_cache_rds if is_debug else RedisCluster(startup_nodes=startup_nodes, password="kdib2nd$&H#")

cache_redis_conn = RedisCluster(startup_nodes=cache_startup_nodes, password="123456")
cache_redis_conn.set('name', '666')
print(cache_redis_conn.get('name'))
print('22222')