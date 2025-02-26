# video_editor.py

import moviepy.editor as mp
from moviepy.video.fx.all import fadein, fadeout
from config import INPUT_VIDEO_PATH, OUTPUT_VIDEO_PATH, CAPTIONS_FILE, BACKGROUND_MUSIC, TRANSITION_DURATION, VIDEO_RESOLUTION
import logging

# Configure logging
logging.basicConfig(filename='output/video_editor.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_captions():
    """Load captions from a text file."""
    with open(CAPTIONS_FILE, 'r') as f:
        captions = [line.strip() for line in f.readlines()]
    return captions

def add_captions(video, captions):
    """Add captions to the video."""
    clips = []
    duration_per_clip = video.duration / len(captions)
    
    for i, caption in enumerate(captions):
        start_time = i * duration_per_clip
        end_time = (i + 1) * duration_per_clip
        
        clip = video.subclip(start_time, end_time)
        txt_clip = mp.TextClip(caption, fontsize=50, color='white', size=VIDEO_RESOLUTION).set_position(('center', 'bottom')).set_duration(clip.duration)
        
        final_clip = mp.CompositeVideoClip([clip, txt_clip])
        clips.append(final_clip)
    
    return mp.concatenate_videoclips(clips)

def add_background_music(video):
    """Add background music to the video."""
    audio = mp.AudioFileClip(BACKGROUND_MUSIC)
    audio = audio.subclip(0, video.duration).volumex(0.2)  # Lower volume
    final_audio = mp.CompositeAudioClip([video.audio, audio])
    video = video.set_audio(final_audio)
    return video

def apply_transitions(video):
    """Apply fade-in and fade-out transitions."""
    video = fadein(video, TRANSITION_DURATION)
    video = fadeout(video, TRANSITION_DURATION)
    return video

def run_video_editor():
    """Main function to run the video editor."""
    logging.info("Starting Video Editor Bot...")
    
    # Load the input video
    video = mp.VideoFileClip(INPUT_VIDEO_PATH)
    video = video.resize(VIDEO_RESOLUTION)  # Resize for TikTok/Instagram
    
    # Add captions
    captions = load_captions()
    video_with_captions = add_captions(video, captions)
    
    # Add background music
    video_with_music = add_background_music(video_with_captions)
    
    # Apply transitions
    final_video = apply_transitions(video_with_music)
    
    # Save the edited video
    final_video.write_videofile(OUTPUT_VIDEO_PATH, codec='libx264', audio_codec='aac')
    logging.info(f"Video editing completed. Edited video saved to {OUTPUT_VIDEO_PATH}")

if __name__ == "__main__":
    run_video_editor()