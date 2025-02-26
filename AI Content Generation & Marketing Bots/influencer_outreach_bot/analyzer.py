# analyzer.py

import pandas as pd
import openai
from config import OPENAI_API_KEY, MIN_ENGAGEMENT_RATE

openai.api_key = OPENAI_API_KEY

def calculate_engagement_rate(followers, likes, comments):
    """Calculate engagement rate based on followers, likes, and comments."""
    return ((likes + comments) / followers) * 100

def evaluate_influencer(influencer):
    """Evaluate influencer potential using OpenAI GPT-4."""
    prompt = f"Evaluate the following influencer for collaboration potential:\n" \
             f"Username: {influencer['username']}\n" \
             f"Platform: {influencer['platform']}\n" \
             f"Followers: {influencer['followers']}\n" \
             f"Engagement Rate: {influencer['engagement_rate']}%\n" \
             f"Provide a score (1-10) and reasoning."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_analysis():
    """Main function to run the analysis."""
    data = pd.read_csv('output/influencers.csv')
    evaluations = []
    
    for _, row in data.iterrows():
        engagement_rate = calculate_engagement_rate(row['followers'], row['likes'], row['comments'])
        if engagement_rate >= MIN_ENGAGEMENT_RATE:
            evaluation = evaluate_influencer(row)
            evaluations.append(evaluation)
    
    data['evaluation'] = evaluations
    data.to_csv('output/evaluated_influencers.csv', index=False)
    logging.info("Evaluation completed. Data saved to evaluated_influencers.csv")

if __name__ == "__main__":
    run_analysis()