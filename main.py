from PIL import Image, ImageOps

# Open the image file
with Image.open('input_image.jpg') as image:
    # Define the desired square size (assuming 1920x1920)
    square_size = 1920

    # Calculate the width and height difference
    width_diff = square_size - image.width
    height_diff = square_size - image.height

    # Calculate padding values for left, top, right, and bottom
    left_padding = width_diff // 2
    top_padding = height_diff // 2
    right_padding = width_diff - left_padding
    bottom_padding = height_diff - top_padding

    # Add white borders to the sides
    square_image = ImageOps.expand(image, border=(left_padding, top_padding, right_padding, bottom_padding),
                                   fill='white')

    # Save the square image
    square_image.save("output_image.jpg")
