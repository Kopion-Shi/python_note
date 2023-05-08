import os


##写数据
###获取当前项py的根目录
class Datacontrol():
    pro_path=os.path.dirname(os.path.abspath(__file__))
    def writ_data(self):
        pass
    def read_data(self,data_file):
        import pandas as pd
        data_path=os.path.join(self.pro_path,data_file)
        data = pd.read_csv(data_path)
        return data
    
    def process_dumpy_data(self,data_file):
        """
        通过位置索引iloc，我们将data分成inputs和outputs，其中前者为data的前两列，⽽后者为data的最后⼀列。
        对于inputs中缺少的数值，我们⽤同⼀列的均值替换“NaN”项。
        """
        data=self.read_data(data_file)
        inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
        inputs = inputs.fillna(inputs.mean())
        return inputs,outputs
    

class DatacontrolCvs(Datacontrol):   
    def write_data(self):
        os.makedirs(os.path.join(self.pro_path,'data'), exist_ok=True)
        data_file = os.path.join(self.pro_path,'data', 'house_tiny.csv')
        with open(data_file, 'w') as f:
            f.write('NumRooms,Alley,Price\n') # 列名
            f.write('NA,Pave,127500\n') # 每⾏表⽰⼀个数据样本
            f.write('2,NA,106000\n')
            f.write('4,NA,178100\n')
            f.write('NA,NA,140000\n')
    def read_data(self,data_file):
        return super().read_data(data_file)
    
if __name__=='__main__':
    fp=DatacontrolCvs()
    data=fp.read_data(os.path.join('data', 'house_tiny.csv'))
    print(data)
    preprocess_data=fp.process_dumpy_data(os.path.join('data', 'house_tiny.csv'))
    print(preprocess_data[0],'===x10^ok',preprocess_data[1])