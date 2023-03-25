import os
import sys
from pytube import YouTube

# Get the folder name from the command line argument
folder_name = sys.argv[1]

# Create the folder if it doesn't exist
try:
    os.makedirs(folder_name)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# Open the file containing the list of URLs
with open("url_list.txt", "r") as f:
    # Read the URLs into a list
    url_list = f.read().splitlines()

# Loop through each URL in the list and download the audio to the folder
for url in url_list:
    # Create a YouTube object from the URL
    yt = YouTube(url)

    # Get the first audio stream from the YouTube video
    audio = yt.streams.filter(only_audio=True).first()

    # Replace any invalid characters in the video title with underscores
    video_title = yt.title.replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_")

    # Download the audio stream to the folder with the video title as the file name
    try:
        audio.download(output_path=folder_name, filename=video_title + ".mp3")
    except OSError as e:
        print(f"Error downloading {video_title}: {e}")
