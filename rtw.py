import numpy as np
from os import sys

class ray:
    def __init__(self ,origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self , t : float):
        return self.origin + t*self.direction

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


def hit_sphere(center : np.array, radius : float, r : ray) -> bool:
    oc = center - r.origin
    a = np.dot(r.direction,r.direction)
    b = -2.0 * np.dot(r.direction, oc)
    c = np.dot(oc,oc) - radius**2
    discriminant = b**2 - 4*a*c
    return (discriminant>=0)

def ray_color(r : ray) -> np.array: # Gradient

    if hit_sphere(np.array([0,0,-1]),0.5,r):
        return np.array([1,0,0])

    unit_direction = unit_vector(r.direction)
    a = float(0.5 * ( unit_direction[1] + 1.0))
    return (1.0 - a) * np.array([1.,1.,1.])+ a * np.array([0.5,0.7,1.0])


