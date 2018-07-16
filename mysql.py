# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:48:39 2018

@author: lenovo
"""
import pymysql.cursors

connect = pymysql.Connect(
    host='192.168.43.192',#MySQL服务器地址
    port=3306,#MySQL服务器端口号
    user='myuser',
    passwd='123456',
    db='mysql',#数据库名称
    charset='utf8'#连接编码
)

# 获取游标
cursor = connect.cursor()

# 插入数据
def insert_data():
    sql = "INSERT INTO SC (user_id, user_money) VALUES ( '%s', '%d')"
    data = ('Mr.guo', 1500)
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')

# 修改数据
def change_data1(money,user_id):
    sql = "UPDATE SC SET user_money = %d WHERE user_id = '%s' "
    data = (money, user_id)
    cursor.execute(sql % data)
    connect.commit()
    print('成功修改', cursor.rowcount, '条数据')
    
def change_data(user_num,user_id):
    sql = "UPDATE SC SET user_num = %d WHERE user_id = '%s' "
    data = (user_num, user_id)
    cursor.execute(sql % data)
    connect.commit()
    print(u'成功修改', cursor.rowcount, u'条数据')

# 查询数据
#sql = "SELECT user_money FROM SC WHERE user_id = '%s'  "
def check_data():
    sql = "SELECT user_num FROM SC"
    cursor.execute(sql)
    return cursor.fetchall()
    #for row in cursor.fetchall():
        #print("Money:%.2f" % row)

def check_data1(user_id):
    sql = sql = "SELECT user_money FROM SC WHERE user_id = '%s'  "
    data = (user_id)
    cursor.execute(sql % data)
    return cursor.fetchall()

if __name__ == "__main__":

    money = check_data1('Mr.guo')
    print money

    change_data1(money[0][0]-1,'Mr.guo')

    money = check_data1('Mr.guo')
    print money




    '''
    change_data(1,'Jone Snow')
    row = check_data()
    sum = 0
    for i in row[1:]:
        sum = i[0]+sum
    print(sum)
    cursor.close()
    connect.close()
    '''
