import math
import random

# 该文件夹主要负责数据的转换
class Num_Change:
    # 一个数据改变对象有三个属性：本身的数值，正负号，转换成二进制后的字符串
    def __init__(self, num):
        self.num = num
        if (num > 0):
            self.flag = 1
        else:
            self.flag = -1
        self.s = self.floatTo2(num)

    # 将数值部分转换成二进制字符串
    def floatTo2(self, num):
        a = []
        # 判断正负号
        if(num > 0):
            flag = 1
        else:
            num *= -1
            flag = -1

        b = round(num*math.pow(10, 3))
        c = bin(b).replace('0b','')
        for i in range(10-len(c)):
            a.append('0')
        str = ''
        front = str.join(a)
        result = front + c
        return result

    # 二进制字符串转换成原始数据
    def toFloat(self):
        num = 0
        count = len(self.s) - 1
        for i in range(len(self.s)):
            if(self.s[i] == '1'):
                num += math.pow(2, count)
            count -= 1
        num *= self.flag
        num *= math.pow(10, -3)
        return num

# 传入原始的128维数据，可以得到128维数据转换后的二进制数
class Get_s:
    def __init__(self, nums):
        # nums是原始的数据，即128维数组
        self.nums = nums
        # s是128维数据转换后的二进制字符串
        self.s = self.to128Str()
        # flags 存储的是128维数据的正负号
        self.flags = self.getFlags()

    # 获得连接的字符串s
    def to128Str(self):
        s = ''
        for i in range(len(self.nums)):
            num = Num_Change(self.nums[i])
            s += num.s
        return s

    # 获得128维数据的符号
    def getFlags(self):
        flags = []
        for i in range(len(self.nums)):
            num = Num_Change(self.nums[i])
            flags.append(num.flag)
        return flags

    # 二进制字符串转换成原始数据
    def toFloat(self, s, k):
        num = 0
        count = len(s) - 1
        for i in range(len(s)):
            if (s[i] == '1'):
                num += math.pow(2, count)
            count -= 1
        num *= self.flags[k]
        num *= math.pow(10, -3)
        return num

    # 128维向量的二进制字符串s转换成128个数据
    def to128Float(self):
        mynums = []
        for i in range(len(self.s)//10):
            res = self.s[i*10 :i*10+10]
            print(res)
            mynums.append(self.toFloat(res, i))
        return mynums

class Xor():
    def __init__(self):
        self.specific = self.getSpecific()

    # 随机生成一个异或串
    def getSpecific(self):
        specific_res = []
        for i in range(1280):
            x = random.random()
            if(x < 0.5):
                specific_res.append('0')
            else:
                specific_res.append('1')
        str = ''
        result = str.join(specific_res)
        return result

    # 异或函数
    def xor(self, s):
        res = []
        for i in range(1280):
            if (s[i] == self.specific[i]):
                res.append('0')
            else:
                res.append('1')
        str = ''
        result = str.join(res)
        return result


def main():
    nums = [0.123, 0.762, -0.003, 0.56465461, -0.1616512351]
    b = Get_s(nums)
    print(b.s)
    print(b.to128Float())

