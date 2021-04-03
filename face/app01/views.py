import string
from random import random, randint

from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse

from app01 import models


# 生成指定长度的随机数
def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


# Create your views here.

def index(request):
    return render(request, 'index.html')


def getface_native(request):
    # dict = request.POST.nativeData
    dict = request.POST
    username = dict['username']
    NDB = dict['NDB']
    userid = random_with_N_digits(6)
    # 将数据写入到文件中
    # filepath = 'static/native/xh.txt'
    filepath = 'static/native/' + username + str(userid) + '.txt'
    print(filepath)
    with open(filepath, 'w') as file_object:
        file_object.write(NDB)
    p = models.user.objects.get_or_create(uid=userid, name=username, data=filepath)
    return JsonResponse({'userID': userid})


def getface_part(request):
    # dict = request.POST.partData
    dict = request.POST
    username = dict['username']
    NDB = dict['NDB']
    userid = random_with_N_digits(6)
    # 将数据写入到文件中
    filepath = 'static/part' + username + str(userid) + '.txt'
    with open(filepath, 'w') as file_object:
        file_object.write(NDB)
    p = models.user.objects.get_or_create(uid=userid, name=username, data=filepath)
    return JsonResponse({'userID': userid})


def faceRecognize_native(request):
    dict = request.POST.nativeRecognize
    userid = dict.userID
    NDB = dict.NDB
    # 获取加密数据的存储路径
    filepath = models.user.objects.get(uid=userid).data
    f = open('filepath', 'r')
    data = f.read()
    # 接下来进行比对两组数据

    return JsonResponse({'result:true'})


def faceRecognize_part(request):
    dict = request.POST.nativeRecognize
    userid = dict.userID
    NDB = dict.NDB
    # 获取加密数据的存储路径
    filepath = models.user.objects.get(uid=userid).data
    f = open('filepath', 'r')
    data = f.read()
    # 接下来进行比对两组数据

    return JsonResponse({'result:true'})
