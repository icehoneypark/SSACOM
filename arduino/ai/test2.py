import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.python.keras.models import load_model

#같은데이터를 사용했습니다
study = pd.read_csv('Student Study Hour V2.csv')
x_study = study[['Hours']]
y_study = study[['Scores']]

#모델을 불러옵니다(import 잊지마세요)
model = load_model('test.h5')

predict = model.predict(x_study)
print(y_study)
print(predict)
print('완료22')