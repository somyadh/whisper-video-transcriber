import os
import subprocess
import whisper
import json
import argparse

def extract_audio(video_path, audio_directory):
    audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".wav"
    audio_path = os.path.join(audio_directory, audio_filename)
    audio_exists = os.path.exists(audio_path)

    if not audio_exists:
        # Use FFmpeg to extract audio from the video
        subprocess.call(['ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', audio_path])

    return audio_path

def transcribe_audio(model, audio_path, transcription_directory):
    # Get the base name of the audio file
    base_name = os.path.splitext(os.path.basename(audio_path))[0]

    transcription_filename = base_name + ".txt"
    transcription_path = os.path.join(transcription_directory, transcription_filename)
    transcript_exists = os.path.exists(transcription_path)

    print("Transcription path created:", transcription_path)

    if transcript_exists:
        print("Transcription already exists. Skipping...")
        return transcription_path

    result_directory = os.path.join(transcription_directory, "segments")
    os.makedirs(result_directory, exist_ok=True)

    result_filename = base_name + "_segments.txt"
    result_path = os.path.join(result_directory, result_filename)

    result = model.transcribe(audio_path)

    #to filter out specifc keys of segment data while storing
    # segments_data = []
    # for segment in result["segments"]:
    #     segment_data = {key: segment[key] for key in ['start', 'end', 'text']}
    #     segments_data.append(segment_data)

    # Write the transcription to a text file
    with open(transcription_path, 'w') as file:
        file.write(result["text"])

    with open(result_path, 'w') as fp:
        json.dump(result["segments"], fp)

    return transcription_path

def process_videos(model, video_directory, audio_directory, transcription_directory):
    video_files = [file for file in os.listdir(video_directory) if file.endswith((".mp4", ".avi", ".mov"))]
    total_videos = len(video_files)
    transcription_paths = []

    for index, video_file in enumerate(video_files, start=1):
        print(f"Starting transcription for video {index}/{total_videos}: {video_file}")
        video_path = os.path.join(video_directory, video_file)
        audio_path = extract_audio(video_path, audio_directory)
        transcription_path = transcribe_audio(model, audio_path, transcription_directory)
        transcription_paths.append(transcription_path)

    return transcription_paths

def main():
    parser = argparse.ArgumentParser(description="Video Transcription Tool")
    parser.add_argument("--video_dir", required=True, help="Directory containing video files")
    parser.add_argument("--audio_dir", required=True, help="Directory to store extracted audio files")
    parser.add_argument("--transcription_dir", required=True, help="Directory to store transcriptions")
    parser.add_argument("--model", default="tiny", help="Whisper model to use for transcription (default: tiny)")

    args = parser.parse_args()

    video_directory = args.video_dir
    audio_directory = args.audio_dir
    transcription_directory = args.transcription_dir
    model_name = args.model

    # Create directories if they don't exist
    os.makedirs(audio_directory, exist_ok=True)
    os.makedirs(transcription_directory, exist_ok=True)

    # Load the Whisper model
    model = whisper.load_model(model_name)

    # Extract audio and transcribe videos
    transcriptions = process_videos(model, video_directory, audio_directory, transcription_directory)

    # Print the transcription paths
    print("\nTranscription Results:")
    for i, transcription in enumerate(transcriptions):
        print(f"Transcription {i+1}: {transcription}")

if __name__ == "__main__":
    main()