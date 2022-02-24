from pytube import YouTube
import os

video_link = input("Video Link: ")

try:
    video = YouTube(video_link)

    audio = video.streams.filter(only_audio=True).first()

    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or "."

    out_file = audio.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print('Download Completed!')

except:
    print("Connection Error")  # to handle exception
