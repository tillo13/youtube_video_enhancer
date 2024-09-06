import yt_dlp

def get_best_format(formats):
    best_format = None
    best_resolution = 0
    
    for fmt in formats:
        # Ensure the height is an integer and not None
        height = fmt.get('height')
        if height is not None and isinstance(height, int):
            if height > best_resolution:
                best_resolution = height
                best_format = fmt
    
    return best_format

def download_best_resolution(url):
    try:
        # List the formats to find the best resolution
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'video')
            print(f"Title: {video_title}")
            
            formats = info_dict.get('formats', [])
            best_format = get_best_format(formats)
            if not best_format:
                print("No suitable format found.")
                return
            
            print(f"Best format: ID={best_format['format_id']}, Resolution={best_format.get('height')}p, Extension={best_format['ext']}")
            
            # Download the best format
            ydl_opts = {
                'format': best_format['format_id'],
                'outtmpl': './downloaded_video.mp4'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print('Download completed successfully.')
    
    except yt_dlp.utils.DownloadError as e:
        print(f"Download Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# The URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=u1e4rpY7syM'
download_best_resolution(video_url)