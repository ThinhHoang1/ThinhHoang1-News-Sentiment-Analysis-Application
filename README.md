# News Sentiment Analysis Application

## Overview
This project is a Streamlit application that fetches and analyzes news articles based on user-defined topics. Utilizing the Google Gemini API and NewsAPI, the application provides sentiment analysis and investment recommendations.

## Features
- **User Input**: Enter a topic (e.g., "bitcoin") to fetch relevant news articles.
- **Fetch Articles**: Retrieves articles published in the last three days.
- **Sentiment Analysis**: Analyzes the sentiment of the fetched articles and provides recommendations on whether to buy, sell, or hold based on the sentiment.

## Technologies Used
- **Programming Language**: Python
- **Framework**: Streamlit
- **APIs**:
  - Google Gemini API for sentiment analysis
  - NewsAPI for fetching news articles
- **Environment Management**: dotenv for managing API keys

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/news-sentiment-analysis.git
   cd news-sentiment-analysis

2. Install required packages:
pip install -r requirements.txt

3. Create a .env file in the root directory and add your API keys
 ```python
   GEMINI_API_KEY=your_gemini_api_key
   newsapi_key=your_newsapi_key
   ```

4. Run the application:
   ```bash
   streamlit run app.py
```



