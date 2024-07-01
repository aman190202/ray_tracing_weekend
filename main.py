from rtw import Ray,write_color,RayColor
from os import sys
from tqdm import tqdm
import numpy as np
import mlx.core as mx

JAX = 0

def main(apple=0):

    # Image
    aspect_ratio = float(4.0/3.0)
    image_width = int(720)

    # Calculating the image height and ensuring it's at least 1
    image_height = int(image_width/aspect_ratio)
    if(image_height<1): 
        image_height = 1
    
    # Camera

    focal_length = float(1)
    viewport_height = float(2)
    viewport_width = viewport_height * (float(image_width)/image_height)
    camera_center = np.array([0,0,0])

    # Calculate the vectors across the horizontal and down the vertical viewport edges

    viewport_u = np.array( [viewport_width, 0 , 0]) 
    viewport_v = np.array( [0 , -viewport_height , 0])

    # add on MLX functions

    if(apple):

        camera_center = mx.array(camera_center)
        viewport_u = mx.array(viewport_u)
        viewport_v = mx.array(viewport_v)

    # Calculate the horizontal and vertical delta vectors from pixel to pixel
    pixel_delta_u = viewport_u/ image_width
    pixel_delta_v = viewport_v/ image_height

    #  The vector from the camera center to the viewport center will be orthogonal to the viewport,
    #   hence, we are adjusting the viewport corner in a way the center aligns 

    viewport_upper_left = camera_center - np.array([0,0,focal_length]) - viewport_u/2 - viewport_v/2
    
    pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)
    
    print(f'P3\n {image_width} {image_height} \n255\n')

    print('Progress : ',file=sys.stderr)

    for j in tqdm(range(image_height)):

        for i in range(image_width):

            pixel_center = pixel00_loc + (i * pixel_delta_u) + (j* pixel_delta_v)
            ray_direction = pixel_center - camera_center

            r = Ray(camera_center,ray_direction)            
            pixel_color = RayColor(r)
            write_color(pixel_color)

    print('Done', file=sys.stderr)

if __name__=='__main__':
    main(0)

Qa = """

Doubts I had:

How does normalising and using only the y direction effects the horizontal gradient as well?


The normalization process ensures that the y-component of the ray direction vector changes smoothly across the viewport. 
Although only the y-component is used to determine the gradient, the normalization involves all components of the direction vector. 
Therefore, changes in the x-component (horizontal movement) also affect the y-component after normalization, 
leading to a gradient that appears to vary both horizontally and vertically. 

"""
