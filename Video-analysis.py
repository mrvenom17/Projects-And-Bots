import cv2
import numpy as np

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    sample_frames = []
    frame_indices = np.linspace(0, frame_count - 1, num=10, dtype=int)
    
    for i in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            sample_frames.append(gray_frame)
    
    contrast_values = [np.std(frame) for frame in sample_frames]
    avg_contrast = np.mean(contrast_values)
    brightness_values = [np.mean(frame) for frame in sample_frames]
    avg_brightness = np.mean(brightness_values)
    cap.release()
    
    return {
        "Resolution": f"{video_width}x{video_height}",
        "Duration (seconds)": round(duration, 2),
        "Average Contrast": round(avg_contrast, 2),
        "Average Brightness": round(avg_brightness, 2),
        "FPS": round(fps, 2)
    }

def suggest_improvements(analysis):
    improvements = []
    if analysis["Average Brightness"] < 25:
        improvements.append("Increase brightness to ~25-30 for better visibility.")
    if analysis["Average Contrast"] < 40:
        improvements.append("Enhance contrast to improve sharpness and engagement.")
    if analysis["Duration (seconds)"] > 20:
        improvements.append("Shorten video length to 15-20 sec for higher retention.")
    return improvements

def enhance_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS),
                           (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        enhanced_frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=20)  # Adjust contrast & brightness
        out.write(enhanced_frame)
    
    cap.release()
    out.release()
    print("Enhanced video saved at", output_path)

# Usage
video_file = "enhanced_video.mp4"
output_file = "enhanced.mp4"

analysis_results = analyze_video(video_file)
print("Analysis Results:", analysis_results)

suggestions = suggest_improvements(analysis_results)
print("Suggested Improvements:", suggestions)

enhance_video(video_file, output_file)
