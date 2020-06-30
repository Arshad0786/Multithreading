# -*- coding: utf-8 -*-
import threading

# initialize A and B matrixes


def initializeA():
    #建立作業指定的 A 矩陣
    a = []
    Arow = 35
    Acolumn = 60
    for row in range(Arow):
        a.append([])
        for column in range(Acolumn):
            a[row].append(None)
    for row in range(Arow):
        for column in range(Acolumn):
            a[row][column] = 3.5*row - 6.6*column
    return a


def initializeB():
    #建立作業指定的 B 矩陣
    b = []
    Brow = 60
    Bcolumn = 35
    for row in range(Brow):
        b.append([])
        for column in range(Bcolumn):
            b[row].append(None)
    for row in range(Brow):
        for column in range(Bcolumn):
            b[row][column] = 6.6 + 8.8*row - 3.5*column
    return b


def regularCross(a, b):
    # 正常寫法的運算 for-looping
    Arow = len(a)
    Acolumn = len(a[0])
    Brow = len(b)
    Bcolumn = len(b[0])
    # initialize result matrix
    result = []
    for row in range(Arow):
        result.append([])
        for column in range(Bcolumn):
            result[row].append(None)

    for row in range(Arow):
        for column in range(Bcolumn):
            cross = 0
            for i in range(Acolumn):
                cross = cross + a[row][i] * b[i][column]
            result[row][column] = cross
    return result


def SectionCross(a, b, row, result):
    # 運算單一個 row 的函式， multithreading 寫法會運用此函式，把每個 row 的運算設立成不同的 thread 平行運算
    Arow = len(a)
    Acolumn = len(a[0])
    Brow = len(b)
    Bcolumn = len(b[0])
    rowresult = []
    for column in range(Bcolumn):
        cross = 0
        for i in range(Acolumn):
            cross = cross + a[row][i] * b[i][column]
        rowresult.append(cross)
    result[row] = rowresult

def multithreadCross(a, b):
    # 多執行緒寫法的 multithreading
    Arow = len(a)
    Acolumn = len(a[0])
    Brow = len(b)
    Bcolumn = len(b[0])
    threadQueue = []
    # initialize result matrix
    result = list()
    for row in range(Arow):
        result.append(None)
        # 把每個 row 的運算設立為不同的 thread ，放入 threadQueue 中
        threadQueue.append(threading.Thread(target=SectionCross, args=(a, b, row, result)))
    for row in range(Arow):
        # 開始 threadQueue 中每一個 thread 的工作
        threadQueue[row].start()
    for row in range(Arow):
        # 待 threadQueue 中每個 thread 都完成工作
        threadQueue[row].join()
    #輸出答案
    return result
