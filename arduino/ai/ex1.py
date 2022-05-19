import pandas as pd
import tensorflow as tf
import numpy as np

# mnist: 손으로 쓴 숫자의 이미지를 보고 어떤 숫자인지 맞추는 학습입니다.
# 예시 데이터는 tensorflow 내에 포함되어 있습니다
mnist = tf.keras.datasets.mnist

# x_train : 학습 데이터
# y_train : 데이터의 정답 
# train 데이터로 학습을 시킨 후 test 데이터로 학습이 잘 됐는지 확인
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train[0]) 사용해서 예시데이터 확인해 보세요
# 데이터 형식이 numpy 형식이면 된다고 알고있어요

# 데이터의 값을(0~1)사이의 값으로 변경
x_train = x_train/x_train.max()
x_test = x_test/x_test.max()

# 학습 모델입니다 딥러닝(인공신경망)방식으로 여러줄에 걸쳐 진행합니다 많을수록 정확하겠지만 오래걸리겠죠
model = tf.keras.Sequential()
#flatten으로 데이터를 1줄로 펴서 학습합니다 원래는 정사각형
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
#dense가 각 레이어층이고 activation은 학습모델의 종류입니다
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(32, activation='relu'))
# 마지막은 %로 나타내는거라 sofrmax로 마무리됩니다
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

print(model.summary())

# 여기서 학습이 진행됩니다(= 모델이 생성됩니다)
# 모델저장은 test파일에서 설명할게요
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10)

test_loss, test_acc = model.evaluate(x_test, y_test)

print('test_loss =', test_loss)
print('test_acc =', test_acc)

# 이게 학습이 잘 됬는지 예측하는 과정입니다
predictions = model.predict(x_test)

# 실제데이터와 예측한 과정이 같게 나옵니다 = 학습이 잘됐다
print('y_test =', y_test[:10])
print('predictions =', np.argmax(predictions[:10], axis=1))
