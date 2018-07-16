# -*- coding: utf-8 -*-

import serial
import string  
import binascii

ser = serial.Serial('/dev/rfcomm0',9600,timeout=None)

print (ser.name)#打印设备名称
print (ser.port)#打印设备名

weight1 = 0.0
weight2 = 0.0


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

    print(weight)

ser.close()


'''
实例网址https://blog.csdn.net/u012611644/article/details/79125234

timeout=None            # 永远等待，直到有数据传过来（阻塞）    
timeout=0               # 不等待，收不到数据直接退出读取（非阻塞）    
timeout=x               # 设定等待时间（阻塞，x可以为浮点数）   

ser=serial.Serial("/dev/ttyUSB0",9600,timeout=0.5) #使用USB连接串行口
ser=serial.Serial("/dev/ttyAMA0",9600,timeout=0.5) #使用树莓派的GPIO口连接串行口
ser=serial.Serial(1,9600,timeout=0.5)#winsows系统使用com1口连接串行口
ser=serial.Serial("com1",9600,timeout=0.5)#winsows系统使用com1口连接串行口
ser=serial.Serial("/dev/ttyS1",9600,timeout=0.5)#Linux系统使用com1口连接串行口
print ser.name#打印设备名称
print ser.port#打印设备名
ser.open()

s = ser.read(10)#从端口读10个字节
ser.write("hello")#向端口些数据
ser.close()#关闭端口
        data = ser.read(20) #是读20个字符

        data = ser.readline() #是读一行，以/n结束，要是没有/n就一直读，阻塞。

        data = ser.readlines()和ser.xreadlines()#都需要设置超时时间

        ser.baudrate = 9600 #设置波特率

        ser.isOpen() #看看这个串口是否已经被打开
'''
