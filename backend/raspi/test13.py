
import numpy as np
import matplotlib.pyplot as plt # 시각화와 관련된 라이브러리
import numpy.linalg as LA

f = open('C:/Users/multicampus/Desktop/data.txt', 'r')
lines = f.readlines()
# lists =np.array([]) 
lists  =[]
cnt = 0
for line in lines:

    cnt+=1
    if(cnt==10):
        break
    tmp = line.replace(' ', '')
    tmp = tmp[6:]
        
    for i in range(0,2):
        list = []
        for k in range(0,240):            
            val = int(tmp[240*i+4*k+2:240*i+4*k+4] + tmp[240*i+4*k:240*i+4*k+2] , 16)
                        
            list.append(val)
        # np_list = np.array(list)
        # normal_list = np_list/LA.norm(np_list)
        # print(normal_list.size)
        # lists = np.append(normal_list, list.reshape(1,1,240), axis=0)
        lists.append(list)


np_lists = np.array(lists)
np_lists = np.transpose(lists)
# normal_lists = np_lists / LA.norm(np_lists, axis=0)
# normal_lists = (np_lists - np_lists.min(axis = 0)) / (np_lists.max(axis =0) -np_lists.min(axis = 0) )
normal_lists = np_lists
for i in range(0,len(normal_lists)):
    print(normal_lists[i])
    
#  그림 그리기
plt.imshow(normal_lists)
plt.show()
f.close()