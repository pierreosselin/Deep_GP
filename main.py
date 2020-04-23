## Test
from model import DeepGP
from kernel import GaussianKernel
import numpy as np

test = DeepGP([(2,2), (2,2)], [GaussianKernel(1.), GaussianKernel(1.)])

test.inference(np.array([[1,2], [3,4], [5,6]]))
