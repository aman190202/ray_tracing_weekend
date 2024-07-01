from concurrent.futures import ThreadPoolExecutor
from rtw import ray, write_color, ray_color
from os import sys
from tqdm import tqdm
import numpy as np


JAX = 0


def process_row(j, image_width, pixel00_loc, pixel_delta_u, pixel_delta_v, camera_center):
    row_colors = []
    for i in range(image_width):
        pixel_center = pixel00_loc + (i * pixel_delta_u) + (j * pixel_delta_v)
        ray_direction = pixel_center - camera_center
        r = ray(camera_center, ray_direction)
        pixel_color = ray_color(r)
        row_colors.append(pixel_color)
    return row_colors


def main():
    # Image
    aspect_ratio = float(16.0 / 9.0)
    image_width = int(2000)

    # Calculating the image height and ensuring it's at least 1
    image_height = int(image_width / aspect_ratio)
    if image_height < 1:
        image_height = 1

    # Camera
    focal_length = float(1)
    viewport_height = float(2)
    viewport_width = viewport_height * (float(image_width) / image_height)

    camera_center = np.array([0, 0, 0])

    # Calculate the vectors across the horizontal and down the vertical viewport edges
    viewport_u = np.array([viewport_width, 0, 0])
    viewport_v = np.array([0, -viewport_height, 0])

    # Calculate the horizontal and vertical delta vectors from pixel to pixel
    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    # The vector from the camera center to the viewport center will be orthogonal to the viewport,
    # hence, we are adjusting the viewport corner in a way the center aligns
    viewport_upper_left = camera_center - np.array([0, 0, focal_length]) - viewport_u / 2 - viewport_v / 2

    pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

    print(f'P3\n{image_width} {image_height} \n255\n')

    print('Progress : ', file=sys.stderr)

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_row, j, image_width, pixel00_loc, pixel_delta_u, pixel_delta_v, camera_center)
            for j in range(image_height)
        ]

        for future in tqdm(futures):
            row_colors = future.result()
            for color in row_colors:
                write_color(color)

    print('Done', file=sys.stderr)


if __name__ == '__main__':
    main()