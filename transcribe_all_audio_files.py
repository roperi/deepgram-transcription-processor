# Copyright 2024 roperi. All Rights Reserved.

import os
import subprocess
import concurrent.futures
import shlex
import multiprocessing
import argparse


def transcribe_audio(file_path, project_name):
    """
    Transcribes a single audio file.

    Args:
        file_path (str): Path to the audio file.
        project_name (str): Name of the transcription project.
    """
    # Escape special characters in project name
    escaped_project_name = shlex.quote(project_name)

    # Remove unnecessary single quotes added by shlex.quote()
    escaped_project_name = escaped_project_name.strip("'")

    # Build the command to transcribe the file
    command = f'python transcribe.py -n "{escaped_project_name}" -i "{file_path}"'

    # Execute the command using subprocess
    subprocess.run(command, shell=True)


def transcribe_all_audio(folder_path):
    """
    Transcribes all audio files in a folder concurrently.

    Args:
        folder_path (str): Path to the folder containing the audio files.
    """
    # List all files in the folder
    file_list = os.listdir(folder_path)

    # Determine the number of CPU cores
    num_cores = multiprocessing.cpu_count()
    # Determine the number of workers based on the number of CPU cores
    max_workers = min(5, num_cores)  # Set a maximum of 5 workers or the number of CPU cores, whichever is smaller

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit transcription tasks for each audio file
        futures = [executor.submit(transcribe_audio, os.path.join(folder_path, file_name), os.path.splitext(file_name)[0]) for file_name in file_list]

        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")


def main():
    """
    Main function to parse command-line arguments and execute the transcription process.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Transcribe all audio files in a folder concurrently.')
    parser.add_argument('-i', '--input', metavar='folder_path', type=str, required=True,
                        help='Path to the folder containing the audio files')
    args = parser.parse_args()

    # Transcribe all audio files in the specified folder
    transcribe_all_audio(args.input)


if __name__ == '__main__':
    main()
