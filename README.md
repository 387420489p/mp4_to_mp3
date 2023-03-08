### MP4 to MP3 Converter
## Description
This Python script converts all mp4 files in subdirectories of the current working directory to mp3 files using FFmpeg. It also deletes the original mp4 files and their parent directories once the conversion is complete.

## Requirements
FFmpeg (https://ffmpeg.org/)
## Usage
1. Place the script in the directory containing the subdirectories with the mp4 files you want to convert.
2. Install FFmpeg if you haven't already.
3. Run the script using a Python interpreter.
## Notes
- The script uses multiprocessing to convert the mp4 files in parallel, with the number of processes set to the number of available CPU cores.
- The script converts the mp4 files to mp3 with the best quality and overwrites the output file if it already exists.
- The script deletes the original mp4 files and their parent directories after the conversion is complete.
- The script prints the total run time, number of converted files, and number of deleted files once the conversion is complete.
