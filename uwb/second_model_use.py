import pandas as pd
import tensorflow as tf
from tensorflow.python.keras.models import load_model
import csv
import time
import numpy as np

def min_pooling(arr):
    x, y = arr.shape
    new_x, new_y = x//2 , y//2
    # new_x, new_y = x//10 , y//10

    arr = np.min(arr.reshape(new_x, 2, y, 1), axis = (1,3))
    # arr = np.min(arr.reshape(new_x, 10, y, 1), axis = (1,3))
    return arr

start = time.time()
## 0명 재실 데이터 불러오기 
f1 = open("no2_test_data.csv", "r")
no_reader = csv.reader(f1)
# no_raws = list(no_reader)
no_raws = min_pooling(np.array(list(no_reader)).astype(np.int64))


## 1명 재실 데이터 불러오기
f2 = open("on2_test_data.csv", "r")
on_reader = csv.reader(f2)
# on_raws = list(on_reader)
on_raws = min_pooling(np.array(list(on_reader)).astype(np.int64))

full_datas = list()

tmp = list()
## 0명 재실 데이터 12프레임으로 나누기
for no_raw in no_raws:
    tmp.append(no_raw)
    if len(tmp) == 12:
        full_datas.append(tmp)
        tmp = list()

## 1명 재실 데이터 12프레임으로 나누기 + 0명 재실 데이터에 붙이기
for on_raw in on_raws:
    tmp.append(on_raw)
    if len(tmp) == 12:
        full_datas.append(tmp)
        tmp = list()
        
x_train = np.array(full_datas).astype(np.int64)


#모델을 불러옵니다(import 잊지마세요)
model = load_model('test.h5')

predict = model.predict(np.array(full_datas).astype(np.int64))

print(len(predict))
# print(predict)

for idx in range(len(predict)):
    print(predict[idx])
#     print(predict[idx][0], end = " ")
    if idx == len(predict) // 2:
        print(" ")
        print("========")
# count_0 = 0
# count_1 = 0

# for result in predict:
#     if result < 0.5:
#         count_0 += 1
#     else:
#         count_1 += 1

# print("time = {}".format(time.time() - start))
# print("count_0 = {}".format(count_0))
# print("count_1 = {}".format(count_1))
