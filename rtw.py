import numpy as np

class Ray:

    def __init__(self ,origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self , t : float):
        return self.origin + t*self.direction

class HitRecord:

    def __init__(self, p : np.array, normal : np.array, t : float):
        self.p = p
        self.normal = normal
        self.t = t

class Hittable:

    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, rec : HitRecord) -> bool:
        raise NotImplementedError("Subclass should implement this")

class Sphere(Hittable):
    
    def __init__(self, center : np.array, radius : float):
        self.center = center
        self.radius = max(0,radius)
    
    def hit(self, r : Ray, ray_tmin : float, ray_tmax : float, rec : HitRecord) -> bool:
        oc = self.center - self.r.origin
        a = length_squared(r.direction)
        h = np.dot(r.direction, oc)
        c = length_squared(oc) - self.radius**2

        discriminant = h ** 2 - a * c
        if(discriminant < 0):
            return False
        
        
        # Find the nearest root that lies in the acceptable range

        root = (h - np.sqrt(discriminant))/a
        if(root <= ray_tmin or ray_tmax <= root):
            root = ( h + np.sqrt(discriminant))/a
            if(root <= ray_tmin or ray_tmax <= root):
                return False
        
        rec.t = root
        rec.p = r.at(rec.t)
        rec.normal = (rec.p - self.center) / self.radius

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


def hit_sphere(center : np.array, radius : float, r : Ray):
    oc = center - r.origin
    a =  length_squared(r.direction) # np.dot(r.direction,r.direction)
    # b = -2.0 * np.dot(r.direction, oc)
    h = np.dot(r.direction,oc)
    c = length_squared(oc) - radius ** 2 # np.dot(oc,oc) - radius**2
    discriminant = h * h - a * c# b**2 - 4*a*c

    if(discriminant < 0):
        return -1.0
    else:
        #return ( -b - np.sqrt(discriminant))/(2. * a)
        return (h - np.sqrt(discriminant))/a
    

def RayColor(r : Ray) -> np.array: # Gradient

    t = hit_sphere(np.array([0,0,-1]),0.5,r)

    if(t>0.0):
        N = unit_vector(r.at(t) - np.array([0,0,-1]))
        return 0.5 * np.array([N[0]+1, N[1] + 1, N[2] + 1])

    unit_direction = unit_vector(r.direction)
    a = float(0.5 * ( unit_direction[1] + 1.0))
    return (1.0 - a) * np.array([1.,1.,1.])+ a * np.array([0.5,0.7,1.0])


