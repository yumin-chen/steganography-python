import cv2 # OpenCV 2

# Read the image and try to restore the message
img = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)
i = 0
bits = ''
chars = []
for row in img:
    for pixel in row:
        bits = str(pixel & 0x01) + bits
        i += 1
        if(i == 8):
            chars.append(chr(int(bits, 2)))
            i = 0
            bits = ''
print(''.join(chars))
