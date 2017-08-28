#!/usr/bin/env python
import scipy.spatial.distance as dist
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

        self.group = [[] for i in range(self.dimx)]
        self.max_r = 3.0
        self.min_r = 0.2
        self.delta_r = 0.2
        self.rlist = arange(0.2, 3, 0.2)

    def _get_dim(self):
        self.dimx = len(self.data)
        self.dimy = len(self.data[0])
    
    def dim(self):
        return (self.dimx, self.dimy)

    def filtration(self):
        for idx in range(len(self.data)):
            grouplist = []
            for jdx in range(idx+1, len(self.data)):            
                for r in self.rlist:
                    if self.data[idx, 0] - self.data[jdx, 0] < r and \
                       self.data[idx, 1] - self.data[jdx, 1] < r:
                        length = cdist(self.data[idx], self.data[jdx], 'euclidean')
                        if length < r:
                            grouplist.append(jdx)
            self.group[idx].append(grouplist)
    

if __name__ == '__main__':
    num = 50
    theta = np.linspace(0, 2 * np.pi, num)
    x, y = create_random_circle_data(0, 0, 10, 2, theta, num)
    data = np.dstack((x, y))
    data = data[0]
    s = Simplex(data)
    s.dim()
    s.filtration()
    print(group)
    

