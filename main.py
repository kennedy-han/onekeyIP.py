#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os,sys

# 修改下方文件路径！！！ 仅仅修改双引号之间的内容！！！
path1 = r"/home/bllli/PycharmProjects/onekey/demo/cfg1"
path2 = r"/home/bllli/PycharmProjects/onekey/demo/cfg2"
# 修改上方文件路径！！！ 仅仅修改双引号之间的内容！！！

re_ip = r'\d+\.\d+\.\d+\.\d+'
re_h  = '0.0.0.0'
true_ip ='111'


def change():
    global true_ip
    print '获取ip中......'
    true_ip = getip()
    print '外网ip获取成功：' + true_ip
    print '修改中.......'
    listdir(path1, a)
    listdir(path2, a)
    print 'IP文件修改完成'


def bak():
    print '备份中.......'
    listdir(path1, b)
    listdir(path2, b)
    print 'IP文件备份完成'


def chfile(path):
    global true_ip
    if not os.path.isfile(path + '.bak'):
        print '找不到备份文件！请阅读上方教程！'
        quit()
    f = open(path + '.bak', 'r')  # 打开备份的含有0.0.0.0的文件
    content = f.read()
    f.close()

    if re.search(re_h, content):
        print path + "匹配成功"
        content = re.sub(re_h, true_ip, content)
    else:
        print path + "匹配失败"
    f = open(path, 'w')# 写回到文件
    f.write(content)
    f.close()


def getip():
    import urllib2
    response = urllib2.urlopen("http://www.baidu.com/s?ie=utf-8&wd=ip")
    html = response.read()
    ip_bd = re.search('fk="' + r'\d+\.\d+\.\d+\.\d+', html)
    if ip_bd:
        ip_bd = ip_bd.group()
    else:
        print '未成功链接外网，请更新程序！'
        quit()
    return re.search(r'\d+\.\d+\.\d+\.\d+', ip_bd).group()
    # done


def listdir(dir, do):
    filenum = 0
    list = os.listdir(dir)  # 列出目录下的所有文件和目录
    for line in list:
        filepath = os.path.join(dir,line)
        if os.path.isdir(filepath):  # 如果filepath是目录，跳过
            pass
        elif os.path:   # 如果filepath是文件，直接列出文件名
            # print filepath + '的后缀名是 \n' + os.path.splitext(line)[1]
            # print '对比结果' + str('.cfg' == os.path.splitext(line)[1])
            if os.path.splitext(line)[1] == '.cfg': # 限制仅仅处理规定后缀名的文件
                do(filepath)
                print('   ' + line + '已处理' + '\n')
                filenum = filenum + 1
    print('共处理文件数 '+ str(filenum))


def a(filepath):
    chfile(filepath)

def b(filepath):
    f = open(filepath, 'r')
    content = f.read()
    f.close()
    f = open(filepath + '.bak', 'w')
    f.write(content)
    f.close()


def main():
    print '*' * 60
    print """\
*
*         一键修改服务端ip文件
*   by bllli https://github.com/bllli/
* 第一次使用，请先将所有cfg文件内的公网ip修改成 "0.0.0.0"（没有引号）
* 然后使用"./onekey.py bak"命令进行初始化
*\
"""
    print '*' * 60

    if len(sys.argv) > 1 :
        if sys.argv[1] == 'bak':
            bak()
        elif sys.argv[1] == 'res':
            # res()
            print '真的需要还原功能吗？'
    change()


if __name__ == '__main__':
    main()
