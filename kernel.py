## Kernel constructions

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
