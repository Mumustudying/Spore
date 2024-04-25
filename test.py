import requests


url = "https://118.31.3.198:8900/admin/common/upload2"
files = {
    'file':('https://118.31.3.198:8998/group1/M00/00/2F/rBEGJmXytWmAcuDMAABgMoKHWxM258.jpg',
            open("C:/Users/17865/Desktop/123.jpg",'rb'), 
            'image/jpg')}

data ={
    # 'file':'F:/Server_model/yolov8_spore/img/out_image/test.jpg',
    'sign':'XuChengYong12345'
}

res = requests.post('https://118.31.3.198:8900/admin/common/upload2',data=data, files=files, verify=False)
print(res.json())

