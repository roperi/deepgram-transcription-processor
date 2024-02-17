# Deepgram Transcription Processor

This Python program is designed to process transcription output obtained from Deepgram's transcription service. It extracts key information such as topics, summary, and paragraphs from the transcription output JSON and writes them to separate text files for further analysis and reference.

## Features

- Extracts topics from the transcription output and writes them to a text file.
- Extracts summary information from the transcription output and writes it to a separate text file.
- Extracts paragraphs from the transcription output and writes them to another text file.

## Requirements

- Python 3.x
- Deepgram API access
- JSON transcription output from Deepgram


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
1. **Create output folder:** Create an output folder to save the topics, summary and paragraphs. The `output` dir is hardcoded in the code so make sure to create it:
   ```bash
   mkdir output/
   ```

2. **Run the Program:** Once your API key is set up, you can run the program with the following command:

    ```bash
    python transcribe.py [-h] --name NAME [--url] input

    ```

    - Replace `input_path` with the path to the audio file or URL you want to process.
    - Optionally, use the `--url` flag if the input is a URL instead of a local audio file.

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

4. **Review Test Results**: After running the tests, review the output to ensure that all tests passed successfully.

    ```
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK
    ```

If any tests fail, review the error messages to identify the issues and make any necessary corrections to the code.



## Logging Configuration

This project utilizes Python's logging module to provide detailed information about the program's execution. The logging level can be adjusted to control the verbosity of the logs. 

### Configuration

The logging configuration is stored separately from the main codebase to allow for easy customization without altering the source files. The logging configuration can be found in the `config.py` file, which is included in the `.gitignore` to prevent sensitive information from being exposed in version control.

```python
# config.py

from deepgram import DeepgramClientOptions
import logging

# Configure logging settings
config = DeepgramClientOptions(
    verbose=logging.SPAM,
    # Add other logging parameters as needed
)
```

## Copyright and License
Copyright 2023 Deepgram SDK contributors.

Copyright 2024 roperi. 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
