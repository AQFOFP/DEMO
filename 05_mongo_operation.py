from mongoengine import *

# mongo的orm操作
def mongoorm():
    connect('movies', host='localhost', port=27017)

    class GiftSendNum(Document):
        aid = StringField(default='')
        giftId = IntField(default=0)
        giftNum = IntField(default=0)
        mtime = IntField(default=0)
        meta = {'collection': 'giftSendNum', "strict": False, 'indexes': ['aid'], 'index_background': True}


    class DgGift(Document):
        aid = StringField(default='')
        giftId = IntField(default=0)
        giftNum = IntField(default=0)
        aidcount = IntField(default=0)
        meta = {'collection': 'dggift', "strict": False}

    send_alls = GiftSendNum.objects(giftId=102).all()

    for send in send_alls:
        uid = send.aid
        giftId = send.giftId
        giftNum = send.giftNum

        deal = DgGift.objects(aid=uid).first()
        print(f'deal with {uid}')
        if deal:
            deal.giftNum += send.giftNum
            deal.aidcount += 1
        else:
            DgGift(aid=uid, giftId=giftId, giftNum=giftNum, aidcount=1).save()


if __name__ == '__main__':
    print('start')
    mongoorm()
    print('end')