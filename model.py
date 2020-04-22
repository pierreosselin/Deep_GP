## Model construction of the deep gaussian Processes
import numpy as np

class DeepGP:
    """
    Deep Gaussian Processes main class
    """
    def __init__(self,layers, listkernels):
        self.layers = layers #list couple (beg, end)
        self.listkernels = listkernels

    def inference(self, points):
        n = points.shape[0]
        for c, kernel in zip(self.layers, self.listkernels):
            points = np.random.multivariate_normal(np.zeros(n) , kernel.build_covariance(points))
        return points
