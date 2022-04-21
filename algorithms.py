import time
from colors import *


def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, [YELLOW if x == j or x == j + 1 else BLUE for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])





def insertion_sort(data, drawData, timeTick):
    for i in range(len(data)):
        temp = data[i]
        k = i
        while k > 0 and temp < data[k - 1]:
            data[k] = data[k - 1]
            k -= 1
        data[k] = temp
        drawData(data, [YELLOW if x == k or x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)

        merge_sort(data, start, mid, drawData, timeTick)

        merge_sort(data, mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])


def partition(data, start, end, drawData, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start + 1, end + 1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[start], data[i - 1] = data[i - 1], data[start]
    return i - 1


def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick)
        quick_sort(data, start, pivot_position - 1, drawData, timeTick)
        quick_sort(data, pivot_position + 1, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
        else DARK_BLUE if x > pivot_position and x <= end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])


def selection_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        minimum = i
        for k in range(i + 1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, [YELLOW if x == minimum or x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])