from PIL import Image

# Prompt user for access to image gallery and gain permissions

# Load the bitmap image
img = Image.open("path/to/image.bmp")

# Convert image to grayscale
img_gray = img.convert('L')

# Resize the image to fit a D&D map
img_resized = img_gray.resize((1000, 1000))

# Save the resized image as a new bitmap file
img_resized.save("path/to/d&d_map.bmp")
