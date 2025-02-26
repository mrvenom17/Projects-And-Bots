# article_generator.py

import openai
import pandas as pd
from config import OPENAI_API_KEY, BLOG_TOPICS, SEO_KEYWORDS

openai.api_key = OPENAI_API_KEY

# Configure logging
import logging
logging.basicConfig(filename='output/article_generator.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_article(topic, keywords):
    """Generate a blog post using OpenAI GPT-4."""
    keyword_list = ', '.join(keywords)
    prompt = f"Write a detailed and SEO-optimized blog post about '{topic}'.\n" \
             f"Include the following keywords naturally: {keyword_list}.\n" \
             f"The article should be at least 800 words long and include an introduction, body, and conclusion."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def generate_all_articles():
    """Generate blog posts for all topics."""
    logging.info("Starting Blog Article Generator Bot...")
    all_articles = []
    
    for topic in BLOG_TOPICS:
        keywords = SEO_KEYWORDS.get(topic.split()[0], [])
        logging.info(f"Generating article for topic: {topic}")
        article = generate_article(topic, keywords)
        all_articles.append({
            'topic': topic,
            'article': article
        })
    
    df = pd.DataFrame(all_articles)
    df.to_csv('output/articles.csv', index=False)
    logging.info("Article generation completed. Data saved to articles.csv")

if __name__ == "__main__":
    generate_all_articles()