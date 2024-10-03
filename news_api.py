import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from newsapi import NewsApiClient
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Configure the Google Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=[],
    generation_config=generation_config,
)

# Initialize NewsApiClient to fetch news data
newsapi = NewsApiClient(api_key=os.getenv("newsapi_key"))

# Streamlit app
st.title('News Sentiment Analysis')
st.write('Fetch articles and analyze their sentiment.')

# User input for topic
topic = st.text_input('Enter topic for news articles (e.g., bitcoin)')

def fetch_articles(topic):
    # Get today's date and the date three days ago
    today = datetime.now().strftime('%Y-%m-%d')
    three_days_ago = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
    
    all_articles = newsapi.get_everything(
        q=topic,
        language='en',
        from_param=three_days_ago,
        to=today,
        sort_by='relevancy'
    )
    
    if 'articles' in all_articles and all_articles['articles']:
        # Filter articles that contain the topic in title or description
        filtered_articles = [
            article for article in all_articles['articles']
            if topic.lower() in article['title'].lower() or 
               (article.get('description') and topic.lower() in article['description'].lower())
        ]
        return filtered_articles[:5]  # Get top 5 relevant articles
    else:
        st.write("No articles found for the specified topic.")
        return []


def analyze_sentiment(text):
    try:
        # Start a chat session
        chat_session = model.start_chat(history=[])
        # Construct the message to be sent
        message = f"Analyze the sentiment of the following text: {text}. Based on the sentiment, should I buy, sell, or hold? Please respond with 'buy', 'sell', or 'hold'."
        # Send the message to the chat session
        response = chat_session.send_message(message)
        return response.text.strip()
    except Exception as e:
        st.write(f"Error during sentiment analysis: {e}")
        return "Error"

if st.button('Fetch Articles'):
    with st.spinner('Fetching articles...'):
        articles = fetch_articles(topic)
    
    for idx, article in enumerate(articles):
        title = article['title']
        text = f"{title} {article.get('description', '')}"
        sentiment = analyze_sentiment(text)
        
        # Display the article title and sentiment
        st.markdown(f"### Article {idx + 1}: {title}")
        st.markdown(f"**Sentiment:** {sentiment}")

        # Analyze and display the decision in one call
       
