# Video Transcription Tool

This is a command-line tool for transcribing video files using the OpenAI Whisper library. It extracts the audio from the video files, transcribes the audio using the specified Whisper model, and saves the transcriptions along with the timing information.

## Features

- Extracts audio from video files locally on your machine
- Transcribes the extracted audio using the Whisper library.
- Supports various Whisper models for transcription (e.g., tiny, base,small, medium, large)
- Saves the transcriptions as text files
- Saves the timing information of each transcribed segment as JSON files
- Provides progress updates during the transcription process

## Requirements

- Python 3.6 or higher
- FFmpeg (installed and accessible from the command line)
- OpenAI - Whisper library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/video-transcription-tool.git
   ```

2. Navigate to the project directory:
   ```
   cd video-transcription-tool
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Make sure FFmpeg is installed and accessible from the command line. You can download FFmpeg from the official website: [https://ffmpeg.org](https://ffmpeg.org)

## Usage

To transcribe video files, use the following command:

```
python transcribe.py --video_dir /path/to/video/directory --audio_dir /path/to/audio/directory --transcription_dir /path/to/transcription/directory [--model model_name]
```

- `--video_dir`: Directory containing the video files to be transcribed (required).
- `--audio_dir`: Directory where the extracted audio files will be stored (required).
- `--transcription_dir`: Directory where the transcriptions and timing information will be saved (required).
- `--model`: Whisper model to use for transcription (optional, default: "tiny"). Available models: "tiny", "base", "small", "medium", "large".

Example:
```
python transcribe.py --video_dir /path/to/videos --audio_dir /path/to/audio --transcription_dir /path/to/transcriptions --model small
```

## Output

The tool will generate the following output files:

- Transcriptions: The transcriptions will be saved as text files in the specified `transcription_dir` directory. Each transcription file will have the same name as the corresponding video file, with the ".txt" extension.

- Segment Information: The segment information for each video file will be saved as JSON files in the "segments" subdirectory within the `transcription_dir` directory. 

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Whisper library: [https://github.com/openai/whisper](https://github.com/openai/whisper)
- FFmpeg: [https://ffmpeg.org](https://ffmpeg.org)

