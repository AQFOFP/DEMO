import threading
import time

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
    ["127.0.0.1:9200"],  # 连接集群，以列表的形式存放各节点的IP地址,master分支
)


def insert():
    '''
    　　create：必须指定待查询的idnex、type、id和查询体body；缺一不可，否则报错 
　　    index：相比于create，index的用法就相对灵活很多；id并非是一个必选项，如果指定，则该文档的id就是指定值，
              若不指定，则系统会自动生成一个全局唯一的id赋给该文档。 
              若id存在，则为更新记录，否则为创建记录
    '''
    body = {"name": 'lucy', 'sex': 'female', 'age': 11}
    rt = es.index(index='school', doc_type='students', id=1, body=body)
    print(rt)  # 成功返回字典(包含index、tyoe等信息)

    # # 插入数据,index，doc_type名称可以自定义，id可以根据需求赋值,body为内容
    # es.index(index="my_index", doc_type="test_type", id=0, body={"name": "python", "addr": "深圳"})
    # es.index(index="my_index", doc_type="test_type", id=1, body={"name": "python", "addr": "深圳"})
    #
    # # 同样是插入数据，create() 方法需要我们指定 id 字段来唯一标识该条数据，而 index() 方法则不需要，如果不指定 id，会自动生成一个 id
    # es.create(index="my_index", doc_type="test_type", id=2, body={"name": "python", "addr": "深圳"})

def query():
    # get：指定index、type、id,查询所对应的文档
    rt = es.get(index='school', doc_type='students', id=1)
    print(rt, type(rt))


def delete():
    # delete：删除指定index、type、id的文档
    rt = es.delete(index='school', doc_type='students',  id=1)
    print(rt, type(rt))


def update():
    # update：跟新指定index、type、id所对应的文档
    es.update(index='indexname', doc_type='typeName', id='idValue', body={待更新字段})


def query_condition():
    # 条件查询
    query = {'query': {'match_all': {}}}  # 查找所有文档
    # query = {'query': {'term': {'name': 'jack'}}}  # 查找名字叫做jack的所有文档
    # query = {'query': {'range': {'age': {'gt': 11}}}}  # 查找年龄大于11的所有文档
    allDoc = es.search(index='indexname', doc_type='typeName', body=query)
    print(allDoc)


def delete_condition():
    # 条件删除
    query = {'query': {'match': {'sex': 'famale'}}}  # 删除性别为女性的所有文档
    query = {'query': {'range': {'age': {'lt': 11}}}}  # 删除年龄小于11的所有文档
    es.delete_by_query(index='indexname', body=query, doc_type='typeName')



def es_crud():
    # for i in range(n, n+1000):
    #     body = {"name": 'lucy'+str(i), 'sex': 'female', 'age': 11+i}
    #     print(es.index(index='school', doc_type='students', body=body))

    query = {'query': {'match_all': {}}}
    while True:
        result_es_count = es.count(index="school", doc_type="students", body=query, ignore=404)
        print(f'总记录数：{result_es_count["count"]}')
        # # if result_es_count['count'] == 0:
        # #     break
        #
        try:
            params = {'size': 10,
                      'refresh': 'true'
                      }
            print(es.delete_by_query(index='school', doc_type='students', body=query, params=params))  # 通过查询删除数据
            # time.sleep(1)
        except Exception as e:
            print(e)


def create_es_data():
    body = {
        'uid': 'abc3',
        'changed': -544,
        'balance': 453,
        'title': 'googlePayCharge',
        'desc': 'buy product_coins_diamonds3',
        'atype': 5,
        'mtime': 1587933046
    }
    es.index(index='youstar', doc_type='diamond', body=body)


if __name__ == '__main__':
    # create_es_data()
    # body_search = {
    #     "size": 0,
    #     'query': {
    #         'bool': {
    #             # 'filter': {},
    #             # 'filter': {'term': {'atype': 1}},
    #             'filter': [{"range": {"mtime": {"gte": 1587933011, "lte": 1587933055}}},
    #                        {"range": {'changed': {"lt": 0}}},
    #                        ],
    #         }
    #     },
    #     "aggs": {
    #             'record_count_ll': {
    #                 "terms": {
    #                     "field": "uid.keyword",
    #                 },
    #                 'aggs': {
    #                     'sub_beans': {
    #                         'sum': {'field': 'changed'}
    #                     },
    #                     # "having": {
    #                     #     "bucket_selector": {
    #                     #         "buckets_path": {
    #                     #             "orderCount": "_count",
    #                     #         },
    #                     #         "script": "params.orderCount ==1"
    #                     #     }
    #                     # }
    #                 }
    #             }
    #         },
    # }
    #
    # sub_beans = {
    #     "size": 0,
    #     'query': {
    #         'bool': {
    #             'filter': [{"range": {"mtime": {"gte": 1587933011, "lte": 1587933055}}},
    #                        {"range": {'changed': {"lt": 0}}},
    #                        ],
    #         }
    #     },
    #     "aggs": {
    #      "record_count_ll": {
    #        "sum": {
    #          "field": "changed"
    #        }
    #      }
    #     }
    # }
    user_list = ['abc3']
    body_search = {"from": 0, "size": 10000,
                   "query": {
                       "bool": {"filter": [{"range": {"mtime": {"gte": 1587933011, "lte": 1587933055}}},
                                           {"terms": {"atype": ["1"]}},
                                           {"terms": {"title": ["ApplePayCharge"]}}
                                           ]}},
                   # "sort": [{"mtime": {"order": "DESC"}}],
                   }

    # result_es = es_bak.search(index="money_detail2_es", doc_type="politics", body=body_search, ignore=404)
    #
    # ret = result_es['hits']['hits']

    result_es = es.search(index="youstar", doc_type="diamond", body=body_search, ignore=404)
    online_res = result_es['hits']['hits']
    # online_res = result_es['aggregations']['record_count_ll']['value']
    # online_res = result_es['aggregations']['record_count_ll']['buckets']
    # print(online_res)
    for item in online_res:
        print(item)


    # https://blog.csdn.net/xuezhangjun0121/article/details/80745575

