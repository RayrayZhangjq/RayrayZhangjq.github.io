import os
import re
import sys

info = []
# filename = "./yq_in_03.txt"
filename = sys.argv[1]
f = open(filename, 'r')
line = f.readline()
while line:
    province = line[0:3]
    # 使用正则表达式取出每一行里的城市名
    matchObj1 = re.search(r'(?<=\s)[\u4e00-\u9fa5]*(?=\s)', line)
    # 取出一行里面的人数
    matchObj2 = re.search(r'\d+\.?\d*', line, re.U)
    city = matchObj1.group(0)
    num = matchObj2.group(0)
    # 存储信息
    info.append({"province": province, "city": city, "num": num})
    line = f.readline()
f.close()

# path = './yq_out_03.txt'

# 给输出文件命名
path = filename.replace("in", "out")
if os.path.exists(path):
    os.remove(path)

tmp = ""
for i in info:
    f = open(path, 'a')
    if tmp != i['province']:
        f.write('\n' + str(i['province']) + ':' + '\n')
        tmp = i['province']
    f.write(str(i['city']) + '\t' + str(i['num']) + '\n')
    f.close()
