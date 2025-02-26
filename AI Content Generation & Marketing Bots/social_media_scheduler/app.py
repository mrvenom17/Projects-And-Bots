# app.py (Flask Dashboard)

from flask import Flask, request, render_template
from scheduler import schedule_posts

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def manage_posts():
    if request.method == 'POST':
        platform = request.form['platform']
        content = request.form['content']
        time_to_post = request.form['time']
        
        # Add the post to the schedule
        POSTS.append({"platform": platform, "content": content, "time": time_to_post})
        schedule_posts()
        return "Post scheduled successfully!"
    
    return '''
    <!doctype html>
    <title>Schedule Social Media Post</title>
    <h1>Schedule a Post</h1>
    <form method=post>
      Platform: <input type=text name=platform><br>
      Content: <input type=text name=content><br>
      Time (YYYY-MM-DD HH:MM:SS): <input type=text name=time><br>
      <input type=submit value=Schedule>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)