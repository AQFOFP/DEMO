# 创建连接相关
import random
import time

from sqlalchemy import create_engine, func, and_, Date, desc

# 和 sqlapi 交互，执行转换后的 sql 语句，用于创建基类
from sqlalchemy.ext.declarative import declarative_base

# 创建表中的字段(列)
from sqlalchemy import Column

# 表中字段的属性
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy import UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship

# 创建连接对象，并使用 pymsql 引擎
conn_str = "mysql+mysqlconnector://root:root@127.0.0.1:3306/db_2006"
engine = create_engine(conn_str, encoding='utf-8', echo=False, pool_size=20, max_overflow=10, pool_recycle=14000)

# 创建基类
Base = declarative_base()


# 创建会话实例对象
Session = sessionmaker(bind=engine)
session = Session()


class Mony(Base):
    __tablename__ = 't_user_mony'
    id = Column(Integer, primary_key=True)
    uid = Column(String(32), nullable=False)  # 注册日期
    money = Column(Integer, nullable=False, default=0)
    recharge_date = Column(Date, nullable=False)


class OpBigR(Base):
    __tablename__ = 't_op_big_r'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(32), nullable=False)  # 注册日期
    loss_level = Column(Integer, nullable=False, default=0)
    last_30_charge = Column(Integer, nullable=False, default=0)


if __name__ == '__main__':
    results = session.query(Mony.uid, OpBigR.loss_level, func.sum(Mony.money).label('sum_money')).\
        join(OpBigR, and_(Mony.uid == OpBigR.user_id)).\
        filter(Mony.recharge_date >= '2021-02-01').\
        group_by(Mony.uid, OpBigR).\
        having(Column('sum_money') > 600).\
        order_by(desc('sum_money'))

    total_count = session.query(func.count(Mony.uid).label('count_uid'), func.sum(Mony.money).label('sum_money')).\
        filter(Mony.recharge_date >= '2021-02-01', Mony.recharge_date <= '2021-02-02').first()
    for rn, item in enumerate(results):
        print(item.uid, '----------', item.sum_money, '-----', item.loss_level)

    print(total_count)
    print(total_count.count_uid)
    print(total_count.sum_money)

    # session.query(Mony.uid, DailyRecharge.pay_type,
    #            func.sum(DailyRecharge.recharge_money).label('sum_money'),
    #            func.sum(DailyRecharge.recharge_diamond).label('sum_diamond'),
    #            ).filter(*filters, e_stamp - DailyRecharge.register_time < 30 * 12 * 60 * 60). \
    #     group_by(DailyRecharge.uid, DailyRecharge.pay_type). \
    #     order_by(desc('sum_money'))