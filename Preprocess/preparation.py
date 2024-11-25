import os
from PIL import Image

folder_path = 'C:\Documents\Sem5\DL\MathSolver\Dataset\MatricesTest2014\)'
target_size = (28, 28)
min_width, min_height = 10, 10


# Function to pad the image to target size
def pad_image(image, target_size):
    width, height = image.size
    new_image = Image.new("L", target_size, color=255)  # 'L' for grayscale, 255 for white padding
    left = (target_size[0] - width) // 2
    top = (target_size[1] - height) // 2
    new_image.paste(image, (left, top))
    return new_image

def prepare(subFolder):
    for filename in os.listdir(subFolder):
        z_counter = 1
        if filename.endswith(".png"):  # Process PNG images
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    
                    # Check if image is below size threshold
                    if width < min_width or height < min_height:
                        new_name = f'z{z_counter}.png'
                        new_path = os.path.join(folder_path, new_name)
                        os.rename(file_path, new_path)
                        z_counter += 1
                        print(f'Renamed {filename} to {new_name} (too small)')
                    
                    elif width != target_size[0] or height != target_size[1]:
                        if width > target_size[0] or height > target_size[1]:
                            # Resize if image is larger than target size
                            img = img.resize(target_size, Image.Resampling.LANCZOS)
                        else:
                            # Pad if the image is smaller than target size
                            img = pad_image(img, target_size)
                        
                        # Save the modified image
                        img.save(file_path)
                        print(f'Resized/padded {filename} to 45x45')
                        
            except Exception as e:
                print(f'Error processing {filename}: {e}')

            break

def main():
    # for folders in os.listdir(folder_path):
    #     sub_folder_path = os.path.join(folder_path, folders)
    #     if os.path.isdir(sub_folder_path):
    #         print(sub_folder_path)
            # for subFolders in os.listdir(folders):
    prepare(folder_path)
        # break

if __name__ == '__main__':
    main()