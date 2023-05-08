#1.张量的初始化
##func：各种分布的函数，para：形状参数，result：tensor
import torch
x = torch.arange(12)
x1=x.reshape([3,4])#改变张量的形状
x2=torch.zeros((2,3,4))#个数，行，列
x3=torch.rand(3,4) ##每个元素都从均值为0、标准差为1的标准⾼斯分布（正态分布）中随机采样
print(x3)

##明确的tensor的构造，通过提供包含数值的Python列表（或嵌套列表），来为所需张量中的每个元素赋予确定值。
# 在这⾥，最外层的列表对应于轴0，内层的列表对应于轴1。
x4 = torch.tensor([[1,2,3],[3,2,1]])
print(x4)

#2.张量的计算：
# 2.1常⻅的标准算术运算符（+、-、*、/和**，幂方）,按对应元素计算

x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y, x - y, x * y, x / y, x ** y,torch.exp(x))
#2.2 线性代数计算：向量点积和矩阵乘法
#2.3 张量连接
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(f"x:{X},y:{Y}")
print(X==y,torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1))##dim=0:按行叠加，dim=1，按列叠加
##2.4 张量的求和
print(X.sum())

##3，广播机制：形状不同的张量，按位计算
a=torch.arange(3).reshape(3,1)#3行1列
b=torch.arange(2).reshape(1,2)#1行2列
print(f"a:{a},b:{b},a+b:{a+b}")

##4.索引和切片
X=torch.arange(12).reshape(3,4)
print(X)
print(X[1],X[-2])
X[0,0:2]=9
X[1:4]=10
print(X)

# 5.节省内存

before = id(Y)
##方式1：
Y +=  X
##方式2：
Y[:]=X+Y
print(id(Y) == before)
print(id(Y),before)

##6.转换为其他的python对象
A = X.numpy()
B = torch.tensor(A)
print(type(A), type(B))

#只有一个元素的tensor的张量可以转化，感觉意义不大
a = torch.tensor([3.5])
a, a.item(), float(a), int(a)