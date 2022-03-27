#coding=GBK
import sys
import numpy as np
import pandas as pd
from xpinyin import Pinyin

class Corebuild():
    def Put_Province(self):
        filename = input().split()
        province = ''
        if(1 == len(sys.argv)):
            file1 = pd.read_csv(filename[0], encoding='GBK', sep='\s+').values
            file2 = open(filename[1], 'w', encoding='GBK')
        if (2 == len(sys.argv)):
            stgv2_1 = "txt"
            stgv2_2 = sys.argv[2].split('.')
            if (stgv2_2 == stgv2_1):
                 filename = input().split()
                 file1 = pd.read_csv(filename[0], encoding='GBK', sep='\s+').values
                 file2 = open(filename[1], 'w', encoding='GBK')
            else:
                pass

        data1 = file1[:, 0]
        data2 = file1[:, 2]
        if len(filename) > 2:
            province = filename[2]
            exchangeaaa(file1, data1, file2, province)
        if province != '':
            f = 0
            for i in range(len(file1)):
                if file1[i][0] == province:
                    p = i
                    break
            for i in range(len(file1)):
                if file1[i][0] == province:
                    f += 1
            data1 = file1[p:f, 0]
            data2 = file1[p:f, 2]

        if province == '':
            prolen = plen(data1)
            proex = exchange(data1, prolen, file1)
            proindex = sorted(range(len(proex[prolen])), key=lambda k: proex[prolen][k], reverse=True)
            cityindex = list([] for _ in range(prolen))
            data3 = exdata(data2, proex, prolen)
            data4 = list([] for _ in range(prolen))
            data4 = dexcity(file1, proex, prolen, data4)
            cityindex = excity(cityindex, prolen, data3)
            cityindex = expinyin(cityindex, data3, data4)
            poutput(proex, proindex, cityindex, prolen, data3, data4, data1, file2)

def plen(data1):
    A = np.array('a')
    A = data1[0]
    prolen = 1
    for i in range(len(data1)):
        if data1[i] != A:
            prolen += 1
            A = data1[i]
    return prolen


def exchange(data1, prolen, file1):
    proint = 0
    A = data1[0]
    J = list()
    K = list([] for _ in range(prolen + 1))
    L = list()
    indexk = 0
    for i in range(len(data1)):
        if data1[i] is A:
            J.append(i)
            proint += file1[i][2]
        else:
            A = data1[i]
            proint += file1[i][2]
            L.append(proint)
            K[indexk] = J.copy()
            indexk += 1
            J.clear()
            J.append(i)
            proint = 0
    K[indexk] = J.copy()
    L.append(proint)
    K[prolen] = L.copy()
    return K

def exchangeaaa(file1, data1, file2, province):
    A = np.array('a')
    A = data1[0]
    if province != '':
        A = province
    file2.write(A)
    file2.write('\r\n')
    if province == '':
        for i in range(len(data1)):
            if data1[i] == A:
                B = (file1[i][1], file1[i][2])
                C = " ".join('%s' %id for id in B)
                file2.write('\r\n')
                file2.write(C)
            else:
                file2.write('\r\n')
                file2.write('\r\n')
                file2.write('\r\n')
                file2.write(A)
                A = data1[i]
    else:
        for i in range(len(data1)):
            if data1[i] == A:
                B = (file1[i][1], file1[i][2])
                C = " ".join('%s' %id for id in B)
                file2.write('\r\n')
                file2.write(C)


def excity(cityindex, prolen, data3):
    for i in range(prolen):
        cityindex[i] = sorted(range(len(data3[i])), key=lambda k: data3[i][k], reverse=True)
    return cityindex

def execity(data1, data2, lena, cityindex):
    for i in range(lena):
        cityindex[i] = sorted(range(len(data2)), key=lambda k: data2[k], reverse=True)
    return cityindex


def poutput(proex, proindex, cityindex, prolen, data3, data4, data1, file2):
    for j in range(len(proindex)):
        file2.write('\r\r')
        file2.write(data1[proex[proindex[j]][0]])
        for k in range(len(cityindex[proindex[j]])):
            a = proindex[j]
            b = cityindex[a][k]
            file2.write('\r')
            file2.write(data4[a][b])
            file2.write(str(data3[a][b]))
        file2.write('\r')
        file2.write('总数')
        file2.write(str(proex[prolen][proindex[j]]))

def exdata(data2, proex, prolen):
    data3 = list([] for _ in range(prolen))
    for i in range(prolen):
        for j in range(len(proex[i])):
            data3[i].append(data2[proex[i][j]])
    return data3

def dexcity(file1, proex, prolen, data4):
    for i in range(prolen):
        for j in range(len(proex[i])):
            data4[i].append(file1[proex[i][j]][1])
    return data4

def expinyin(cityindex, data3, data4):
    for i in range(len(cityindex)):
        for j in range(len(cityindex[i])):
            if j+1 != len(cityindex[i]):
                if data3[i][cityindex[i][j]] == data3[i][cityindex[i][j+1]]:
                    if topinyin(cityindex, i, j, data4):
                        c = cityindex[i][j]
                        cityindex[i][j] = cityindex[i][j+1]
                        cityindex[i][j+1] = c
    return cityindex


def topinyin(cityindex, i, j, data4):
    p = Pinyin()
    a = p.get_pinyin(data4[i][cityindex[i][j]])
    b = p.get_pinyin(data4[i][cityindex[i][j+1]])
    if a > b:
        return True
    else:
        return False

if __name__ == '__main__':

    core = Corebuild()
    core.Put_Province()

'''
    file1 = pd.read_csv('yq_in.txt', encoding='GBK', sep='\s+').values
    data1 = file1[:, 0]
    data2 = file1[:, 2]
    file2 = open('yq_out.txt', 'w', encoding='GBK')
    province = ''
    prolen = plen(data1)
    proex = exchange(data1, prolen)
    proindex = sorted(range(len(proex[prolen])), key=lambda k: proex[prolen][k], reverse=True)
    cityindex = list([] for _ in range(prolen))
    data3 = exdata(data2, proex, prolen)
    data4 = list([] for _ in range(prolen))
    data4 = dexcity(file1, proex, prolen, data4)
    cityindex = excity(cityindex, prolen, data3)
    cityindex = expinyin(cityindex, data3, data4)
    poutput(proex, proindex, cityindex, prolen, data3, data4, data1)
'''