
import scipy.io as scio
import numpy as np
import math 

data_path='./data/LETTER.mat'
data = scio.loadmat(data_path)
print(type(data))
print(list(data.keys()))
print('type of data',type(data['data']),'shape of data',data['data'].shape)
print('type of letter',type(data['letter']),'shape of letter',data['letter'].shape)

def edclid_metric(A,B):
    dis = math.sqrt(sum([(a - b) ** 2 for (a, b) in zip(A, B)]))



# data_temp=[]
# for k in data.items():
#     data_temp.append(k)
# data_np = np.array(data_temp)
# print(type(data_np))
# print(data_np)
# print(data_np.shape)