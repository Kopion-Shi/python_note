import torchvision
from torchvision import transforms

from torch.utils import data
class Basemodel():
    def __init__(self,model=None,train_date=None) -> None:
        self.model=model
        self.train_date=train_date
    
    def train_run(self):
        pass

    def train_date(self):
        pass
    


    def get_dataloader_workers(self):
        """Use 4 processes to read the data.

        Defined in :numref:`sec_fashion_mnist`"""
        return 4
    def load_data_fashion_mnist(self,batch_size, resize=None):
        """Download the Fashion-MNIST dataset and then load it into memory.

        Defined in :numref:`sec_fashion_mnist`"""
        trans = [transforms.ToTensor()]
        if resize:
            trans.insert(0, transforms.Resize(resize))
        trans = transforms.Compose(trans)
        mnist_train = torchvision.datasets.FashionMNIST(
            root="../data", train=True, transform=trans, download=True)
        mnist_test = torchvision.datasets.FashionMNIST(
            root="../data", train=False, transform=trans, download=True)
        return (data.DataLoader(mnist_train, batch_size, shuffle=True,
                                num_workers=self.get_dataloader_workers()),
                data.DataLoader(mnist_test, batch_size, shuffle=False,
                                num_workers=self.get_dataloader_workers()))
