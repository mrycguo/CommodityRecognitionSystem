# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:44:11 2018

@author: lenovo
"""

import requests
from json import JSONDecoder
import time
import cv2
import os
import mysql


key ="wUkL-ctNFvh_f6A-Qp9b2bTKaPyn1I3I"
secret ="1JEHsrIholzaA2v91LkW4JL9F1G-LzB9"
filepath1 ="mosh1.jpg"
filepath2 = "mayun2.jpg"
filepath3 = "mayun.jpg"
data = {"api_key":key, "api_secret": secret}

#files = {"image_file": open(filepath1, "rb")}
#cap = cv2.VideoCapture(0)

def detect_face(filepath):#传入图片文件
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}
    response = requests.post(http_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def detect_face_64(filepath):#传入base64编码
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}

    response = requests.post(http_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def set_face():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    params = {
            'api_key':key,
            'api_secret':secret,
            
            }
    r = requests.post(url,data = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict


def compare(faceId1, faceId2):
    params = {}
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    params['face_token1'] = faceId1
    params['face_token2'] = faceId2
    params['api_key'] = key
    params['api_secret'] = secret
    r = requests.post(url, params)
    return r.json()

def addface(faceset,facetokens):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'
    params = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset,
            'face_tokens':facetokens
            }
    r = requests.post(url,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def get_face_set():
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
    params = {
            'api_key':key,
            'api_secret':secret,
            }
    r = requests.post(url,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict
    
def delete_faceset(faceset_token,check_empty):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/delete'
    params = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token,
            'check_empty':check_empty
            }
    r = requests.post(url,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def faceset_update(faceset_token,display_name,user_data):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/update'
    params = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token,
            'display_name':display_name,
            'user_data':user_data
            }
    r = requests.post(url,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def faceset_getdetail(faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'
    params = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token,
            }
    r = requests.post(url,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def face_compare(image_file1,face_token2):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'
    files = {"image_file1": open(image_file1, "rb")}
    params = {
            'api_key':key,
            'api_secret':secret,
            'face_token2':face_token2
            }
    r = requests.post(url,files = files,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def face_search(image_file1,faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    files = {"image_file": open(image_file1, "rb")}
    params = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token
            }
    r = requests.post(url,files = files,params = params)
    req_con = r.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    return req_dict

def face_SetUserID(face_token,user_id):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/setuserid'
    params = {
            'api_key':key,
            'api_secret':secret,
            'face_token':face_token,
            'user_id':user_id
            }
    r = requests.post(url,params = params)
    req_dict = r.json()
    print(req_dict)
    return req_dict

def pay_check(money):
    print '请正对人脸识别系统以完成支付'
    cap = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
    i = 0 # 用于隔20帧取一次图像
    face_right =0
    while (1):
        ret, img = cap.read()  # 摄像头获取该帧图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图像转灰度
        faces = faceCascade.detectMultiScale(gray, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, (5, 5))  # 送入Haar特征分类器
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
        if len(faces) == 0 :#视频中无脸出现
            cv2.imshow('ImageCaptured', img)
        else:
            if i >= 20 and face_right == 0:
                i = 0
                cv2.imwrite('image/faceID.jpg', img)  # 写入该帧图像文件
                face_information = face_search('image/faceID.jpg', 'e55232f11a305f9165caf50ef16ae053')  # 该帧与faceset中人脸进行匹配
                if face_information['faces']:  # [faces]数组不能为空，能在图像中找到脸
                    confidence = face_information['results'][0]['confidence']
                    thresholds = face_information['thresholds']['1e-5']
                    os.remove('image/faceID.jpg')  # 删除该帧图像文件，为下一次处理准备
                    if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
                        user_id = face_information['results'][0]['user_id']  # 获得唯一人脸id

                        recognize_inf = 1
                        face_right = 1
                    else:
                        face_right = 0
                else:
                    face_right = 0  # 未能在图像中找到脸
            else:
                i = i + 1

            for x, y, w, h in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸矩形框

            if face_right == 1:
                cv2.putText(img, user_id, (x, y - 5), font, 1, (0, 0, 255), 1)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
                cv2.putText(img, 'Welcome:', (x - 20, y - 50), font, 2, (0, 0, 0), 2)
                cv2.imshow('ImageCaptured', img)
                if recognize_inf:
                    b = (time.localtime()[5])
                    a = (time.localtime()[5])
                    recognize_inf = 0
                if (abs(a - b) <= 2):  # 现在该提示信息2s
                    a = (time.localtime()[5])
                else:
                    face_right = 0
                    current_money = mysql.check_data1(user_id)
                    mysql.change_data(0, user_id)
                    mysql.change_data1(current_money[0][0] - money, user_id)

                    print '支付成功 欢迎下次光临'
                    break
            else:
                cv2.putText(img, "stranger", (x, y - 5), font, 1, (0, 255, 0), 1)
                cv2.imshow('ImageCaptured', img)
    cv2.destroyAllWindows()
    return user_id,current_money[0][0] - money

if __name__ == "__main__":
    user_id ,a =  pay_check(10)
    print user_id

'''
    face_search(filepath3,'1e78cba6ac972357b7e25f74dc3d18b9')
    face_SetUserID('63f0a9f9ebe8485ac81e7a2a06b40324','Mr.mayun')
    
    detect_face(filepath1)
    addface('1e78cba6ac972357b7e25f74dc3d18b9','dba19cc867f9535b26ddd58055fed338')



            w = face_information['faces'][0]['face_rectangle']['width']
            h = face_information['faces'][0]['face_rectangle']['top']
            x = face_information['faces'][0]['face_rectangle']['left']
            y = face_information['faces'][0]['face_rectangle']['height']

 
face_compare(filepath2,'63f0a9f9ebe8485ac81e7a2a06b40324')
faceset_update('1e78cba6ac972357b7e25f74dc3d18b9','马云','1000')
delete_faceset('481646f4c292389d98e4ecbd2d0f4d35',0)
faceset_getdetail('1e78cba6ac972357b7e25f74dc3d18b9')
image1 = detect_face(filepath1)
faceId2 = image2['faces'][0]['face_token']
addface('1e78cba6ac972357b7e25f74dc3d18b9',faceId1)
set_face()

'''


