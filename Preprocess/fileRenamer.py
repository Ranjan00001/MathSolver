import os

# Rename files with numbering
def rename_files_with_numbering(directory, start_number=1):
    files = os.listdir(directory)
    print(f"Entering directory: {directory}, Found files: {files}")  # Log entry and files found
    
    for count, filename in enumerate(files, start=start_number):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            # Extract file extension
            file_extension = os.path.splitext(filename)[1]
            # Create the new file name with numbering and original extension
            new_filename = f'{count}{file_extension}'
            new_path = os.path.join(directory, new_filename)
            
            # Check if the target file already exists
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")  # Print renamed files
            else:
                print(f"Skipped renaming (already exists): {new_path}")

# Recursively process all subdirectories
def process_all_subdirectories(directory):
    print(f"Entering directory: {directory}")
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            # Recur for nested subdirectories
            process_all_subdirectories(path)
        else:
            rename_files_with_numbering(directory)

# Main execution
if __name__ == '__main__':
    directory = r'C:\Users\Deependra\Documents\SEM5\DeepLearning\Cnn\cv project\MathSolver\Dataset\MatricesTest2014'
    process_all_subdirectories(directory)
