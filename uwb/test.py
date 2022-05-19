import csv
import tensorflow as tf
import time
import numpy as np

from tensorflow import keras

# 헬퍼(helper) 라이브러리를 임포트합니다
def min_pooling(arr):
    x, y = arr.shape
    new_x, new_y = x//2 , y//2

    arr = np.min(arr.reshape(new_x, 2, y, 1), axis = (1,3))
    return arr

# print(min_pooling(arr))


start = time.time()
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

# fashion_mnist = keras.datasets.fashion_mnist



# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = np.array(full_datas)

test_images = np.array(full_datas)

train_labels = np.array(y_datas)

test_labels = np.array(y_datas)


# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
            #    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(train_images.shape)


print(len(train_images))

# print(train_labels)

print(train_labels.shape)

print(len(train_labels))

# train_images = train_images / 255.0

# train_images = train_images / 2538.0

# test_images = test_images / 255.0

# test_images = test_images / 2538.0



model = keras.Sequential([
    keras.layers.Flatten(input_shape=(12, 40)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\n테스트 손실율:', test_loss)

print('\n테스트 정확도:', test_acc)

print(model.predict(test_images[:10]))
print(model.predict(test_images[5880:5890]))