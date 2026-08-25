# 线性回归
# 对n维输入的加权和，外加偏差
# 线性回归有显示解
import random
import torch
from d2l import torch as d2l
def synthetic_data(w,b,num_exaples):    # 生成y=Xw+b+噪声。
    X=torch.normal(0,1(num_exalpes,len(w)))
    y=torch.matmul(x,w)+b
    y+=torch.normal(0,0.01,y.shape)
    return X,y.reshape((-1,1))
true_w=torch.tensor([2,-3.4])
true_b=4.2
features,labels=synthetic_data(true_w,true_b,1000)

