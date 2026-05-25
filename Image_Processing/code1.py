# Flipping the Image

from PIL import Image

try:

    # Open the Image
    img = Image.open('obtained.png')

    # Flip Horizontally
    transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # Save Corrected Image
    transposed_img.save('corrected.png')

    print("Done Flipping")
    print("corrected.png Generated Successfully!")

except FileNotFoundError:

    print("Error: obtained.png file not found!")

except Exception as e:

    print("Error:", e)