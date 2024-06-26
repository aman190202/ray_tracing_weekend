from os import sys
from tqdm import tqdm

def main():

    image_width = int(256)
    image_height = int(256)

    print(f'P3\n {image_width} {image_height} \n255\n')

    for j in tqdm(range(image_height)):


        for i in range(image_width):
            r = float(i) / (image_width - 1) 
            g = float(j) / (image_height - 1)
            b = 0.0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(f'{ir} {ig} {ib}')
    
    print('Done', file=sys.stderr)

if __name__=='__main__':
    main()