import torch
from torch import nn
from d2l import torch as d2l
import base_model

class Alexnet(base_model.Basemodel):
    def __init__(self, model=None, train_date=None) -> None:
        super().__init__(model, train_date)
        self.train_iter=None
        self.test_iter=None
        self.net=None

    def mode(self):
        Alexnet = nn.Sequential(
            # 这⾥使⽤⼀个11*11的更⼤窗⼝来捕捉对象。
            # 同时，步幅为4，以减少输出的⾼度和宽度。
            # 另外，输出通道的数⽬远⼤于LeNet
            nn.Conv2d(1, 96, kernel_size=11, stride=4, padding=1), nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            # 减⼩卷积窗⼝，使⽤填充为2来使得输⼊与输出的⾼和宽⼀致，且增⼤输出通道数
            nn.Conv2d(96, 256, kernel_size=5, padding=2), nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            # 使⽤三个连续的卷积层和较⼩的卷积窗⼝。
            # 除了最后的卷积层，输出通道的数量进⼀步增加。
            # 在前两个卷积层之后，汇聚层不⽤于减少输⼊的⾼度和宽度
            nn.Conv2d(256, 384, kernel_size=3, padding=1), nn.ReLU(),
            nn.Conv2d(384, 384, kernel_size=3, padding=1), nn.ReLU(),
            nn.Conv2d(384, 256, kernel_size=3, padding=1), nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Flatten(),
            # 这⾥，全连接层的输出数量是LeNet中的好⼏倍。使⽤dropout层来减轻过拟合
            nn.Linear(6400, 4096), nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(4096, 4096), nn.ReLU(),
            nn.Dropout(p=0.5),
            # 最后是输出层。由于这⾥使⽤Fashion-MNIST，所以⽤类别数为10，⽽⾮论⽂中的1000
            nn.Linear(4096, 10))
        return Alexnet

    def model_demo(self):
        X = torch.randn(1, 1, 224, 224)
        for layer in self.mode():
            X=layer(X)
            print(layer.__class__.__name__,'output shape:\t',X.shape)


    def train_date_(self):
        batch_size = 128
        train_iter, test_iter = super().load_data_fashion_mnist(batch_size, resize=224)
        print(train_iter,test_iter)
        return train_iter, test_iter


    def train_run(self):
        self.train_iter, self.test_iter=self.train_date_()
        self.net=self.mode()
        lr, num_epochs = 0.01, 10
        d2l.train_ch6(self.net, self.train_iter, self.test_iter, num_epochs, lr, d2l.try_gpu())

if __name__=='__main__':
    obj=Alexnet()
    obj.train_run()