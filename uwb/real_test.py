import csv
import tensorflow as tf
import time
import numpy as np

def min_pooling(arr):
    x, y = arr.shape
    new_x, new_y = x//2 , y//2
    # new_x, new_y = x//10 , y//10

    arr = np.min(arr.reshape(new_x, 2, y, 1), axis = (1,3))
    # arr = np.min(arr.reshape(new_x, 10, y, 1), axis = (1,3))
    return arr

# print(min_pooling(arr))


start = time.time()
## 0명 재실 데이터 불러오기 
f1 = open("no_test_data.csv", "r")
no_reader = csv.reader(f1)
no_raws = min_pooling(np.array(list(no_reader)).astype(np.int64))


## 1명 재실 데이터 불러오기
f2 = open("on_test_data.csv", "r")
on_reader = csv.reader(f2)

on_raws = min_pooling(np.array(list(on_reader)).astype(np.int64))

full_datas = list()

tmp = list()

two_line = list()

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

print(y_datas)

## 여기서부터 학습코드 작성하면 됨 (x_train = full_datas, y_train = y_datas)
## full_datas의 구조는 10000 * 12 * 40, y_datas는 10000``
x_train = full_datas
y_train = y_datas

x_ex = np.array(x_train)
x_train = x_ex.astype(np.int64)
y_ex = np.array(y_train)
y_train = y_ex.astype(np.int64)
# print(x_train[0][0][0])

model = tf.keras.Sequential()
#flatten으로 데이터를 1줄로 펴서 학습합니다 원래는 정사각형
model.add(tf.keras.layers.Flatten(input_shape=(12,40)))
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print(model.summary())
model.fit(x_train, y_train, validation_data=(x_train, y_train), epochs=200)

test_loss, test_acc = model.evaluate(x_train, y_train)

print('test_loss =', test_loss)
print('test_acc =', test_acc)

model.save('test.h5')

# test_data = list()
# for arr_data in arr:


# predictions = model.predict(x_train)
# print(len(predictions))
# print("====")
# print(predictions[8000])

# for idx in range(100):
#     if predict

predict = model.predict(x_train)

print(len(predict))
# print(predict)

for idx in range(len(predict)):
    print(predict[idx])
    print(y_train[idx])
#     print(predict[idx][0], end = " ")
    if idx == len(predict) // 2:
        print(" ")
        print("========")
# count_0 = 0
# count_1 = 0