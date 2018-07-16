# coding:utf-8

from Tkinter import *
import threading
import time
import Queue

msgQueue = Queue.Queue()

def addQueue(canPass):
    msgQueue.put(canPass)

def show():
    def labelSelect():
        while True:
            if msgQueue.empty():
                continue
            canPass = msgQueue.get()
            if canPass == 1:
                var1.set(msgQueue.get())
            elif canPass == 2:
                var2.set(msgQueue.get())
            elif canPass == 3:
                var3.set(msgQueue.get())
                time.sleep(3)
            else:
                var1.set('欢迎光临')
                var2.set('')
                var3.set('')
            time.sleep(0.01)


    root = Tk()

    root.title("结算系统")  # 窗口标题
    root.geometry('1280x720')  # 是x 不是*
    root.resizable(width=False, height=False)  # 宽, 高不可变

    var1 = StringVar()  # 设置变量
    var2 = StringVar()
    var3 = StringVar()

    l1 = Label(root, textvariable=var1, font=("楷体", 50), justify='left', fg='blue', width=500, height=3)  # 提示语label
    l2 = Label(root, textvariable=var2, font=("楷体", 30), justify='left',width=35, height=3)  # 商品信息label
    l3 = Label(root, textvariable=var3, font=("楷体", 30), justify='left',width=35, height=3)  # 用户信息label

    l1.pack()
    l2.pack(side  = LEFT)
    l3.pack(side  = RIGHT)

    th1 = threading.Thread(target=labelSelect,args=())
    th1.setDaemon(True)  # 守护线程
    th1.start()

    root.mainloop()

th=threading.Thread(target=show,args=())
th.setDaemon(True) # 守护线程
th.start()
