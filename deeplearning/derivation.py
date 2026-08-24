import torch
x=torch.arange(4.0)
x.requires_grad_(True)  # 自动记录x的梯度，为反向计算做铺垫
x.grad
y=2*torch.dot(x,x)
y.backward()    # 反向传播自动求导，执行完毕，x的梯度会自动保存
x.grad
x.grad==4*x
# 在默认情况下，pytorch会自动积累梯度，需要清除之前的值
x.grad.zero_()
y=x.sum()
y.backward()
x.gard