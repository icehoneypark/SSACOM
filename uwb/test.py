import csv
import tensorflow as tf
import time
import numpy as np

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
    tmp.append(list(map(float, no_raw)))
    if len(tmp) == 12:
        full_datas.append(tmp)
        tmp = list()

## 1명 재실 데이터 12프레임으로 나누기 + 0명 재실 데이터에 붙이기
for on_raw in on_raws:
    tmp.append(list(map(float, on_raw)))
    if len(tmp) == 12:
        full_datas.append(tmp)
        tmp = list()

## 0명 재실 데이터 길이만큼 0 붙이기 + 1명 재실 데이터 길이만큼 1 붙이기
y_datas = [0] * (int(len(full_datas) / 2))
y2_datas = [1] * (int(len(full_datas) / 2))
y_datas.extend(y2_datas)

## 학습 시작
print("start")

# 학습 모델입니다 딥러닝(인공신경망)방식으로 여러줄에 걸쳐 진행합니다 많을수록 정확하겠지만 오래걸리겠죠
model = tf.keras.Sequential()
#flatten으로 데이터를 1줄로 펴서 학습합니다 원래는 정사각형
model.add(tf.keras.layers.Flatten(input_shape=(12,40)))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print(model.summary())

x_train = full_datas

x_test = full_datas

y_train = y_datas

y_test = y_datas

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10000)

test_loss, test_acc = model.evaluate(x_test, y_test)

print('test_loss =', test_loss)
print('test_acc =', test_acc)

predictions = model.predict(x_test)

print('y_test =', y_test[:10],", ", y_test[5000:5010])
print('predictions =', np.argmax(predictions[:10], axis=1))
print('predictions =', np.argmax(predictions[5000:5010], axis=1))

# 모델 저장
model.save('uwb_model.h5')
print("time = {}".format(time.time() - start))
print('finished')