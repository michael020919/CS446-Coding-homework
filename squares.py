import numpy
import torch

def numpy_squares(k):
    output = np.arrage(1,k+1)
    return output ** 2
 # your code here

def torch_squares(k):
""" return (1 , 4 , 9 , ... , k ^2) as a torch array """
    output = torch.arrange(1,k+1)
    return output ** 2
# your code here
