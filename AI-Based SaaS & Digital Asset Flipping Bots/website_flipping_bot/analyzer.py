# analyzer.py

import pandas as pd
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def evaluate_website(website):
    """Evaluate website potential using OpenAI GPT-4."""
    prompt = f"Evaluate the following website for flipping potential:\n" \
             f"Website Name: {website['name']}\n" \
             f"Price: {website['price']}\n" \
             f"Traffic: {website['traffic']}\n" \
             f"Revenue: {website['revenue']}\n" \
             f"Provide a score (1-10) and reasoning."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_analysis():
    """Main function to run the analysis."""
    data = pd.read_csv('logs/websites.csv')
    evaluations = []
    
    for _, row in data.iterrows():
        evaluation = evaluate_website(row)
        evaluations.append(evaluation)
    
    data['evaluation'] = evaluations
    data.to_csv('logs/evaluated_websites.csv', index=False)
    logging.info("Evaluation completed. Data saved to evaluated_websites.csv")

if __name__ == "__main__":
    run_analysis()