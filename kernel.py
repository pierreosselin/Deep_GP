## Kernel constructions
import numpy as np

class Kernel:
    """
    Kernel General Class
    :return : Kernel Object
    """
    def __init__(self):
        pass

    def build_covariance(self):
        """
        Build the cocvariance matrix for inference
        :return : Covariance Matrix
        """
        pass

    def covariance_functions(self):
        """
        Implementation of the specific covariance function for the kernel
        """
        pass

class GaussianKernel(Kernel):
    """
    Kernel General Class
    :return : Kernel Object
    """
    def __init__(self, lengthscale):
        super().__init__()
        self.lengthscale = lengthscale
        pass

    def build_covariance(self, points):
        """
        Build the covariance matrix for inference
        :return : Covariance Matrix
        """
        n = points.shape[0]
        mat = np.zeros((n,n))
        for i, el1 in enumerate(points):
            mat[i,i] = 1.
            for j, el2 in enumerate(points[(i+1):]):
                mat[i,j] = self.covariance_functions(el1, el2)
                mat[j,i] = mat[i,j]
        return mat

    def covariance_functions(self, x, y):
        """
        Implementation of the specific covariance function for the kernel
        """
        return np.exp(((x-y)**2) / self.lengthscale)
