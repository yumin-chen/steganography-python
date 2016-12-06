import cv2 # OpenCV 2

# Create a hidden message
def hidden_message():
    msg = "This is the hidden message......" * 10000
    for c in (msg):
        o = ord(c)
        for i in range(8):
            yield (o & (1 << i)) >> i

hiddenMessage = hidden_message()

# Read the original image
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
for h in range(len(img)):
    for w in range(len(img[0])):
        # Write the hidden message into the least significant bit
        img[h][w] = (img[h][w] & ~1) | next(hiddenMessage)
# Write out the image with hidden message
cv2.imwrite("img_grayscale.bmp", img)
