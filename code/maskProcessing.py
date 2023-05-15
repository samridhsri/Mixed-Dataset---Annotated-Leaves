import os
import cv2

# Folder path containing the masks
mask_folder = './resized_imagesAndMasks/masks-resized'

# Output folder for saving the preprocessed masks
output_folder = './resized_imagesAndMasks/preprocessed_masks'

# Threshold value for converting to binary format
threshold = 127

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over the masks in the folder
for mask_filename in os.listdir(mask_folder):
    # Load the mask image
    mask_path = os.path.join(mask_folder, mask_filename)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # Apply thresholding to convert to binary format
    _, binary_mask = cv2.threshold(mask, threshold, 255, cv2.THRESH_BINARY)

    # Invert the binary mask if needed
    binary_mask = cv2.bitwise_not(binary_mask)

    # Save the preprocessed mask
    output_path = os.path.join(output_folder, mask_filename)
    cv2.imwrite(output_path, binary_mask)
