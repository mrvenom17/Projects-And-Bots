# analyzer.py

import pandas as pd
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def evaluate_domain(domain):
    """Evaluate domain potential using OpenAI GPT-4."""
    prompt = f"Evaluate the following domain for flipping potential:\n" \
             f"Domain Name: {domain['name']}\n" \
             f"Price: {domain['price']}\n" \
             f"Traffic: {domain['traffic']}\n" \
             f"Backlinks: {domain['backlinks']}\n" \
             f"Provide a score (1-10) and reasoning."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_analysis():
    """Main function to run the analysis."""
    data = pd.read_csv('output/domains.csv')
    evaluations = []
    
    for _, row in data.iterrows():
        evaluation = evaluate_domain(row)
        evaluations.append(evaluation)
    
    data['evaluation'] = evaluations
    data.to_csv('output/evaluated_domains.csv', index=False)
    logging.info("Evaluation completed. Data saved to evaluated_domains.csv")

if __name__ == "__main__":
    run_analysis()