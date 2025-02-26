# topic_model.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_topics(feedback, topic_count):
    """Extract topics from feedback using LDA."""
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(feedback)
    
    lda = LatentDirichletAllocation(n_components=topic_count, random_state=42)
    lda.fit(dtm)
    
    topics = []
    for idx, topic in enumerate(lda.components_):
        top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        topics.append(f"Topic {idx+1}: {' '.join(top_words)}")
    
    return topics