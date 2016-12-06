import cv2 # OpenCV 2

def to_bit_generator(msg):
    """Converts a message into a generator which returns 1 bit of the message
    each time."""
    for c in (msg):
        o = ord(c)
        for i in range(8):
            yield (o & (1 << i)) >> i

def main():
    # Create a generator for the hidden message
    hidden_message = to_bit_generator(open("README.md", "r").read() * 10)
    
    # Read the original image
    img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
    for h in range(len(img)):
        for w in range(len(img[0])):
            # Write the hidden message into the least significant bit
            img[h][w] = (img[h][w] & ~1) | next(hidden_message)
    # Write out the image with hidden message
    cv2.imwrite("img_grayscale.bmp", img)

if __name__ == "__main__":
	main()
