import pandas as pd
import tensorflow as tf
import numpy as np

# 따로 데이터 가져오는 과정입니다 같은폴더내의 csv 파일을 사용합니다
study = pd.read_csv('Student Study Hour V2.csv')
x_study = study[['Hours']]
y_study = study[['Scores']]

#여기는 층이 하나밖에 없어서 epoch가 낮으면 제대로 학습이 안됩니다
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss="mse")

model.fit(x_study, y_study, epochs=15000, verbose=0)
# 모델의 가중치를 파악하는건데
# 학습된 모델을 가져오는 방식이 2가지입니다
# 1. 모델전체를 저장하는방법
# 2. 가중치만 저장해서 새로운 모델에 적용하는 방법
model.get_weights()
predict = model.predict(x_study)
# .h5 형식으로 저장하면 파일이 생성됩니다
model.save('test.h5')
print(y_study)
print(predict)
print('완료')
# 모델 저장만 한후 테스트는 다음파일에서 합니다