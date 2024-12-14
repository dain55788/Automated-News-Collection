import requests
import json
from data_transformation import transform
import logging
import os
import time

logger = logging.getLogger(__name__)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

def get_other_news_categories(category):
    api_key = os.getenv("API_KEY")
    # Su dung logging hoac print de log tien do code chay
    logger.debug(f"Ingest data {category}")
    start_time = time.time()
    if category == 'politic':
        response = requests.get(f"https://newsapi.org/v2/everything?q=politic%20OR%20president&language=en&sortBy=popularity&apiKey={api_key}", headers=headers)
    else:
        response = requests.get(f"https://newsapi.org/v2/everything?q={category}&language=en&sortBy=popularity&apiKey={api_key}", headers=headers)
    end_time = time.time()
    processing_time = end_time - start_time
    print(f"Processing time: {processing_time:.4f} seconds")
    file_path = f'Automated-News-Collection/news_data/{category}_news.json'

    print("Start execution")

    if response.status_code == 200:
        news = response.json()
        
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(news, f, ensure_ascii=False, indent=4)
        
        transform(file_path)
        print(f"News articles saved to {category} file and has been transformed.")
    else:
        print(f"Failed to fetch news: {response.status_code}")

# get_other_news_categories()