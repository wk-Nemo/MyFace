import string
import json
from random import random, randint
import numpy as np

from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse

from app01 import models
from app01 import getNDB


class DB:
    def __init__(self, p, c):
        self.p = p
        self.c = c


# 生成指定长度的随机数
def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


# 计算欧氏距离
def distance(list1, list2):
    np_1 = np.array(list1)
    np_2 = np.array(list2)

    ans = np.sqrt(np.sum((np_1 - np_2) ** 2))
    return ans


# Create your views here.

def index(request):
    return render(request, 'index.html')


# 用户注册接口 （负数据库）
# 提交类型：post
# 提交数据：username(用户名)，NDB(加密之后的负数据)
# 返回：json数据类型：userID
def getface_native(request):
    # dict为python数据结构 loads将json字符串转换为python数据结构
    dict = json.loads(request.body)
    print(request.body)
    # 获取字典元素
    username = dict.get('username')

    NDB = dict.get('NDB')
    # print(NDB)
    flag = dict.get('flag')
    specific = dict.get('specific')
    print(flag)
    print(specific)
    # ndb = getNDB.NDB(NDB, flag, specific)
    # print(ndb.primaryGen)

    userid = random_with_N_digits(6)
    # 将数据写入到文件中
    # filepath = 'static/native/xh.txt'
    filepath = 'static/native/' + username + str(userid) + '.json'
    print(filepath)
    with open(filepath, 'w') as file_object:
        jsObj = json.dumps(dict)
        file_object.write(jsObj)
    file_object.close()
    p = models.user_native.objects.get_or_create(uid=userid, name=username, data=filepath)
    return JsonResponse({'userID': userid})


# 负数据库的数据验证
# 提交类型：post
# 提交数据：userID(用户id)，NDB(加密之后的数据)
# 返回：json数据类型：result（验证结果）
def faceRecognize_native(request):
    dict = json.loads(request.body)
    # 认证数据
    userid = dict.get('userID')
    print(userid)
    NDB_new = dict.get('NDB')
    specific_new = dict.get('specific')
    flag_new = dict.get('flag')

    NDB_new_list = []
    for data in NDB_new:
        db = DB(data['p'], data['c'])
        NDB_new_list.append(db)

    # 生成原始数据
    b = getNDB.NDB(NDB_new_list, flag_new, specific_new)
    # print(b.primaryGen)

    # 获取加密数据的存储路径
    filepath = models.user_native.objects.get(uid=userid).data
    with open(filepath, 'r') as f:
        data = json.load(f)
        # 接下来进行比对两组数据
    # 原始数据
    ndb = data['NDB']
    # print(ndb)
    specific = data['specific']
    flag = data['flag']
    NDB_list = []
    for data in ndb:
        db = DB(data['p'], data['c'])
        NDB_list.append(db)

    a = getNDB.NDB(NDB_list, flag, specific)
    print(a.primaryGen)

    return JsonResponse({'result': 'true'})


# 用户注册接口 （局部排序）
# 提交类型：post
# 提交数据：username(用户名)，part(加密之后的数据)
# 返回：json数据类型：userID
def getface_part(request):
    # dict = request.POST.partData
    # dict = request.POST
    dict = json.loads(request.body)
    username = dict.get('username')
    part = dict.get('part')
    p_string = dict.get('p')

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
    dict = json.loads(request.body)
    userid = dict.get('userID')
    # 从数据库中获取userid对应的用户数据
    user_info = models.user_part.objects.get(uid=userid)
    p_string = user_info.p
    return JsonResponse({'p': p_string})


# 局部排序的数据验证
# 提交类型：post
# 提交数据：userID（用户ID），part(加密之后的数据)
# 返回：json数据类型：result（验证结果）
def faceRecognize_part(request):
    dict = json.loads(request.body)
    userid = dict.get('userID')
    part = dict.get('part')
    # 获取加密数据的存储路径
    filepath = models.user_part.objects.get(uid=userid).data
    f = open('filepath', 'r')
    data = f.read()
    # 接下来进行比对两组数据

    return JsonResponse({'result': true})
