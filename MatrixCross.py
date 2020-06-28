import threading

# initialize A and B matrixes


def initializeA():
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
    Arow = len(a)
    Acolumn = len(a[0])
    Brow = len(b)
    Bcolumn = len(b[0])
    threadQueue = []
    # initialize result matrix
    result = list()
    for row in range(Arow):
        result.append(None)
        threadQueue.append(threading.Thread(target=SectionCross, args=(a, b, row, result)))
    for row in range(Arow):
        threadQueue[row].start()
    for row in range(Arow):
        threadQueue[row].join()
    
    return result
