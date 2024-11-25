import os

# Note this is for png files. Change it accordingly for other files
directory = 'C:\Documents\Sem5\DL\MathSolver\Dataset\MatricesTest2014'

# Example of renaming files with a prefix or suffix
def rename_files_with_prefix(directory, prefix='subr'):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            # Create the new file name
            new_filename = prefix + filename
            new_path = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Example of renaming files with numbering
def rename_files_with_numbering(directory, start_number=1):
    files = os.listdir(directory)
    for count, filename in enumerate(files, start=start_number):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path) and old_path.endswith('.png'):
            # Create the new file name with numbering
            new_filename = f'{count}.png'
            new_path = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_path, new_path)
            # print(f'Renamed: {filename} -> {new_filename}')
        else:
            print(old_path)

if __name__ ==  '__main__':
    # Rename files with a prefix
    # rename_files_with_prefix(directory, prefix='new_')

    # Rename files with numbering
    for subFolder in os.listdir(directory):
        sub_folder_path = os.path.join(directory, subFolder)
        if os.path.isdir(sub_folder_path):
            print(sub_folder_path)
            rename_files_with_numbering(sub_folder_path)
            # break
        else:
            print(subFolder)
    # rename_files_with_numbering()
