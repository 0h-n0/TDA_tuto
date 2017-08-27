#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def create_circle_data(x, y, r, theta):
    """ return circle x, y data.

    :params float x: center position x
    :params float y: center position y
    :params float r: radius
    :params float theta: angle of circle
    
    """
    _x = r * np.cos(theta) + x
    _y = r * np.sin(theta) + y
    return _x, _y


def create_random_circle_data(x, y, r, a, theta, num):
    """ return circle x, y data.

    :params float x: center position x
    :params float y: center position y
    :params float a: scale paramter 
    :params float r: radius
    :params float theta: angle of circle
    
    """
    _x , _y = create_circle_data(x, y, r, theta)
    x = _x + a * np.random.uniform(-a, a, num)
    y = _y + a * np.random.uniform(-a, a, num)
    return x, y 

def plot_scatter(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    ax.axis('equal')
    plt.show()

class Simplex(object):
    def __init__(self, data):
        """
        :param np.mat data: data array
        """
        self.data = data
        self._get_dim()

    def _get_dim(self):
        self.dimx = len(self.data)
        self.dimy = len(self.data[0])
    
    def dim(self):
        return (self.dimx, self.dimy)
    

if __name__ == '__main__':
    num = 200
    theta = np.linspace(0, 2 * np.pi, num)
    x, y = create_random_circle_data(0, 0, 10, 2, theta, num)
    data = np.dstack((x, y))
    data = data[0]

    s = Simplex(data)
    s.dim()
    

