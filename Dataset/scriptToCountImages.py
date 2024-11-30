import os
import csv
from PIL import Image

def count_images_in_folders(base_folder, output_csv):
    # Check if the base folder exists
    if not os.path.exists(base_folder):
        print(f"The folder '{base_folder}' does not exist.")
        return

    # Dictionary to store folder names and image counts
    folder_image_counts = {}

    # Iterate through each folder in the base directory
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        
        if os.path.isdir(folder_path):
            image_count = 0

            # Iterate through files in the current folder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                # Check if the file is an image
                try:
                    with Image.open(file_path):
                        image_count += 1
                except:
                    continue

            # Store the count in the dictionary
            folder_image_counts[folder_name] = image_count

    # Write results to a CSV file
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Folder Name", "Image Count"])
        for folder, count in folder_image_counts.items():
            writer.writerow([folder, count])

    print(f"Results have been written to '{output_csv}'")

# Specify the base folder path and output CSV file path
base_folder = "MatricesTest2014"
output_csv = "image_counts.csv"
count_images_in_folders(base_folder, output_csv)