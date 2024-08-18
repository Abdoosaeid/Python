import os
from moviepy.editor import VideoFileClip

def get_video_duration(file_path):
    try:
        video = VideoFileClip(file_path)
        duration = video.duration  # Duration in seconds
        video.close()
        return duration
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def calculate_total_duration(folder_path):
    total_duration = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.flv')):
            file_path = os.path.join(folder_path, filename)
            total_duration += get_video_duration(file_path)
    return total_duration

def main():
    folder_path = input("Enter the path to the folder containing videos: ")
    if os.path.isdir(folder_path):
        total_duration = calculate_total_duration(folder_path)
        total_duration_minutes = total_duration / 60  # Convert to minutes
        print(f"Total duration of videos: {total_duration_minutes // 60 } Hours {round(total_duration_minutes % 60) } minutes")
    else:
        print("Invalid folder path")

if __name__ == "__main__":
    main()
