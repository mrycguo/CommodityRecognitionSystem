# coding:utf-8

import camera as cam
import recognition as recg
import GUI
import time

import serial
import binascii
import face

import sys
reload(sys)
sys.setdefaultencoding('utf8')

ser = serial.Serial('/dev/rfcomm0',9600,timeout=None)
GUI.addQueue(1)
GUI.addQueue('欢迎光临')

print (ser.name)#打印设备名称
print (ser.port)#打印设备名

weight1 = 0.0
weight2 = 0.0

price = {'apple':9,'banana':12,'orange':10,'chair':20,'dog':100}
wait_flag = False  # 当同时识别到多种水果时 置位该flag 等待用户重新称重
while True:
    data1 = str(binascii.hexlify(ser.read(1)))
    data2 = str(binascii.hexlify(ser.read(1)))#读小数数据
    # print data1
    # print data2
    data1 = '0x'+data1
    data2 = '0x'+data2

    data2=int(data2,16)#字符串装16进制
    data2=int(data2)#16转10

    data1=int(data1,16)
    data1=int(data1)

    weight =data1 + data2*0.01#重量（kg）
    if weight >20.0:  # 噪声滤出
        continue
    print(weight)

    weight1 = weight2
    weight2 = weight
    if weight2 < 0.03 and abs(weight1 - weight2)<0.02 :
        wait_flag = False
    if wait_flag:
        GUI.addQueue(1)
        GUI.addQueue('请提走您的商品')
        print '等待用户'
        continue
    else:
        GUI.addQueue(0)

    if abs(weight1 - weight2)<0.02 and weight2 >0.03:
        print 'w1-w2: '+str(weight1 - weight2)+ '  w2: '+str(weight2)
        cam.getFruitImage()
        fruit_type = recg.recg()
        print 'start ' + fruit_type + ' end'

        if fruit_type!='':
            if fruit_type == 'error':
                GUI.addQueue(1)
                GUI.addQueue('系统检测到多种商品，请分开称重')
                print('系统检测到多种水果，请分开称重')
                time.sleep(5)
            else:
                GUI.addQueue(2)
                GUI.addQueue( '商品名称：'+fruit_type+'\n' + '单价(元/kg)：'+str(price[fruit_type])+'\n' + '重量(kg)：'+str(weight2))
                print fruit_type
                print '水果重量为：',
                print weight2
                print '正准备支付'
                GUI.addQueue(1)
                GUI.addQueue('请正对摄像头以完成支付')
                user_id,balance = face.pay_check(price[fruit_type]*weight2) #返回余额
                GUI.addQueue(1)
                GUI.addQueue('支付成功，欢迎下次光临')
                print user_id,balance
                GUI.addQueue(3)
                GUI.addQueue(('会员名：' + user_id + '\n')
                             + ('本次消费(元)：' + str(price[fruit_type]*weight2) + '\n')
                             + ('账户余额(元)：' + str(balance)))
                wait_flag = True


ser.close()
recg.re



