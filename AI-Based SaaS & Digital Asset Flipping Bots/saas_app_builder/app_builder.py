# app_builder.py

import os
import shutil
from jinja2 import Environment, FileSystemLoader
from config import APP_NAME, AI_MODEL_PATH, DATABASE_URL, FRONTEND_FRAMEWORK, BACKEND_FRAMEWORK, DEPLOYMENT_PLATFORM
import logging

# Configure logging
logging.basicConfig(filename='logs/app_builder.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_backend():
    """Generate backend code using predefined templates."""
    env = Environment(loader=FileSystemLoader('templates/backend'))
    template = env.get_template(f"{BACKEND_FRAMEWORK}_template.py")
    
    backend_code = template.render(app_name=APP_NAME, database_url=DATABASE_URL, ai_model_path=AI_MODEL_PATH)
    
    os.makedirs(f"output/{APP_NAME}/backend", exist_ok=True)
    with open(f"output/{APP_NAME}/backend/app.py", 'w') as f:
        f.write(backend_code)
    
    logging.info("Backend code generated.")

def generate_frontend():
    """Generate frontend code using predefined templates."""
    env = Environment(loader=FileSystemLoader('templates/frontend'))
    template = env.get_template(f"{FRONTEND_FRAMEWORK}_template.js")
    
    frontend_code = template.render(app_name=APP_NAME)
    
    os.makedirs(f"output/{APP_NAME}/frontend", exist_ok=True)
    with open(f"output/{APP_NAME}/frontend/app.js", 'w') as f:
        f.write(frontend_code)
    
    logging.info("Frontend code generated.")

def build_docker_image():
    """Build a Docker image for the app."""
    dockerfile = f"""
    FROM python:3.9-slim
    WORKDIR /app
    COPY . /app
    RUN pip install -r requirements.txt
    CMD ["python", "backend/app.py"]
    """
    
    os.makedirs(f"output/{APP_NAME}", exist_ok=True)
    with open(f"output/{APP_NAME}/Dockerfile", 'w') as f:
        f.write(dockerfile)
    
    logging.info("Dockerfile generated.")

def deploy_app():
    """Deploy the app to the specified platform."""
    if DEPLOYMENT_PLATFORM == "heroku":
        os.system(f"heroku create {APP_NAME}")
        os.system(f"git init && git add . && git commit -m 'Initial commit'")
        os.system(f"git push heroku master")
        logging.info(f"App deployed to Heroku: https://{APP_NAME}.herokuapp.com")
    elif DEPLOYMENT_PLATFORM == "docker":
        os.system(f"docker build -t {APP_NAME} output/{APP_NAME}")
        os.system(f"docker run -d -p 5000:5000 {APP_NAME}")
        logging.info(f"App running locally via Docker: http://localhost:5000")

def run_app_builder():
    """Main function to run the SaaS app builder."""
    logging.info("Starting SaaS App Builder...")
    
    generate_backend()
    generate_frontend()
    build_docker_image()
    deploy_app()

if __name__ == "__main__":
    run_app_builder()