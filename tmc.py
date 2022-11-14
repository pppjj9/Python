#coding=utf-8
import os
import re
from random import choice
IMAGE_URLs = "https://eclass.tmcss.edu.hk/file/user_photo/tmc"
keywords = ['21098', '21004']
text = input('请输入目标学生编号(输入纯数字,不用加tmc)：')
textted = ['21013', '21060']
textt = choice(textted)
def check_filter(keywords, text):
 return re.sub("|".join(keywords), textt, text)
IMAGE_URLsmun = check_filter(keywords, text)
os.makedirs('./image/', exist_ok=True)
IMAGE_URLend = ".jpg"
print('目前下载的学生编号:', text)

IMAGE_U = f'{IMAGE_URLs}{IMAGE_URLsmun}{IMAGE_URLend}'
from urllib.request import urlretrieve
urlretrieve(IMAGE_U, './image/IMAGE_U.png')
path = './image/'
os.listdir(path)
fileList = os.listdir(path)
oldname = "./image/IMAGE_U.png"

newname = path + os.sep + 'tmc' + str(text) + '.png'

os.rename(oldname, newname)
