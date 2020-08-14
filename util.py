import datetime
import numpy as np


def F_to_C(fah):
    cel = (fah - 32.0) * (5.0/9.0)
    return cel


def add_array(arr1, arr2):
    arr3 = []
    for num in range(len(arr1)):
        arr3.append(arr1[num]+arr2[num])
    return arr3


def div_array(arr1, arr2):
    arr3 = []
    for num in range(len(arr1)):
        arr3.append(arr1[num]/arr2[num])
    return arr3


def datetime_format(array):
    return [item.strftime('%b-%d')
            for item in array]


def F_to_C(fah):
    cel = (fah - 32.0) * (5.0/9.0)
    return cel


def unique_elem_from_2dim_arr(arr):
    manufacturers, no_of_planes = np.unique(arr, return_counts=True)
    return manufacturers, no_of_planes


def avg_time(data):
    mins = [(item // 100)*60 + (item % 100) for item in data]
    am = np.mean(mins)
    print(am)
    h = int(am//60)
    m = int((am-h*60)//1)
    s = int((int((am-h*60-m)*100)*60)/100)
    return datetime.time(h,m,s)