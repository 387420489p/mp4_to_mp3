import os
import subprocess
import shutil
import multiprocessing
import time

# Define the root directory to start the search from
root_dir = os.getcwd()

# Define the number of processes to use
num_processes = multiprocessing.cpu_count()

# Define the conversion function
def convert_folder(root):
    # Walk through all the directories and files under the current directory
    for subdir, _, files in os.walk(root):
        # Check if there is an mp4 file in the current directory
        if any(file.endswith('.mp4') for file in files):
            # Get the name of the current directory
            current_dir = os.path.basename(subdir)
            # Define the output directory for the converted mp3 file
            output_dir = os.path.dirname(subdir)
            # Define the output file name for the converted mp3 file
            output_file = f'{current_dir}.mp3'
            # Define the full paths for the input mp4 file and output mp3 file
            input_file = os.path.join(subdir, [file for file in files if file.endswith('.mp4')][0])
            output_file = os.path.join(output_dir, output_file)
            # Use FFmpeg to convert the mp4 file to mp3 with the best quality and overwrite the output file if it already exists
            subprocess.run(['ffmpeg', '-y', '-i', input_file, '-q:a', '0', '-map', 'a', output_file])
            # Remove the original directory and its contents
            shutil.rmtree(subdir)

# Record the start time
start_time = time.time()

# Create a pool of worker processes
with multiprocessing.Pool(processes=num_processes) as pool:
    # Walk through all the directories under the root directory and apply the conversion function in parallel
    pool.map(convert_folder, [os.path.join(root_dir, subdir) for subdir in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, subdir)) and os.path.join(root_dir, subdir) != root_dir])

# Record the end time
end_time = time.time()

# Count the number of converted and deleted files
num_converted_files = sum(len(files) for _, _, files in os.walk(root_dir) if any(file.endswith('.mp3') for file in files))
num_deleted_files = sum(len(dirs) for _, dirs, _ in os.walk(root_dir) if any(os.path.join(root_dir, d) != root_dir for d in dirs))

# Print the total run time, number of converted files, and number of deleted files
print(f'Total run time: {end_time - start_time:.2f} seconds')
print(f'Number of converted files: {num_converted_files}')
print(f'Number of deleted files: {num_deleted_files}')
