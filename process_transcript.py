# Copyright 2024 roperi. All Rights Reserved.

import httpx
import argparse
import os
from datetime import datetime
import json
import logging, verboselogs
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    PrerecordedOptions,
    FileSource,
)
from config import config


# Load credentials
load_dotenv()
DG_API_KEY = os.getenv("DG_API_KEY")
TAG = 'SPEAKER '


# Function

def main(input_path, is_url):
    """
    Process audio files or URLs.

    Parameters:
        input_path (str): Path to the input audio file or URL.
        is_url (bool): Flag to specify whether the input is a URL.
    """
    try:
        print('Initialising...')
        deepgram = DeepgramClient(DG_API_KEY, config)

        # Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            diarize=True,
            summarize="v2",
            topics=True,
        )

        timeout = httpx.Timeout(300.0, connect=10.0)

        print(f'Transcribing {input_path}')
        if is_url:
            AUDIO_URL = {
                'url': input_path
            }

            # Input is a URL
            response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options, timeout=timeout)
            base_name = f"url_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        else:
            # Input is a local file
            with open(input_path, "rb") as file:
                buffer_data = file.read()
            payload = {
                "buffer": buffer_data,
            }
            response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options, timeout=timeout)
            base_name = os.path.splitext(os.path.basename(input_path))[0]

        response_dict = response.to_dict()
        print('Saving transcription...')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if is_url:
            output_filename = f"transcription_url_{timestamp}.json"
            output_filename_txt = f"url_{timestamp}.txt"
        else:
            base_filename = os.path.splitext(os.path.basename(input_path))[0]
            output_filename = f"transcription_{base_filename}_{timestamp}.json"
            output_filename_txt = f"{base_name}_{timestamp}.txt"

        output_json = os.path.join('output', output_filename)
        with open(output_json, "w") as json_file:
            json.dump(response_dict, json_file, indent=4)

        # Process transcript text file
        print('Getting diarize and summary from transcript...')
        process_transcript(output_json, output_filename_txt)

    except Exception as e:
        print(f"Exception: {e}")


def process_transcript(output_json, output_transcript):
    """
    Process a transcript from the JSON output of Deepgram's transcription.

    Parameters:
        output_json (str): Path to the JSON file containing the transcription output.
        output_transcript (str): Path to the output text file to save the transcript.
    """
    summary_lines = []

    with open(output_json, "r") as file:
        data = json.load(file)

    # Extract summary from JSON
    summary = data.get("results", {}).get("summary", {}).get("short", "")
    summary_lines.append(summary)

    # Write summary to file
    with open(os.path.join('output', f'summary_{output_transcript}'), 'w') as f_summary:
        for line in summary_lines:
            f_summary.write(line.strip() + '\n')

    # Extract paragraphs from JSON
    paragraphs_transcript = data.get('results', {}).get('channels', [{}])[0].get('alternatives', [{}])[0].get(
        'paragraphs', {}).get('transcript', "")

    # Write paragraphs to file
    with open(os.path.join('output', f'paragraphs_{output_transcript}'), 'w') as f_paragraphs:
        f_paragraphs.write(paragraphs_transcript)

    # Extract topics from JSON
    topics_segments = data.get("results", {}).get("topics", {}).get("segments", [])
    topic_values = []
    for segment in topics_segments:
        topics = segment.get("topics", [])
        for topic_info in topics:
            topic_value = topic_info.get("topic", "")
            topic_values.append(topic_value)

    # Write topics to file
    with open(os.path.join('output', f'topics_{output_transcript}'), 'w') as f_topics:
        for topic in topic_values:
            f_topics.write(topic.strip() + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process transcripts from audio files or URLs.')
    parser.add_argument('--url', '-u', action='store_true', help='Flag to specify input as a URL.')
    parser.add_argument('input', nargs=1, help='Path to audio file or URL.')
    args = parser.parse_args()

    if args.url:
        input_path = args.input[0]
        is_url = True
    else:
        input_path = args.input[0]
        is_url = False

    main(input_path, is_url)
