import time

test_data1 = [1, 6, 9, 4, 7, 3, 2, 5, 8]
test_data2 = [1, 6, 9, 4, 7, 3, 2, 5, 8]


def gettime(func):
    def mysort(need_sort):
        begin = time.time()
        result = func(need_sort)
        end = time.time()
        print('排序时间：%d' % (end - begin))

    return mysort


@gettime
def selectsort(test_data):
    for i in range(0, len(test_data) - 1):
        for j in range(i + 1, len(test_data)):
            if test_data[i] > test_data[j]:
                sum = test_data[i]
                test_data[i] = test_data[j]
                test_data[j] = sum


@gettime
def bopsort(test_data):
    for i in range(len(test_data) - 1):
        for j in range(len(test_data) - 1 - i):
            if test_data[j] > test_data[j + 1]:
                test_data[j], test_data[j + 1] = test_data[j + 1], test_data[j]



selectsort(test_data1)
bopsort(test_data2)
