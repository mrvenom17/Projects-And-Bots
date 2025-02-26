# app.py (Flask Dashboard)

from flask import Flask, request, render_template
import os
from video_editor import run_video_editor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        video = request.files['video']
        captions = request.files['captions']
        
        video_path = os.path.join('input_videos', video.filename)
        captions_path = os.path.join('captions.txt')
        
        video.save(video_path)
        captions.save(captions_path)
        
        run_video_editor()
        return "Video editing completed!"
    
    return '''
    <!doctype html>
    <title>Upload Video and Captions</title>
    <h1>Upload Video and Captions</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=video>
      <input type=file name=captions>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)