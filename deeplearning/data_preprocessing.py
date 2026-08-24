import os
import pandas as pd
import torch
# os.makedirs()创建文件夹，os.path.join('文件夹目录','文件夹名称')
# exist_ok参数：在文件已被创建后不抛出错误
os.makedirs(os.path.join('.','data'),exist_ok=True)
data_file=os.path.join('D:/github/Ai-Study/data/house_tiny.csv')
# 以w模式打开文件，w：当文件里面含有内容时直接覆盖原内容
with open(data_file,'w')as f:
    f.write('NumRooms,Alley,Price\n')       #列名
    f.write('NA,Pave,127500\n')             #每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')
# 读取csv文件
data=pd.read_csv(data_file)
print(data)
# iloc[行,列]   切片
inputs,outputs=data.iloc[:,0:2],data.iloc[:,2]
# 把数字列的值求平均后填充到缺失值位置上
inputs["NumRooms"] = inputs["NumRooms"].fillna(inputs["NumRooms"].mean())
# get_dummies是pands的独热编码函数，输入inputs,对类别列进行分类
inputs=pd.get_dummies(inputs,dummy_na=True)
print(inputs)
# 把数据类型转换为张量
x = torch.tensor(inputs.values.astype("float32"))
y = torch.tensor(outputs.values.astype("float32"))
# 向量间的点乘 vec1 @ vec2
vec1=torch.ones(4,dtype=torch.float32)
vec2=torch.tensor([1.0,2.,3.,4.])
print(torch.dot(vec1,vec2))
# 矩阵和向量间的点乘 mat1 @ vec3
vec3=torch.arange(4)
mat1=torch.arange(12).reshape(3,4)
torch.mv(mat1,vec3)
# 矩阵相乘 mat1 @ mat2
mat2=torch.arange(12).reshape(4,3)
torch.mm(mat1,mat2)
# L2范数是向量元素平方和的平方根
vec4=torch.tensor([3.0,-4.0])
torch.norm(vec4)
# L1范数是向量元素的绝对值之和 torch.abs()求各元素的绝对值，.sum()方法对向量所有元素求和
torch.abs(vec4).sum()
# 矩阵的F范数是矩阵元素的平方和的平方根
mat1=mat1.to(torch.float32)
torch.norm(mat1)