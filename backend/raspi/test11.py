
import numpy as np
import matplotlib.pyplot as plt # 시각화와 관련된 라이브러리
import numpy.linalg as LA

f = open('C:/Users/multicampus/Desktop/data.txt', 'r')
lines = f.readlines()
lists = []
cnt =0
for line in lines:
    tmp = line.replace(' ', '')
    tmp = tmp[6:]
    cnt+=1
    if(cnt<25):
        continue
    for i in range(0,12):
        list = []
        for k in range(0,40):            
            val = int(tmp[40*i+4*k+2:40*i+4*k+4] + tmp[40*i+4*k:40*i+4*k+2] , 16)
            list.append(val)
        minVal = min(list)
        maxVal = max(list)
        for j in range(0,40):
            list[j] =  (list[j] - minVal) / (maxVal - minVal)
        lists.append(list)

np_lists = np.array(lists)
# normal_lists = np_lists / LA.norm(np_lists, axis=0)
# normal_lists = (np_lists - np_lists.min(axis = 0)) / (np_lists.max(axis =0) -np_lists.min(axis = 0) )
normal_lists = np_lists
min = 10000
minIdx = 0
for i in range(0,len(lists)):

    print(normal_lists[i])
    

lists = []
#  그림 그리기
# normal_lists = np.transpose(normal_lists)
print(normal_lists.shape)

plt.imshow(normal_lists)
plt.show()
f.close()

def median_filter(img,filter_size = (3,3), stride = 1):

    img_shape = np.shape(img)

    result_shape = tuple( np.int64((np.array(img_shape)- np.array(filter_size))/stride+1))

    result = np.zeros(result_shape)

    for h in range(0, result_shape[0], stride):
        for w in range(0, result_shape[1], stride):
            tmp = img[h:h+filter_size[0], w:w+filter_size[1]]
            tmp = np.sort(tmp.ravel())
            result[h,w] = tmp[int(filter_size[0]*filter_size[1]/2)]

    return result