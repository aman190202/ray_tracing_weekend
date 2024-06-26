import numpy as np

def length_squared(arr):
    return arr[0]**2 + arr[1]**2 + arr[2]**2

def length(arr):
    return np.sqrt(length_squared(arr))

def unit_vector(arr):
    return arr/length(arr)

def x(arr):
    return arr[0]

def y(arr):
    return arr[1]

def z(arr):
    return arr[2]

def double_dot(a,b):
    return (a*b).sum()

def dot(a , b ):
    return np.dot(a,b)

def write_color(arr):
    r,g,b = arr[0],arr[1],arr[2]

    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    print(f'{rbyte} {gbyte} {bbyte} \n')


class ray:
    def __init__(self ,origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self , t : float):
        return self.origin + t*self.direction









