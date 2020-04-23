## Test
from model import DeepGP
from kernel import GaussianKernel
from plot import draw_function

test = DeepGP([(1,2), (2,1)], [GaussianKernel(0.1), GaussianKernel(0.1)])
draw_function(-1, 1, test)