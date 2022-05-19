# tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras
import time

# 헬퍼(helper) 라이브러리를 임포트합니다
import numpy as np

import csv

def min_pooling(arr):
    x, y = arr.shape
    new_x, new_y = x//2 , y//2
    # new_x, new_y = x//10 , y//10

    arr = np.min(arr.reshape(new_x, 2, y, 1), axis = (1,3))
    # arr = np.min(arr.reshape(new_x, 10, y, 1), axis = (1,3))
    return arr

print(tf.__version__)

start = time.time()
## 0명 재실 데이터 불러오기 
f1 = open("no_test_data.csv", "r")
no_reader = csv.reader(f1)
# no_raws = list(no_reader)
no_raws = min_pooling(np.array(list(no_reader)).astype(np.int64))


## 1명 재실 데이터 불러오기
f2 = open("on_test_data.csv", "r")
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

## 0명 재실 데이터 길이만큼 0 붙이기 + 1명 재실 데이터 길이만큼 1 붙이기
y_datas = [0] * (int(len(full_datas) / 2))
y2_datas = [1] * (int(len(full_datas) / 2))
y_datas.extend(y2_datas)

## 여기서부터 학습코드 작성하면 됨 (x_train = full_datas, y_train = y_datas)
## full_datas의 구조는 10000 * 12 * 40, y_datas는 10000``
train_images = np.array(full_datas).astype(np.int64)
train_labels = np.array(y_datas).astype(np.int64)


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(12, 40)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


model.fit(train_images, train_labels, epochs=100)

test_loss, test_acc = model.evaluate(train_images, train_labels, verbose=2)

print('\n테스트 정확도 acc :', test_acc)
print('\n테스트 정확도 loss :', test_loss)

model.save('test.h5')

print(time.time() - start)