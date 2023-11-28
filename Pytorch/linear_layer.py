import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()

        self.W = torch.FloatTensor(input_dim, output_dim)
        self.b = torch.FloatTensor(output_dim)

    def forward(self, x):
        y = torch.matmul(x, self.W) + self.b
        return y

x = torch.FloatTensor(5)
mylinear = NeuralNetwork(5, 3)

y = mylinear(x)