from PIL import Image 
import os  

# Define input and output folders
input_Folder = "C:/Users/borre/Downloads/FOTO"
output_Folder = "C:/Users/borre/Downloads/New folder"

# Create output folder if it dont exist
os.makedirs(output_Folder, exist_ok=True)

# Loop through all files in the input folder
for file_name in os.listdir(input_Folder):
    # Check if the file is a JPG or JPEG
    if file_name.endswith(".jpg") or file_name.endswith("jpeg"):
        # Open the image file
        img = Image.open(os.path.join(input_Folder,file_name))
        
        # Get the filename without extension
        base_name = os.path.splitext(file_name)[0]
        
        # Save the image as PNG in the output folder
        # The new filename will be the original name but with .png extension
        img.save(os.path.join(output_Folder , base_name + ".png"), "PNG")
