# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 06:33:45 2021

@author: MV
"""

from Data_Loaders import Data_Loaders
from Networks import Action_Conditioned_FF


import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from torch.optim import Adam
from torch.autograd import Variable


path = r"saved/saved_model.pkl"

#model = Action_Conditioned_FF(*args, **kwargs)
model = Action_Conditioned_FF()
model.double()
model.load_state_dict(torch.load(path))

batch_size = 72
data_loaders = Data_Loaders(batch_size)
#min_loss = model.evaluate(model, data_loaders.train_loader, nn.MSELoss())
i=0

for d in data_loaders.test_loader:
    X = torch.from_numpy(d['input'])
    print(model(X))
    i = i + 1
    if (i > 20):
        break
    