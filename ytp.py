import os
import pytube

def on_progress(stream, chunk, remaining):
    """
    Show the download progress as a percentage.
    """
    downloaded = stream.filesize - remaining
    percent = (downloaded / stream.filesize) * 100
    print(f"Downloading... {percent:.2f}% complete")

def download(url):
    """
    Download the audio from a YouTube video using PyTube and return the filename.
    """
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    filename = stream.default_filename[:-4] + ".mp3"
    os.rename(stream.default_filename, filename)
    return filename

def download_playlist(playlist_url):
    """
    Download all videos in a playlist and save as mp3.
    """
    playlist = pytube.Playlist(playlist_url)
    for url in playlist.video_urls:
        download(url)

if __name__ == "__main__":
    playlist_url = input("Enter the URL of a YouTube playlist: ")
    download_playlist(playlist_url)
    print("Download complete.")
    print(" /\\_/\\ ")
    print("( o o )")
    print(" > ^ < ")
