## Plot Module for the deep gaussian Processes
import matplotlib.pyplot as plt
import numpy as np
def draw_function(xmin, xmax, test):
    points = np.linspace(xmin, xmax, 100)
    values = test.inference(points)
    plt.plot(points, values)
    plt.show()