# Project Title: img2img upscale of a youtube video

## Overview

This project automates the process of downloading a YouTube video, extracting frames, enhancing those frames with an AI model, and then compiling the frames back into a video with audio.

**Scripts in this project:**
1. `start.bat` - Batch script to set up the environment, install dependencies, and run the main Python script.
2. `make_from_manual.py` - Script to compile processed frames into a video.
3. `create_images.py` - Script to enhance the video frames using the StableDiffusionInstructPix2PixPipeline model.
4. `download_and_parse.py` - Script to download a YouTube video and extract frames from it.

## Requirements

1. Python 3.7 or higher.
2. All required Python packages specified in the `requirements.txt` file.
3. A CUDA-compatible GPU (optional but recommended for faster processing).

## Usage Instructions

### 1. Setup Environment

Ensure you have Python installed. If not, download and install it from [Python's official website](https://www.python.org/).

### 2. Install Dependencies

Run the `start.bat` script to set up a virtual environment and install necessary Python packages.

### `start.bat` Script:

```bat
@echo off

REM Prompt users to read the README.1ST file for detailed instructions.
echo Please make sure you have read the README.1ST file before proceeding.
echo.

REM Check if the virtual environment folder exists
IF NOT EXIST "env" (
    REM Create a virtual environment named "env"
    python -m venv env
    IF %ERRORLEVEL% NEQ 0 (
        echo "Failed to create a virtual environment. Please ensure Python is installed."
        pause
        exit /b
    )
)

REM Activate the virtual environment
CALL env\Scripts\activate

REM Install the required Python packages
pip install -r requirements.txt

REM Run the download_and_parse.py script
python download_and_parse.py

REM Pause the script output
pause

REM Deactivate the virtual environment and exit
CALL env\Scripts\deactivate
exit
```

### 3. Download and Parse Video

The `download_and_parse.py` script downloads a YouTube video, extracts frames, resizes them, and saves them as images.

```sh
# Run the script
python download_and_parse.py
```

### 4. Enhance Images

The `create_images.py` script processes the extracted frames using a style prompt and the Pix2Pix model.

```sh
# Run the script
python create_images.py
```

### 5. Generate Final Video

The `make_from_manual.py` script combines the processed images back into a video with audio.

```sh
# Run the script
python make_from_manual.py
```

## Detailed Explanation

### Batch Script: `start.bat`

This script initializes the environment, installs dependencies, and runs the main Python script to download and process the video.

### Python Script: `download_and_parse.py`

- **Download Video**: Downloads the YouTube video using the `pytube` library.
- **Extract Frames**: Uses `ffmpeg` to extract frames from the video.
- **Resize Frames**: Resizes the frames based on a given percentage and saves them in a specified directory.

### Python Script: `create_images.py`

- **Loads Model**: Loads the StableDiffusionInstructPix2PixPipeline model.
- **Processes Images**: Enhances each frame based on a style prompt.
- **Saves Processed Images**: Saves the enhanced frames to a new directory.

### Python Script: `make_from_manual.py`

- **Assembles Video**: Combines the processed frames into a video.
- **Adds Audio**: Synchronizes the video with the original audio track.
- **Saves Final Video**: Saves the final video with a timestamped filename.

## Important Notes

- **Dependencies**: Ensure all dependencies listed in `requirements.txt` are installed.
- **GPU**: For best performance, use a CUDA-compatible GPU.
- **Storage**: Make sure you have enough storage space for downloading videos and storing frames.

## Troubleshooting

- If you encounter any errors related to missing dependencies, ensure they are properly installed.
- Check the paths and filenames to ensure they are correctly referenced.
- For issues related to GPU processing, make sure you have the appropriate drivers and libraries installed.

## Conclusion

This project aims to simplify the process of downloading, enhancing, and compiling videos. Feel free to modify the scripts as needed to suit your use case.
