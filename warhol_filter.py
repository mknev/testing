"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

""" Configure filter settings: """

# Patch must be perfectly square.
PATCH_NAME = 'images/simba-sq.jpg'
N_ROWS = 2
N_COLS = 3
# Recommended value of 2.
MAX_FILTER_STRENGTH = 2
# Enter "None" without quotes for true (pseudo) randomness.
RANDOM_SEED = 'Australia'



""" Do not change below. """

PATCH_SIZE = SimpleImage(PATCH_NAME).width
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
random.seed(RANDOM_SEED)


def main():
	# Generate a blank canvas for the final image.
	final_image = SimpleImage.blank(WIDTH, HEIGHT)
	
	# Fill-in each section of the final image, row-by-row.
	for y_final_image in range(0, HEIGHT, PATCH_SIZE):
		# Fill-in each section of each row of the final image, column-by-column.
		for x_final_image in range(0, WIDTH, PATCH_SIZE):
			final_image = generate_top_left_section(final_image)
			final_image = copy_section(final_image, x_final_image, y_final_image)
	
	# Generate the top-left section again so that it isn't identical to the bottom-right section (avoid fencepost-like error).
	final_image = generate_top_left_section(final_image)
	
	# Display the final image.
	final_image.show()


# Fill-in the top-left section of the final image with a randomly color-tinted patch.
def generate_top_left_section(final_image):
	patch = make_recolored_patch()
	final_image = add_patch_to_final_image(patch, final_image)
	return final_image
	

# Copies the top-left section of the final image to another designated section in the final image (as specified by x_final_image & y_final_image - these variables/co-ordinates correspond to the top-left pixel of each section of the final image).
def copy_section(final_image, x_final_image, y_final_image):
	# For each pixel in the top-left section of the final image:
	for x in range(PATCH_SIZE):
		for y in range(PATCH_SIZE):
			pixel = final_image.get_pixel(x, y)
			
			# Copy the pixel to the same relative position within a different section of the final image.
			final_image.set_pixel((x + x_final_image), (y + y_final_image), pixel)
	
	return final_image
	

# Generate a randomly color-tinted patch.
def make_recolored_patch():
	# Load the patch from the file designated by the user.
	patch = SimpleImage(PATCH_NAME)
	
	# Generate a random color scale/tint for the whole patch.
	red_scale, green_scale, blue_scale = random_scale(), random_scale(), random_scale()
	
	# Multiply the RGB values of each pixel in the patch by the generated scale/tint.
	for pixel in patch:
		pixel.red *= red_scale
		pixel.green *= green_scale
		pixel.blue *= blue_scale

	return patch


# Add the randomly color-tinted patch to the top-left section of the final image.
def add_patch_to_final_image(patch, final_image):
	# For each pixel in the patch:
	for x in range(PATCH_SIZE):
		for y in range(PATCH_SIZE):
			pixel = patch.get_pixel(x, y)
			# Copy the pixel to the same position within the top-left section of the final image.
			final_image.set_pixel(x, y, pixel)
	
	return final_image
	
# Generate a random float between 0 and the maximum filter strength.
def random_scale():
	return random.uniform(0, MAX_FILTER_STRENGTH)
	

if __name__ == '__main__':
    main()