import numpy as np
import cv2
import glob
import os
from argparse import ArgumentParser

parser = ArgumentParser(description='Tawawa Filter')
parser.add_argument('-p','--path', help='Directory', default="./inputs/")
args = parser.parse_args()

filelist = sorted(glob.glob(args.path + "*.png")) # change to jpg if needed

for file in filelist:
    # Read grayscale input
    input = cv2.imread(file, cv2.IMREAD_COLOR)

    # Matrix to turn pixels into orangeish pixels
    colour_matrix = np.array([0, 0.55, 1])

    # Perform the color transformation
    inverted_input = 255 - input
    output = (inverted_input * colour_matrix).astype(np.uint8)

    # Invert it again before saving
    cv2.imwrite(f"{os.path.splitext(file)[0]}_blue.png", 255 - output)
