# 创建连接相关
import random
import threading
import time

from sqlalchemy import create_engine, func, and_, Date, desc, case

# 和 sqlapi 交互，执行转换后的 sql 语句，用于创建基类
from sqlalchemy.ext.declarative import declarative_base

# 创建表中的字段(列)
from sqlalchemy import Column

# 表中字段的属性
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy import UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship, scoped_session

# 创建连接对象，并使用 pymsql 引擎
conn_str = "mysql+mysqlconnector://root:root@127.0.0.1:3306/db_2006"
engine = create_engine(conn_str, encoding='utf-8', echo=False, pool_size=10, max_overflow=10, pool_recycle=5)

# 创建基类
Base = declarative_base()


# 创建会话实例对象
Session = sessionmaker(bind=engine)



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


def th_ss():
    sess = Session()
    print(sess.query(Mony).filter(Mony.money >= 0).all())
    time.sleep(5)


if __name__ == '__main__':
    # filter_q = set()
    sess = Session()
    xpr = case([(Mony.uid == 'ccc', 'ccccv')], else_='ooo').label("full_name")
    dddc = sess.query(func.count(Mony.uid).label('dddd')).filter(Mony.money >= 0).first()
    # dddc = sess.query(Mony.uid, xpr).filter(Mony.money >= 0)
    # for item in dddc:
    print(dddc.dddd)
    # time.sleep(6)
    # print(sess.query(Mony).filter(Mony.money >= 0).all())





    # filter_q.add(Mony.uid.in_(['aaa']))
    # results = session.query(Mony.uid, func.sum(Mony.money).label('sum_money')).\
    #     group_by(Mony.uid).having(Column('sum_money').in_([436.00]))
    # print(results)
    # results1 = session.query(func.distinct(Mony.uid).label('d_uid')).filter(Mony.uid == 'bbb')
    # results2 = session.query(func.distinct(Mony.uid).label('d_uid')).filter(Mony.uid == 'ccc')
    # results3 = results.union(results2, results1)
    # print(results3)
    #
    # for rn, item in enumerate(results):
    #     print(item.uid, '----------', item.sum_money)

    # session.query(Mony.uid, DailyRecharge.pay_type,
    #            func.sum(DailyRecharge.recharge_money).label('sum_money'),
    #            func.sum(DailyRecharge.recharge_diamond).label('sum_diamond'),
    #            ).filter(*filters, e_stamp - DailyRecharge.register_time < 30 * 12 * 60 * 60). \
    #     group_by(DailyRecharge.uid, DailyRecharge.pay_type). \
    #     order_by(desc('sum_money'))