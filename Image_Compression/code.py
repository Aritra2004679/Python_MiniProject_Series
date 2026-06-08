import numpy as np
from PIL import Image

# Open image and convert to grayscale
im = Image.open('lena.jfif').convert('L')

pixelMap = im.load()

img = Image.new(im.mode, im.size)
pixelNew = img.load()

'''
0-31   = 0
32-63  = 1
64-95  = 2
96-127 = 3
128-159 = 4
160-191 = 5
192-223 = 6
224-255 = 7
'''

for i in range(img.size[0]):
    for j in range(img.size[1]):

        if 0 <= pixelMap[i, j] <= 31:
            pixelNew[i, j] = 0

        elif 32 <= pixelMap[i, j] <= 63:
            pixelNew[i, j] = 1

        elif 64 <= pixelMap[i, j] <= 95:
            pixelNew[i, j] = 2

        elif 96 <= pixelMap[i, j] <= 127:
            pixelNew[i, j] = 3

        elif 128 <= pixelMap[i, j] <= 159:
            pixelNew[i, j] = 4

        elif 160 <= pixelMap[i, j] <= 191:
            pixelNew[i, j] = 5

        elif 192 <= pixelMap[i, j] <= 223:
            pixelNew[i, j] = 6

        elif 224 <= pixelMap[i, j] <= 255:
            pixelNew[i, j] = 7

# Save compressed image
img.save('lena_2.jpg')

# Read compressed image as NumPy array
J = np.asarray(Image.open('lena_2.jpg'))

print("Compressed image shape:", J.shape)
print("Compression completed successfully!")