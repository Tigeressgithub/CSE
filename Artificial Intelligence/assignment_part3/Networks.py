import torch
import torch.nn as nn
import numpy as np


class Action_Conditioned_FF(nn.Module):
    def __init__(self,input_size=6,hidden_size=4,output_size=1):
# STUDENTS: __init__() must initiatize nn.Module and define your network's
# custom architecture
        super(Action_Conditioned_FF,self).__init__()
        self.input_to_hidden=nn.Linear(input_size,hidden_size)
        self.nonlinear_activation = nn.Sigmoid()
        self.hidden_to_output = nn.Linear(hidden_size,output_size)
        #self.loss_function = nn.MSELoss()
    def forward(self, input):
# STUDENTS: forward() must complete a single forward pass through your network
# and return the output which should be a tensor
        hidden = self.input_to_hidden(input)
        hidden = self.nonlinear_activation(hidden)
        output = self.hidden_to_output(hidden)
        return output


    def evaluate(self, model, test_loader, loss_function):
# STUDENTS: evaluate() must return the loss (a value, not a tensor) over your testing dataset. Keep in
# mind that we do not need to keep track of any gradients while evaluating the
# model. loss_function will be a PyTorch loss function which takes as argument the model's
# output and the desired output.
        #input = torch.from_numpy(test_loader['input'])
        losses = list()
        y_list = list()
        for t in test_loader:
            X = t['input']
            X = torch.from_numpy(X)
            y_hat = model(X)
            #y = y.float()
            
            y = torch.tensor(t['label'])
            loss = loss_function(y,y_hat)
            #input = torch.randn(3, requires_grad=True)
            #target = torch.empty(3).random_(2)
            #loss = loss_function(input.reshape(-1),target.reshape(-1))
            losses.append(loss.item())
        losses=sum(losses)
        # print(type(losses))
        # print(losses)
        return losses

def main():
    model = Action_Conditioned_FF()
    model.double()
    # data = np.genfromtxt(r'C:\Users\MV\Desktop\CSE 571\assignment_part3\saved\savedtraining_data.csv', delimiter=',')
    # temp = list()
    # for d in data:
    #     row = {'input': d[0:6],'label':d[6]}
    #     temp.append(row)
    
    # r = model.evaluate(model=model, test_loader=temp,loss_function= nn.MSELoss())
        
        
if __name__ == '__main__':
    main()
