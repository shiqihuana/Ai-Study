# 使用torch创建张量
import torch
# torch.arange(个数，数值类型).reshape()
x=torch.arange(12,dtype=torch.float32).reshape(3,4)
# torch.tensor([[[..列明各元素]]..,[[..]]..])
y=torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,3,2,1]])
# torch.cat()
print(x,"\n",y)
# 按行相加(行变多)
torch.cat((x,y),dim=0)
# 按列相加(列变多)
torch.cat((x,y),dim=1)

# 三维张量相加
tensor1=torch.arange(24).reshape(3,4,2)
tensor1
torch.cat((tensor1,tensor1),dim=0)
torch.cat((tensor1,tensor1),dim=1)
torch.cat((tensor1,tensor1),dim=2)

# sum求和
tensor1.sum()

a=torch.arange(3).reshape(3,1)
b=torch.arange(2).reshape(1,2)
a
b
a+b
# 内存
Y=3
before=id(Y)
before
Y=5
id(Y)
Y==before
Y