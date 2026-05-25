# Image Enhancement using CLAHE
import cv2

try:
    # Read the Image
    img = cv2.imread('crime.png')

    # Check if image loaded successfully
    if img is None:
        print("Error: crime.png not found!")
        exit()

    # Create CLAHE Object
    clahe = cv2.createCLAHE()

    # Convert Image to Gray Scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE Enhancement
    enh_img = clahe.apply(gray_img)

    # Save Enhanced Image
    cv2.imwrite('enhanced.png', enh_img)

    print("Done Enhancing")
    print("enhanced.png Generated Successfully!")

except Exception as e:
    print("Error:", e)