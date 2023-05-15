from PIL import Image
import os

print(os.getcwd())
# Set the path of the folder containing the images to be resized
image_folder = './resized_imagesAndMasks/'

# Set the path of the folder where the resized images will be saved
output_folder = './resized_imagesAndMasks/ResizedImages/'

# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Set the desired size of the resized images
new_size = (256, 256) # Change this to your desired size
files = []
# Loop through all the files in the image folder
for filename in os.listdir(image_folder):
    # Check if the file is an image file
    if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.jpeg') or filename.endswith('.png'):
        
        # files.append(filename)
        # Open the image using Pillow
        image = Image.open(os.path.join(image_folder, filename))
        # Resize the image
        resized_image = image.resize(new_size)
        # Save the resized image to the output folder
        resized_image.save(os.path.join(output_folder, filename))

# print(len(files))
