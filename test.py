# coding:utf-8

import GUI
import time
# 提示语
# 欢迎光临 11
# 支付成功 12
# 水果重复 13

# 商品信息 2（商品名 21 单价 22 重量 23 ）
# 用户信息 3（userid 31 余额 32）

price = {'apple':9,'banana':12,'orange':10,'chair':20,'dog':100}
i=0
while True:
    print i
    GUI.addQueue(1)
    GUI.addQueue('欢迎光临')

    GUI.addQueue(2)
    fruit_type = 'apple'
    weight2 = 1.23

    GUI.addQueue('商品名称：' + fruit_type + '\n' + '单价(元/kg)：' + str(price[fruit_type]) + '\n' + '重量(kg)：' + str(weight2))

    time.sleep(0.5)

