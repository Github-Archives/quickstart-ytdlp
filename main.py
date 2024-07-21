import yt_dlp

# URL of the YouTube video to download
video_url = 'https://www.youtube.com/watch?v=7PIji8OubXU'

# Options for yt-dlp
ydl_opts = {
    'format': 'best',  # Download the best quality available
    'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save to the 'downloads' folder with title as filename or creates local dir if none exists
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
