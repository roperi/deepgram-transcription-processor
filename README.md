# Deepgram Transcription Processor

This Python program is designed to process transcription output obtained from Deepgram's transcription service. It extracts key information such as topics, summary, and paragraphs from the transcription output JSON and writes them to separate text files for further analysis and reference.

## Features

- Extracts topics from the transcription output and writes them to a text file.
- Extracts summary information from the transcription output and writes it to a separate text file.
- Extracts paragraphs from the transcription output and writes them to another text file.

## Requirements

- Python 3.x
- Deepgram API acces. You can signup for free and get $200 in credits! (as of February 2024)


## Tested Environment

This program has been tested and verified to work correctly in Python 3.10 Debian 10. While it may work in other versions of Python 3, we recommend using Python 3.10 for optimal compatibility and performance.


## Installation


1. **Create Virtual Environment:** It's recommended to create a virtual environment to isolate the dependencies of this project. You can create a virtual environment with Python 3.10 using the following command:

    ```bash
    python3.10 -m venv venv
    ```

    This command will create a virtual environment named `venv` in the current directory.

2. **Activate Virtual Environment:** After creating the virtual environment, activate it using the appropriate command for your operating system:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```
      
3. **Clone the repository:**
   
    ```
    git clone https://github.com/roperi/deepgram-transcription-processor.git
    ```

4. **Navigate to the project directory:**
   
    ```
    cd deepgram-transcription-processor
    ```

5. **Install the required dependencies:**
   
    ```
    pip install -r requirements.txt
    ```

## Setup Deepgram API Key


**Free credit when signing up**

As of February 2024 new accounts get $200 in credit (up to 45,000 minutes), absolutely free. No credit card needed. This is more than enough for playing around with their API! 

**Get API key**

Before using this program, you need to obtain an API key from Deepgram's transcription service. Follow these steps to set up your API key:

1. **Sign Up/Login to Deepgram:** If you haven't already, sign up for a Deepgram account or log in to your existing account [here](https://www.deepgram.com/).

2. **Obtain API Key:** Once logged in, navigate to your account settings or API dashboard to obtain your API key.

3. **Create .env File:** Create a file named `.env` in the root directory of this project.

4. **Set API Key in .env:** Open the `.env` file and add the following line, replacing `YOUR_API_KEY` with your actual API key:

    ```
    DG_API_KEY=YOUR_API_KEY
    ```

    Save the `.env` file.

## Usage
1. **Run the Program:** Once your API key is set up, you can run the program with the following command:

    ```bash
    python transcribe.py [-h] --name NAME [--input INPUT]

    ```
    - Replace `name` with the name of your project.
    - Replace `input` with the path to the audio file or URL you want to process.

Output will be saved in the output folder.

Example with a URL:

```
python transcribe.py --name "Awesome podcast - Episode 1" --input https://example.com/audio.wav
```

Example with a mp3 file:

```
python transcribe.py -n "Customer service conversation" -i input/conversation.mp3
```

### Output 

After executing the command you should check in the output folder for all the processed files.  

```commandline
output/Customer service conversation__transcription.json
output/Customer service conversation__paragraphs.txt
output/Customer service conversation__summary.txt
output/Customer service conversation__topics.txt
```

## Running Unit Tests

To run the unit tests for this project, follow these steps:

1. **Clone the Repository**: Clone the project repository to your local machine using Git:

    ```
    git clone git clone https://github.com/roperi/deepgram-transcription-processor.git
    ```

2. **Navigate to the Tests Directory**: Open a terminal or command prompt, and change into the directory containing the unit test scripts:

    ```
    cd deepgram-transcription-processor/
    ```

3. **Run the Tests**: Execute the test script using the Python interpreter:

    ```
    python test_transcribe.py
    ```

4. **Review Test Results**: After running the tests, review the output to ensure that all tests passed successfully. There is an empty audio file incliuded for testing purposes.

    ```
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK
    ```

If any tests fail, review the error messages to identify the issues and make any necessary corrections to the code.


## Transcribing Audio Files in a Folder

The `transcribe_all_audio_files.py` script allows you to transcribe all audio files in a specified folder concurrently. To use this functionality, follow these steps:

1. **Specify Folder Path**: Use the `-i` or `--input` option to specify the path to the folder containing the audio files.

    ```bash
    python transcribe_all_audio_files.py -i /path/to/your/folder
    ```

2. **Transcription Process**: The script will transcribe all audio files in the specified folder concurrently using multiple subprocesses, optimizing resource utilization and reducing transcription time.

3. **Output**: The transcription results for each audio file will be saved to the specified output directory.

This functionality is useful when you have a large number of audio files to transcribe and want to process them in parallel to expedite the transcription process.


## Configuration

### Logging

Create a `config.py` in the project folder and paste the following:

```python
# config.py

from deepgram import DeepgramClientOptions
import logging

# Configure logging settings
config = DeepgramClientOptions(
    verbose=logging.SPAM,
    # Add other logging parameters as needed
)

# Define the timeout value in seconds
TIMEOUT_SECONDS = 600.0 # = 10 minutes
```

With this file you could control logging and timeout (especially if you get `write operation timed out` errors)


## Copyright and License
Copyright 2023 Deepgram SDK contributors.

Copyright 2024 roperi. 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
