# video_editor.py

import ffmpeg
import logging

# Configure logging
logging.basicConfig(filename='output/video_editor.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def trim_video(input_path, output_path, start_time, duration):
    """Trim a video using FFmpeg."""
    try:
        (
            ffmpeg
            .input(input_path, ss=start_time, t=duration)
            .output(output_path)
            .run(overwrite_output=True)
        )
        logging.info(f"Trimmed video saved to {output_path}")
    except Exception as e:
        logging.error(f"Error trimming video: {e}")

def add_text_overlay(input_path, output_path, text):
    """Add text overlay to a video using FFmpeg."""
    try:
        (
            ffmpeg
            .input(input_path)
            .drawtext(text=text, fontsize=24, fontcolor='white', x='(w-text_w)/2', y='(h-text_h)/2')
            .output(output_path)
            .run(overwrite_output=True)
        )
        logging.info(f"Video with text overlay saved to {output_path}")
    except Exception as e:
        logging.error(f"Error adding text overlay: {e}")

if __name__ == "__main__":
    trim_video('input.mp4', 'output_trimmed.mp4', start_time=10, duration=30)
    add_text_overlay('output_trimmed.mp4', 'output_final.mp4', text="Travel Tips")