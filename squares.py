import numpy as np
import torch

def numpy_squares(k):
    output = np.arrange(1,k+1)
    return output ** 2
    # your code here

def torch_squares(k):
    output = torch.arrange(1,k+1)
    return output ** 2
    # your code here
