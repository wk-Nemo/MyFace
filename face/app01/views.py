import string
import json
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


# 用户注册接口 （负数据库）
# 提交类型：post
# 提交数据：username(用户名)，NDB(加密之后的负数据)
# 返回：json数据类型：userID
def getface_native(request):
    # dict = request.POST.nativeData
    if request.method == 'POST':
        username = json.loads(request.body).get('username')
        NDB = json.loads(request.body).get('NDB')
    # print(dict)
    # username = dict['username']
    userid = random_with_N_digits(6)
    # 将数据写入到文件中
    # filepath = 'static/native/xh.txt'
    filepath = 'static/native/' + username + str(userid) + '.txt'
    print(filepath)
    with open(filepath, 'w') as file_object:
        file_object.write(NDB)
    p = models.user_native.objects.get_or_create(uid=userid, name=username, data=filepath)
    return JsonResponse({'userID': userid})


# 负数据库的数据验证
# 提交类型：post
# 提交数据：userID(用户id)，NDB(加密之后的数据)
# 返回：json数据类型：result（验证结果）
def faceRecognize_native(request):
    # dict = request.POST.nativeRecognize
    dict = request.POST
    userid = dict['userID']
    NDB = dict['NDB']
    # 获取加密数据的存储路径
    filepath = models.user_native.objects.get(uid=userid).data
    f = open('filepath', 'r')
    data = f.read()
    # 接下来进行比对两组数据

    return JsonResponse({'result:true'})


# 用户注册接口 （局部排序）
# 提交类型：post
# 提交数据：username(用户名)，part(加密之后的数据)
# 返回：json数据类型：userID
def getface_part(request):
    # dict = request.POST.partData
    dict = request.POST
    username = dict['username']
    part = dict['part']
    p_string = dict['p']
    userid = random_with_N_digits(6)
    # 将数据写入到文件中
    filepath = 'static/part/' + username + str(userid) + '.txt'
    with open(filepath, 'w') as file_object:
        file_object.write(part)
    p = models.user_part.objects.get_or_create(uid=userid, name=username, data=filepath, p=p_string)
    return JsonResponse({'userID': userid})


# 获取 p 字串接口（局部排序）
# 提交类型:get
# 提交数据：userid（用户id）
# 返回: json数据类型: p
def part_p(request):
    dict = request.GET
    userid = dict['userID']
    # 从数据库中获取userid对应的用户数据
    user_info = models.user_part.objects.get(uid=userid)
    p_string = user_info.p
    return JsonResponse({'p': p_string})


# 局部排序的数据验证
# 提交类型：post
# 提交数据：userID（用户ID），part(加密之后的数据)
# 返回：json数据类型：result（验证结果）
def faceRecognize_part(request):
    dict = request.POST.nativeRecognize
    userid = dict['userID']
    part = dict['part']
    # 获取加密数据的存储路径
    filepath = models.user_part.objects.get(uid=userid).data
    f = open('filepath', 'r')
    data = f.read()
    # 接下来进行比对两组数据

    return JsonResponse({'result:true'})
