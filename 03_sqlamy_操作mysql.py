# 创建连接相关
import random
import time

from sqlalchemy import create_engine, func, and_

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


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(12),
                  unique=True,  # 值必须唯一
                  nullable=False)  # 不允许为空
    full_name = Column(String(64), nullable=True)
    cn_name = Column(String(64))


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32),
                  unique=True,
                  index=True,  # 此列建立索引
                  nullable=False)
    group_id = Column(Integer,
                      ForeignKey('groups.id'),  # 定义外键
                      default=1)  # 默认值

    # 下面此列与创建表无关，仅用于查询使用，group 用于正向查询，user 用于反向查询
    group = relationship('Groups',  # 字符串类型的映射类名称。
                         backref='user')


class MonitorRoom(Base):
    __tablename__ = 't_monitor_room'
    room_type = Column(String(32), primary_key=True)
    room_id = Column(String(32), primary_key=True)

def init_db():
    """创建所有定义的表到数据库中"""
    Base.metadata.create_all(engine)


def drop_db():
    """从数据库中删除所有定义的表"""
    Base.metadata.drop_all(engine)


def init_data():
    session.add_all([
        Groups(name='Other', ),
        Groups(name='PM', full_name='Product Manager', cn_name='产品经理'),
        Groups(name='RD', full_name='Research and Development engineer', cn_name='开发'),
        Groups(name='QA', full_name='Product Manager', cn_name='测试'),
        Groups(name='OP', full_name='Product Manager', cn_name='运维'),
        Groups(name='DBA', full_name='Product Manager', cn_name='数据库管理员'),
    ])

    session.commit()

    session.add_all([
        Users(name='Yangge', group_id=2),
        Users(name='Tom', group_id=2),
        Users(name='Rose', group_id=3),
        Users(name='shark', group_id=3),
        Users(name='xiguatian', group_id=5),
        Users(name='Jack', group_id=6),
        Users(name='new_user'),
    ])

    session.commit()


class RoomTime(Base):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(Integer, primary_key=True)
    uid = Column(String(32), nullable=False)
    online_time = Column(Integer)


base_cls_tb_cfg={"RoomTime":["room_time",RoomTime],}
id_part_class_dict = dict()


def get_mysql_log_model(session, base_name, part_id=None):

    def get_month():
        now = int(time.time())
        today_gmt3_time_stamp = now - 9000
        today_gmt3_time_stamp_array = time.localtime(today_gmt3_time_stamp)
        month_s = time.strftime('%Y_%m', today_gmt3_time_stamp_array)
        return month_s

    part_id = part_id or get_month()
    base_list = base_cls_tb_cfg.get(base_name, ["s_unkown_table",None])
    base_table, base_obj = base_list[0], base_list[1]
    if base_obj:
        cls_name, table_name = base_name+'%s' % part_id, base_table+'_%s' % part_id
        if cls_name not in id_part_class_dict:
            cls = type(cls_name, (base_obj,), {'__tablename__': table_name})
            id_part_class_dict[cls_name] = cls
            session.execute("create table if not exists {} like {}".format(table_name,base_table))
            # global exists_table
            # if table_name not in exists_table:
            #     try:
            #         session.execute("create table if not exists %s like s_start_app" % table_name)
            #     except Exception as e:
            #         print("create table if not exists error={}".format(e))
            #     else:
            #         exists_table.add(table_name)

        return id_part_class_dict[cls_name]
    else:
        return None


if __name__ == '__main__':
    # # 执行创建表
    # init_db()
    #
    # # 初始化数据
    # init_data()
    start = '2020-12-27'
    end = '2021-01-02'
    date_nm_start = start[:7].replace('-', '_')  # 获取年月
    date_nm_end = end[:7].replace('-', '_')  # 获取年月
    RoomTimeStart = get_mysql_log_model(session, "RoomTime", part_id=date_nm_start)
    try:
        session.query(RoomTimeStart).filter(RoomTimeStart.uid == 'eee').update({RoomTimeStart.online_time:'yyyy'})
    except Exception as e:
        print(e)
        # session.commit()
        # session.close()





    # RoomTimeEnd = get_mysql_log_model(session, "RoomTime", part_id=date_nm_end)
    # # RoomTimeStart.
    #
    # # result1 = session.query(RoomTimeStart.online_time)
    # # result2 = session.query(RoomTimeEnd.online_time)
    # result1 = session.query(RoomTimeStart.uid, RoomTimeStart.online_time)
    # result2 = session.query(RoomTimeEnd.uid, RoomTimeEnd.online_time)
    # # res = result1.union_all(result2)
    # # res = result1.union_all(result2).having(func.sum(RoomTimeEnd.online_time)).scalar()
    # res = result1.union_all(result2).distinct(RoomTimeEnd.uid, RoomTimeEnd.online_time)
    # # print(result)
    # # for item in res:
    # #     print(item.uid)
    # print(res)
    #
    #
    #
