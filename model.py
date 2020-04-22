## Model construction of the deep gaussian Processes

class DeepGP:
    """
    Deep Gaussian Processes main class
    """
    def __init__(self,nb_layers, listkernels):
        self.nb_layers = nb_layers
        self.listkernels = listkernels

    def inference(self, points):
        pass
