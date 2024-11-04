import requests
import json
import os

# URL

def get_news_data():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=4b3891226ba640f2923d70515226148b"
    response = requests.get(url)
    file_path = '/opt/airflow/news_data/news.json'

    print("Start execution")

    if response.status_code == 200:
        # Parse the response JSON
        news = response.json()
        
        # Save the data to a JSON file
        with open(file_path, 'w') as f:
            json.dump(news, f, ensure_ascii=False, indent=4)

        print(f"News articles saved to news file.")
    else:
        print(f"Failed to fetch news: {response.status_code}")