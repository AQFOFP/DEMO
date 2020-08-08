# 1.宰牲节活动(钻石发放=>分布式事务锁)
#
# 定义：
import time


from rediscluster import RedisCluster

redis_nodes = [
    {'host': '149.129.109.88', 'port': 6380},
    {'host': '149.129.109.88', 'port': 6381},
    {'host': '149.129.109.88', 'port': 6382},
]

# lock_rds = redis.StrictRedis(db=0, **redis_6380)
lock_rds = RedisCluster(startup_nodes=redis_nodes, password='123456')


class DistributedLock(object):
    """
    分布式锁,基于Redis的setNx特性实现
    name 请根据锁定的资源名称制定，不要随意使用相同的名称，避免相同的资源锁名
    # nx 表示当name不存在时才设置key=value
    """

    def __init__(self, name, timeout=2, ex=10, slp=0.4):
        self.name = name
        self.trys = timeout
        self.ex = ex
        self.slp = slp
        self.ts = time.time()

    def __enter__(self):
        locked = self._try_lock()
        if not locked: raise Exception("Distributed Lock Timeout.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._release()

    def _try_lock(self):
        """尝试得到锁，超时返回False"""
        rds = lock_rds
        while True:
            locked = rds.set(self.name, 1, ex=self.ex, nx=True)
            if locked: return True
            if time.time() - self.ts >= self.trys: return False
            time.sleep(self.slp or 1)

    def _release(self):
        """删除资源"""
        rds = lock_rds
        rds.delete(self.name)
        return True






if __name__ == '__main__':
    # 使用
    with DistributedLock("change_beans_abc1", ex=30) as lock:
        print('666')
        # lock_rds.set("cluster_nx1", 1, ex=30, nx=True)
        # print(lock_rds.exists("change_beans_abc"))
