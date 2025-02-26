# analyzer.py

import pandas as pd
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_post(post):
    """Analyze a post using OpenAI GPT-4."""
    prompt = f"Analyze the following dark web post for potential threats:\n{post}\n" \
             f"Provide a summary and indicate if it poses a threat."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_analysis():
    """Main function to run the analysis."""
    data = pd.read_csv('logs/dark_web_data.csv')
    analyses = []
    
    for _, row in data.iterrows():
        analysis = analyze_post(row['content'])
        analyses.append(analysis)
    
    data['analysis'] = analyses
    data.to_csv('logs/analyzed_dark_web_data.csv', index=False)
    logging.info("Analysis completed. Data saved to analyzed_dark_web_data.csv")

if __name__ == "__main__":
    run_analysis()