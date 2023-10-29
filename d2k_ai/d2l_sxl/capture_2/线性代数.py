### 性代数中的基本数学对象、算术和运算，并⽤数学符号和相应的代码实现来表⽰它们

#1.标量
import torch
x = torch.tensor(3.0)
y = torch.tensor(2.0)
print(x + y, x * y, x / y, x**y)
##加法、乘法、除法和指数
#2.向量：形式上看，标量组成的列表
x = torch.arange(4)
print(x)
print(x[3])#索引
len(x)#长度
print(x.shape)#向量或轴的维度被⽤来表⽰向量或轴的⻓度，即向量或轴的元素数量。然⽽，张量的维度⽤来表⽰张量具有的轴数。在这个意义上，张量的某个轴的维数就是这个轴的⻓度。

##矩阵
A=torch.arange(20).reshape(5,4)
print(A)
print(A.T)#转置
#对称矩阵（symmetric matrix）A等于其转置：A = A⊤。
B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B)
print(B==B.T)

#张量 张量是描述具有任意数量轴的n维数组的通⽤⽅法。
X = torch.arange(24).reshape(2, 3, 4)
print(X)

##张量的基本性质
print('张量的基本性质')
A=torch.arange(20,dtype=torch.float32).reshape(5,4)
print(id(A))
B=A.clone()#通过分配新内存，将A的一个副本分配给B
print(id(B))
print(A,A+B,id(A))
####两个矩阵的按元素乘法称为Hadamard积
print(A*B)

##将张量乘以或加上⼀个标量不会改变张量的形状，其中张量的每个元素都将与标量相加或相乘
a = 2
X = torch.arange(24).reshape(2, 3, 4)
print(a + X, (a * X).shape)


###降维
#对任意张量进⾏的⼀个有⽤的操作是计算其元素的和
x = torch.arange(4, dtype=torch.float32)
print(x,x.T.size(), x.sum())

print(A,A.size())
print(A.sum(axis=0))##沿着列
print(A.sum(axis=1))##沿着行
#与求和相关的量是平均值
print(A.mean(),A.sum()/A.numel())
##沿着某一轴的平均值
print(A.mean(),A.sum(axis=0)/A.shape[0])




