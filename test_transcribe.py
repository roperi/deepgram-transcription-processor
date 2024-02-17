# Copyright 2024 roperi. All Rights Reserved.

import unittest
from unittest.mock import patch
import os
import json
from transcribe import main, process_transcript


class TestTranscribeProgram(unittest.TestCase):
    @patch('transcribe.DeepgramClient')
    def test_main_with_local_file(self, mock_client):
        # Mock DeepgramClient instance and its methods
        mock_deepgram_instance = mock_client.return_value
        mock_deepgram_instance.listen.prerecorded.v.return_value.transcribe_file.return_value.to_dict.return_value = {
            "results": {
                "summary": {"short": "Test summary"},
                "channels": [{"alternatives": [{"paragraphs": {"transcript": "Test transcript"}}]}],
                "topics": {"segments": [{"topics": [{"topic": "Test topic"}]}]}
            }
        }

        # Call main function with a local file
        input_path = 'test_audio.wav'
        project_name = 'test_project'
        main(input_path, False, project_name)

        # Assert that transcription JSON and related files are created
        self.assertTrue(os.path.exists(f'output/{project_name}__transcription.json'))
        self.assertTrue(os.path.exists(f'output/{project_name}__summary.txt'))
        self.assertTrue(os.path.exists(f'output/{project_name}__paragraphs.txt'))
        self.assertTrue(os.path.exists(f'output/{project_name}__topics.txt'))

    @patch('transcribe.DeepgramClient')
    def test_main_with_url(self, mock_client):
        # Mock DeepgramClient instance and its methods
        mock_deepgram_instance = mock_client.return_value
        mock_deepgram_instance.listen.prerecorded.v.return_value.transcribe_url.return_value.to_dict.return_value = {
            "results": {
                "summary": {"short": "Test summary"},
                "channels": [{"alternatives": [{"paragraphs": {"transcript": "Test transcript"}}]}],
                "topics": {"segments": [{"topics": [{"topic": "Test topic"}]}]}
            }
        }

        # Call main function with a URL
        input_url = 'http://example.com/audio.mp3'
        project_name = 'test_project'
        main(input_url, True, project_name)

        # Assert that transcription JSON and related files are created
        self.assertTrue(os.path.exists(f'output/{project_name}__transcription.json'))
        self.assertTrue(os.path.exists(f'output/{project_name}__summary.txt'))
        self.assertTrue(os.path.exists(f'output/{project_name}__paragraphs.txt'))
        self.assertTrue(os.path.exists(f'output/{project_name}__topics.txt'))

    def test_process_transcript(self):
        # Create a temporary JSON file with some content
        test_data = {
            "results": {
                "summary": {"short": "Test summary"},
                "channels": [{"alternatives": [{"paragraphs": {"transcript": "Test transcript"}}]}],
                "topics": {"segments": [{"topics": [{"topic": "Test topic"}]}]}
            }
        }
        with open('test_transcription.json', 'w') as f:
            json.dump(test_data, f)

        # Call process_transcript function with the temporary JSON file
        project_name = 'test_project'
        process_transcript('test_transcription.json', project_name)

        # Assert that output files are created
        self.assertTrue(os.path.exists(f'output/{project_name}__summary.txt'))
        self.assertTrue(os.path.exists(f'output/{project_name}__paragraphs.txt'))
        self.assertTrue(os.path.exists(f'output/{project_name}__topics.txt'))

        # Clean up temporary file
        os.unlink('test_transcription.json')


if __name__ == '__main__':
    unittest.main()
