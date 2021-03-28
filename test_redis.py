from redis import Redis

if __name__ == '__main__':
    dd = {1: [{'rank': 1, 'name': 'هههههههه', 'head': 'https://cdn3.qmovies.tv/youstar/s5.png', 'rid': 1003943, 'tagType': 1},
              {'rank': 2, 'name': 'Flower', 'head': 'https://cloudcdn.qmovies.tv/5cb6fc80644f8e002a90cfc2/123333/h_1597648530.jpg', 'rid': 123335, 'tagType': 1}],
          2: [{'rank': 1, 'name': 'Flower', 'head': 'https://cloudcdn.qmovies.tv/5cb6fc80644f8e002a90cfc2/123333/h_1597648530.jpg', 'rid': 123335, 'tagType': 1},
              {'rank': 2, 'name': 'هههههههه', 'head': 'https://cdn3.qmovies.tv/youstar/s5.png', 'rid': 1003943, 'tagType': 1}]}
    for k, v in dd.items():
        print(k, v)