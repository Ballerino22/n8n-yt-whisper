import os
import sys
import subprocess

def download_audio(url):
    print(f"Downloading from: {url}")
    output_path = "/app/audio.mp3"
    command = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "-o", output_path,
        url
    ]
    subprocess.run(command)
    print(f"Download complete: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download.py <youtube_url>")
    else:
        download_audio(sys.argv[1])
