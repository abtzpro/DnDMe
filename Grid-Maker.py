from PIL import Image, ImageDraw, ImageFont

# Load the image
img = Image.open("map.jpg")

# Get the image dimensions
width, height = img.size

# Set the grid size
grid_size = 50

# Create a new image with white background
new_img = Image.new("RGB", (width + grid_size, height + grid_size), color="white")

# Paste the original image onto the new image
new_img.paste(img, (grid_size, grid_size))

# Draw the grid
draw = ImageDraw.Draw(new_img)

# Define the font and font size for the grid labels
font = ImageFont.truetype("arial.ttf", 20)

# Draw the letters on the left side of the image
for i in range(height // grid_size):
    draw.text((5, grid_size + i * grid_size + 15), chr(65 + i), font=font, fill="black")

# Draw the numbers at the bottom of the image
for j in range(width // grid_size):
    draw.text((grid_size + j * grid_size + 20, 5), str(j + 1), font=font, fill="black")

# Save the new image
new_img.save("map_with_grid.jpg")
