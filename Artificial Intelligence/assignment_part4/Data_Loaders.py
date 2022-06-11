import torch
import torch.utils.data as data
import torch.utils.data.dataset as dataset
from torch.utils.data import DataLoader

import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import random
import sys
#import pandas as pd
class Nav_Dataset(dataset.Dataset):
    def __init__(self):
        self.data = np.genfromtxt(r'saved/training_data.csv', delimiter=',', skip_header=2)
        self.n_samples = self.data.shape[0]

        random.shuffle(self.data)
        #print("data is ",self.data[0])
        
# STUDENTS: it may be helpful for the final part to balance the distribution of your collected data
        # normalize data and save scaler for inference
        self.scaler = MinMaxScaler()
        self.normalized_data = self.scaler.fit_transform(self.data) #fits and transforms
        pickle.dump(self.scaler, open("saved/scaler.pkl", "wb")) #save to normalize at inference

        self.x = torch.from_numpy(self.normalized_data[:, 0:6])
        self.y = torch.from_numpy(self.normalized_data[:, [6]])

    def __len__(self):
# STUDENTS: __len__() returns the length of the dataset
        #rows = len(self.data)
        return self.n_samples

    def __getitem__(self, idx):
        if not isinstance(idx, int):
            #print(idx.item())
            #print(idx)
            #print("idx is ",idx)
            #self.x[idx]
            #return self.x[idx],self.y[idx]
            return {'input': self.x[idx], 'label': self.y[idx]}
            #print(idx)
            
            #return idx
        return {'input': self.x[idx], 'label': self.y[idx]}
# STUDENTS: for this example, __getitem__() must return a dict with entries {'input': x, 'label': y}
# x and y should both be of type float32. There are many other ways to do this, but to work with autograding
# please do not deviate from these specifications.


class Data_Loaders():
    def __init__(self, batch_size):
        self.nav_dataset = Nav_Dataset()

        self.dataloader = DataLoader(dataset=self.nav_dataset,batch_size=batch_size)

        # Version 1
        # l = round(len(self.nav_dataset)/1.5)
        #
        # temp = self.nav_dataset.normalized_data[:l]
        # temp1 = self.nav_dataset.normalized_data[l:]
        # temp2 = self.nav_dataset.normalized_data
        #
        #
        # #self.train_loader.data = self.train_loader.data
        # self.train_loader = list()
        # self.test_loader = list()
        # self.whole_loader = list()
        # for r in temp:
        #     i = r[0:6]
        #     o = r[6]
        #     row = {'input':i,'label':o}
        #     self.train_loader.append(row)
        # for r in temp1:
        #     i = r[0:6]
        #     #i = torch.from_numpy(i)
        #     #i = i.double()
        #     o = r[6]
        #
        #     row = {'input':i,'label':o}
        #     self.test_loader.append(row)
        #
        # for r in temp2:
        #     i = r[0:6]
        #     o = r[6]
        #     row = {'input':i,'label':o}
        #     self.whole_loader.append(row)
# STUDENTS: randomly split dataset into two data.DataLoaders, self.train_loader and self.test_loader
# make sure your split can handle an arbitrary number of samples in the dataset as this may vary

def main():
    batch_size = 5
    data_loaders = Data_Loaders(batch_size)
    
    
    # STUDENTS : note this is how the dataloaders will be iterated over, and cannot be deviated from
    #for idx, sample in enumerate(data_loaders.train_loader):
    #    print("IDX",idx)
    #    print("sample: ",sample)
    for idx, sample in enumerate(data_loaders.dataloader):
        _, _ = sample['input'], sample['label']
        print(idx)
        print(sample['input'])
        if(idx>30):
            break

    # for idx, sample in enumerate(data_loaders.dataloader):
    #     _, _ = sample['input'], sample['label']

    # for idx, sample in enumerate(data_loaders.train_loader):
    #     _, _ = sample['input'], sample['label']
    # for idx, sample in enumerate(data_loaders.test_loader):
    #     _, _ = sample['input'], sample['label']
    

if __name__ == '__main__':
    main()
