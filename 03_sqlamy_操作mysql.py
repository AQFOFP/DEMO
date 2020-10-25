# 创建连接相关
from sqlalchemy import create_engine

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


if __name__ == '__main__':
    # # 执行创建表
    # init_db()
    #
    # # 初始化数据
    # init_data()

    user_objs = session.query(Users).filter(Users.name.like('%P%')).all()
    # print(user_objs)
    for item in user_objs:
        item.name = item.name.replace('P', 'HTTP')
        session.add(item)
    session.commit()

