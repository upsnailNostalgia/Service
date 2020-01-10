#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !author:bruce chou

def testList():
    str = 'aaa bbb'
    list = str.split(' ')
    print(type(list))
    for ele in list:
        print(ele)
    print(list)


def testRange():
    for index in range(0,2):
        print(index)


def testDic():
    dic = {'a':1,'b':2}
    print('dic'+dic.__str__())


# testList()
#testRange()
testDic()