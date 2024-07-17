import yt_dlp

def download_youtube_video(video_url, output_path, filename):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/{filename}.%(ext)s',
        'merge_output_format': 'mp4',  # Asegura que el video y el audio se fusionen en un archivo mp4
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Asegura que la salida sea en formato mp4
        }],
        'postprocessor_args': [
            '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental'
        ],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Descarga completa!")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=w2p0hE8hsQY'
output_path = './SEBA'
filename = 'DIA1'

download_youtube_video(video_url, output_path, filename)

