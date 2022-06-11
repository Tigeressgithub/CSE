import torch
import torch.nn as nn
import numpy as np


class Action_Conditioned_FF(nn.Module):
    def __init__(self,input_size=6,hidden_size=4,output_size=1):
# STUDENTS: __init__() must initiatize nn.Module and define your network's
# custom architecture
        super(Action_Conditioned_FF,self).__init__()
        self.hidden_size = hidden_size
        self.hidden_size2 = 4
        self.input_size = input_size
        self.batch_size = 72

        # LSTM
        # self.lstm_layer = nn.LSTMCell(input_size,hidden_size,bias=True)
        # self.fc_layer = nn.Linear(hidden_size,output_size)

        # self.double()
        self.input_to_hidden=nn.Linear(input_size,self.hidden_size)
        self.hidden2 = nn.Linear(self.hidden_size,self.hidden_size2)
        #self.hidden3 = nn.Linear(self.hidden_size2,self.hidden_size2)
        self.nonlinear_activation = nn.ReLU()
        self.nonlinear_activation2 = nn.Sigmoid()
        self.hidden_to_output = nn.Linear(self.hidden_size2,output_size)
        #self.loss_function = nn.MSELoss()
    #def forward(self, input,hidden_state, cell_state):
    def forward(self, input):
# STUDENTS: forward() must complete a single forward pass through your network
# and return the output which should be a tensor
        # LSTM
        # hidden_state, cell_state = self.lstm_layer(input,(hidden_state,cell_state))
        # output = self.fc_layer(hidden_state)

        # linear
        #input = input.double()
        hidden = self.input_to_hidden(input)
        hidden = self.nonlinear_activation(hidden)

        # hidden = self.hidden2(hidden)
        # hidden = self.nonlinear_activation2(hidden)

        #hidden = self.hidden3(hidden)
        #hidden = self.nonlinear_activation2(hidden)


        output = self.hidden_to_output(hidden)
        return output
        #return output, (hidden_state, cell_state)

    # def init_hidden(self):
    #     hidden_state = (torch.zeros(batch_size,hidden_size))
    #     cell_state = torch.zeroes(batch_size,hidden_size)
    #     return (hidden_state,cell_state)


    def evaluate(self, model, test_loader, loss_function):
# STUDENTS: evaluate() must return the loss (a value, not a tensor) over your testing dataset. Keep in
# mind that we do not need to keep track of any gradients while evaluating the
# model. loss_function will be a PyTorch loss function which takes as argument the model's
# output and the desired output.
        #input = torch.from_numpy(test_loader['input'])
        #model = model.double()
        model.eval()

        losses = list()
        y_list = list()
        with torch.no_grad():
            for t in test_loader:
                X = t['input']
                #X = torch.from_numpy(X).double()
                y_hat = model(X)
                #y_hat = y_hat
                #y = y.float()

                y = t['label']
                #loss1 = loss_function(y,y_hat)
                y_hat = y_hat > 0.85
                print(y_hat)
                exit()
                # def get_accuracy(y_true, y_prob):
                #     print(y_true.ndim)
                #     print(y_true.size())
                #     assert (y_true.ndim == 1 and y_true.size() == y_prob.size())
                #     y_prob = y_prob > 0.85
                #     return (y_true == y_prob).sum().item() / y_true.size(0)

                #losses.append(get_accuracy(y,y_hat))

        returnl = sum(losses)/len(losses)
        del losses
        # print(type(losses))
        # print(losses)
        return returnl

def main():
    model = Action_Conditioned_FF()
    #model.double()
    # data = np.genfromtxt(r'C:\Users\MV\Desktop\CSE 571\assignment_part3\saved\savedtraining_data.csv', delimiter=',')
    # temp = list()
    # for d in data:
    #     row = {'input': d[0:6],'label':d[6]}
    #     temp.append(row)
    
    # r = model.evaluate(model=model, test_loader=temp,loss_function= nn.MSELoss())
        
        
if __name__ == '__main__':
    main()
