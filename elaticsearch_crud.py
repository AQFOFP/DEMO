from elasticsearch import Elasticsearch

# 默认host为localhost,port为9200.但也可以指定host与port

#
# es = Elasticsearch(
#             ['address'],
#             http_auth=('user_name', 'password'),
#             port=9200,
#             use_ssl=False
#         )

# 无密码，自己搭建的
es = Elasticsearch(
    ["127.0.0.1:9200"],  # 连接集群，以列表的形式存放各节点的IP地址
)


def insert():
    '''
    　　create：必须指定待查询的idnex、type、id和查询体body；缺一不可，否则报错 
　　    index：相比于create，index的用法就相对灵活很多；id并非是一个必选项，如果指定，则该文档的id就是指定值，
              若不指定，则系统会自动生成一个全局唯一的id赋给该文档。 
    '''
    body = {"name": 'lucy', 'sex': 'female', 'age': 10}
    es.index(index='indexname', doc_type='typeName', body=body)

    # # 插入数据,index，doc_type名称可以自定义，id可以根据需求赋值,body为内容
    # es.index(index="my_index", doc_type="test_type", id=0, body={"name": "python", "addr": "深圳"})
    # es.index(index="my_index", doc_type="test_type", id=1, body={"name": "python", "addr": "深圳"})
    #
    # # 同样是插入数据，create() 方法需要我们指定 id 字段来唯一标识该条数据，而 index() 方法则不需要，如果不指定 id，会自动生成一个 id
    # es.create(index="my_index", doc_type="test_type", id=2, body={"name": "python", "addr": "深圳"})

def query():
    # get：获取指定index、type、id所对应的文档
    es.get(index='indexname', doc_type='typeName')


def delete():
    # delete：删除指定index、type、id的文档
    es.delete(index='indexname', doc_type='typeName', id='idValue')





def update():
    # update：跟新指定index、type、id所对应的文档
    es.update(index='indexname', doc_type='typeName', id='idValue', body={待更新字段})


def bulkquery():
    # 条件查询
    query = {'query': {'match_all': {}}}  # 查找所有文档
    # query = {'query': {'term': {'name': 'jack'}}}  # 查找名字叫做jack的所有文档
    # query = {'query': {'range': {'age': {'gt': 11}}}}  # 查找年龄大于11的所有文档
    allDoc = es.search(index='indexname', doc_type='typeName', body=query)
    print(allDoc)



def bulkdelete():
    # 条件删除
    query = {'query': {'match': {'sex': 'famale'}}}  # 删除性别为女性的所有文档
    query = {'query': {'range': {'age': {'lt': 11}}}}  # 删除年龄小于11的所有文档
    es.delete_by_query(index='indexname', body=query, doc_type='typeName')


if __name__ == '__main__':
    bulkquery()
    # https://blog.csdn.net/xuezhangjun0121/article/details/80745575

