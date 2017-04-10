jieqi0 = ['小寒', '立春', '惊蛰', '清明', '立夏', '芒种', '小暑', '立秋', '白露', '寒露', '立冬', '大雪']

f = open("d.txt", "r+")             # 返回一个文件对象
fo = open("foo1.py", "w")

line = f.readline()#.replace('\n', '')   # 调用文件的 readline()方法
n = 1
K = 1
while line:

    #print line,                 # 后面跟 ',' 将忽略换行符
    #print(line, end = '')       # 在 Python 3中使用
    if n % 2:
        line = "'" + line[:-1] + '/' + jieqi0[K%12] + "',\n"
        fo.write(line)
        K += 1
    line = f.readline()#.replace('\n', '')
    n += 1

