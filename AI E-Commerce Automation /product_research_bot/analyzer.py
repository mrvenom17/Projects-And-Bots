# analyzer.py

import pandas as pd
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_trends(data):
    """Analyze product trends using OpenAI."""
    prompt = f"Analyze the following products and identify trending items:\n{data.to_string()}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def run_analysis():
    """Main function to run the analysis."""
    data = pd.read_csv('output/products.csv')
    trends = analyze_trends(data)
    with open('output/trends.txt', 'w') as f:
        f.write(trends)
    print("Trend analysis completed. Results saved to trends.txt.")

if __name__ == "__main__":
    run_analysis()