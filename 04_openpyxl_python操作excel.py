

# openpyxl操作
from mongoengine import connect, Document, StringField, IntField
from openpyxl import Workbook

connect('mydb', host='localhost', port=27017)


class Users(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)


def savexl():
    users = Users.objects.all()  # 返回所有的文档对象列表
    wb = Workbook()
    _save_sheet = wb.active

    rowNum = 1
    _save_sheet.cell(row=rowNum, column=1).value = 'name'
    _save_sheet.cell(row=rowNum, column=2).value = 'age'

    for index, item in enumerate(users):
        e_pos = index + 1
        _save_sheet.cell(row=rowNum + e_pos, column=1).value = item.name
        _save_sheet.cell(row=rowNum + e_pos, column=2).value = item.age

    path = 'list_credit_charge_bill.xlsx'
    # 把文件保存到linux本地，
    wb.save(path)


if __name__ == '__main__':
    savexl()