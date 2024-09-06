from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(video_file, out_file, start_time, end_time):
    """
    Cut out section from a video file and write it to another file.
    Args:
        video_file (str): Video file path.
        out_file (str): Output video file path.
        start_time (int, float): Start time in seconds.
        end_time (int, float): End time in seconds.
    """
    ffmpeg_extract_subclip(video_file, start_time, end_time, targetname=out_file)

# call the function
cut_video("NyXZU_n4Zbc.mp4", "output_video.mp4", 0, 99.42)