from PIL import Image, ImageDraw, ImageFont
import random

"""
I have found this 'job' from upwork for exercise purpose
It has been asked; 
- Write a python program that will create a frame for a image.
- There will be 3 inputs to create the image. Image must be in png format and 1640x840

And there was an output examples
"""

# Function to create a frame around the image
def create_frame(image, thickness=20):
    width, height = image.size
    frame_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random frame color
    frame_image = Image.new("RGB", (width + 2 * thickness, height + 2 * thickness), frame_color)
    frame_image.paste(image, (thickness, thickness))
    return frame_image


def add_text(image, text_to_add):
    draw = ImageDraw.Draw(image)
    text_color = (255, 255, 255)  # White text color
    font = ImageFont.load_default()  # Use default font
    text_width, text_height = draw.textsize(text_to_add, font=font)
    text_position = ((image.width - text_width) // 2, image.height - text_height - 20)  # Position text at the bottom
    draw.text(text_position, text_to_add, fill=text_color, font=font)
    return image


# Create the photo image
photo_image = Image.open("photo.png")

# Create the frame around the photo
photo_with_frame = create_frame(photo_image)

# Add text to the image
text = "live your life when you still can"
image_with_text = add_text(photo_with_frame, text)

# Resize the image to 1640x840
image_with_text_resized = image_with_text.resize((1640, 840))

# Save the final image as a PNG file
image_with_text_resized.save("output_image.png", format="PNG")

print("Image created successfully!")
