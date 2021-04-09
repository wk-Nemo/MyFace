import math
import json


class DB:
    def __init__(self, p, c):
        self.p = p
        self.c = c


class NDB:
    def __init__(self, NDB):
        self.NDB = NDB
        self.m = 1280
        self.r = 10
        self.cn = self.m * self.r
        self.p = [0, 0.95, 0.03, 0.02]
        self.q = [0.55, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
        self.posbility = self.getPosbility()
        self.cc = self.getCC()
        self.Pos = self.num_01()
        self.Gen = self.getAttr()

    def getPosbility(self):
        posbility = []
        for i in range(10):
            posbility.append([])
            posbility[i].append(self.diff(i))
            posbility[i].append(1 - posbility[i][0])
        return posbility

    def diff(self, i):
        Ndiff = 0
        Nsame = 0
        for j in range(1, 4):
            Ndiff += j * self.p[j] * self.q[i]
        for j in range(1, 4):
            Nsame += ((3 - j) * self.p[j]) / 10
        Pdiff = Ndiff / (Ndiff + Nsame)
        return Pdiff

    def myTo2(self, num):
        a = []
        b = bin(num).replace('0b', '')
        for i in range(10 - len(b)):
            a.append('0')
        str = ''
        front = str.join(a)
        result = front + b
        return result

    def getCC(self):
        cc = []
        for i in range(1024):
            cc.append(self.myTo2(i))
        return cc

    def num_01(self):
        Pos = []
        for i in range(self.m):
            Pos.append([])
            Pos[i].append(0)
            Pos[i].append(0)

        for i in range(self.cn):
            for j in range(3):
                if (self.NDB[i].c[j] == '0'):
                    Pos[self.NDB[i].p[j]][0] += 1
                else:
                    Pos[self.NDB[i].p[j]][1] += 1
        return Pos

    def getAttr(self):
        count = 0
        Gen = []
        for i in range(self.m):
            if (i % 10 == 0):
                Gen.append(self.E(i))
                count += 1
        return Gen

    # 从0，1，2 ....., 1023
    def E(self, index):
        tmp = 0
        for i in range(1024):
            tmp += self.calculate(index, i)
        tmp *= math.pow(10, -3)
        return tmp

    def calculate(self, index, real):
        sum = 1
        for i in range(10):
            tmp = self.Pr(index + i, self.cc[real][i])
            sum *= tmp
        sum *= real
        return sum

    def Pr(self, index, num):
        tmp = index % 10
        pdiff = self.posbility[tmp][0]
        psame = self.posbility[tmp][1]
        pr0 = (math.pow(pdiff, self.Pos[index][1]) * math.pow(psame, self.Pos[index][0])) / (
                    math.pow(pdiff, self.Pos[index][1]) * math.pow(psame, self.Pos[index][0]) + math.pow(pdiff,self.Pos[index][0]) * math.pow(psame, self.Pos[index][1]))
        if (num == '1'):
            pr1 = 1 - pr0
            return pr1
        else:
            return pr0


def main():
    # load方法：读取文件中的 JSON 数据
    with open('ndb.txt', 'r') as f:
        data = json.load(f)
        # print(data)

    ndb = data['NDB']

    print(type(ndb))
    # print(NDB[0]['p'][2])

    NDB_list = []
    for data in ndb:
        db = DB(data['p'], data['c'])
        NDB_list.append(db)
    # print(NDB_list[0].p[2])

    a = NDB(NDB_list)
    print(a.Gen)


main()
