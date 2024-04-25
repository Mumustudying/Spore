
import requests
import re
import cv2
import sys
import os
import predict
import urllib
from gmssl import sm4
from flask import Flask, request, jsonify




# 验证码
Sign = 'XuChengYong12345'

"""
孢子检测算法
import predict
"""



###--------------执行上传------------------###
url = "http://192.168.1.128:8091/upload"

files = {
    'file':('https://118.31.3.198:8998/group1/M00/00/2F/rBEGJmXytWmAcuDMAABgMoKHWxM258.jpg',   #测试图像文件
            open(predict.save_path,'rb'), 
            'image/jpg')}

def sm4_encode(key, data):
    """
    国密sm4加密
    :param key: 密钥
    :param data: 原始数据
    :return: 密文hex
    """
    sm4Alg = sm4.CryptSM4()  # 实例化sm4
    sm4Alg.set_key(key.encode(), sm4.SM4_ENCRYPT)  # 设置密钥
    dateStr = str(data)
    # print("明文:", dateStr)
    enRes = sm4Alg.crypt_ecb(dateStr.encode())  # 开始加密,bytes类型，ecb模式
    enHexStr = enRes.hex()
    # print("密文:", enHexStr)
    return enHexStr # 返回十六进制值
    # return encrypt_value.hex()  

def sm4_decode(key, data):
    """
    国密sm4解密
    :param key: 密钥
    :param data: 密文数据
    :return: 明文hex
    """
    sm4Alg = sm4.CryptSM4()  # 实例化sm4
    sm4Alg.set_key(key.encode(), sm4.SM4_DECRYPT)  # 设置密钥
    deRes = sm4Alg.crypt_ecb(bytes.fromhex(data))  # 开始解密。十六进制类型,ecb模式
    deHexStr = deRes.decode()
    # print("解密后明文:", deRes)
    # print("解密后明文hex:", deHexStr)
    return deHexStr

def test():
    """
    测试
    """
    key = "AN3462g23529K729";  
    strData = Sign

    enHexRes = sm4_encode(key,strData)

    # print("解密测试===",enHexRes)

    code = sm4_decode(key,enHexRes)
    return code


password = test()

data ={                 # 请求参数
    # 'file':'F:/Server_model/Spore/img/out_image/test.jpg',
    'sign':password
}

res = requests.post(url=url,data=data, files=files, verify=False)  # 发送post请求
print(res.json())


# 测试url: https://118.31.3.198:8998/group1/M00/00/2F/rBEGJmXukxeAGhcCAABgMoKHWxM526.jpg
