from Data_Loaders import Data_Loaders
from Networks import Action_Conditioned_FF


import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from torch.optim import Adam
from torch.autograd import Variable


#model = Action_Conditioned_FF()
#loss_fn = nn.CrossEntropyLoss()
#optimizer = Adam(model.parameters(), lr=0.001, weight_decay=0.0001)


def saveModel(model):
    path = r"saved/saved_model.pkl"
    torch.save(model.state_dict(), path,_use_new_zipfile_serialization=False)




def train_model(no_epochs):

    

    batch_size = 72
    data_loaders = Data_Loaders(batch_size)
    model = Action_Conditioned_FF()
    model = model.double()
    best_accuracy = 0.0
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("The model will be running on", device, "device")
    model.to(device)
    
    loss = nn.MSELoss()
    optimizer = torch.optim.SGD(params=model.parameters(), lr=0.7)
    losses = []
    min_loss = model.evaluate(model, data_loaders.train_loader, nn.MSELoss())
    losses.append(min_loss)


    for epoch_i in range(no_epochs):
        model.train()
        for idx, sample in enumerate(data_loaders.train_loader): # sample['input'] and sample['label']
            X, y = sample['input'], sample['label']
            X = torch.from_numpy(X).double()
            y = torch.tensor(sample['label'])
            y_pred = model.forward(X)
            
            #y_pred =torch.tensor(y_pred, requires_grad=False)
            
            l = loss(y,y_pred)
            l.backward
            optimizer.step()
            optimizer.zero_grad()
    saveModel(model)


if __name__ == '__main__':
    
    no_epochs = 1
    train_model(no_epochs)
