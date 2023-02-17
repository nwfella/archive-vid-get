import youtube_dl

# Get archive.org video URL from user
url = input("Enter Archive.org video URL: ")

# Set youtube_dl options
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nooverwrites': True,
    'continuedl': True,
    'retries': 10,
    'buffer_size': '16M',
}

# Download video using youtube_dl
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
