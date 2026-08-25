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
# 将某些计算移动到梯度记录之外
x.gard.zero_()
y=x*x
u=y.detach()       # detach()方法表示梯度截断，不再继续回传--把y当成一个常数而不是一个关于x的函数
z=u*x              # u也被当做一个常数使用而不是关于x的函数
z.sum().backward()
x.grad ==u
