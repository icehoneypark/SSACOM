import csv
import tensorflow as tf
import time

start = time.time()
# import numpy as np
## 0명 재실 데이터 불러오기 
f1 = open("no_data.csv", "r")
no_reader = csv.reader(f1)
no_raws = list(no_reader)


## 1명 재실 데이터 불러오기
f2 = open("on_data.csv", "r")
on_reader = csv.reader(f2)

on_raws = list(on_reader)

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

## 학습 모델 설정 (X(독립변수)의 크기 = 1, Y(종속변수)가 영향받는 갯수 = 1)
X = tf.keras.layers.Input(shape=(12, 40), dtype=tf.int32)
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss="mse")

## 학습 시작
print("start")
model.fit(full_datas, y_datas, epochs=20, verbose=0)

# 학습된 모델을 가져오는 방식이 2가지입니다
# 1. 모델전체를 저장하는방법
# 2. 가중치만 저장해서 새로운 모델에 적용하는 방법
model.get_weights()
# predict = model.predict(full_datas)

# 모델 저장
model.save('uwb_model.h5')

print("time = {}".format(time.time() - start))

print('finished')