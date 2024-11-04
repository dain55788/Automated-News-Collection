import requests
import json
import os
from datetime import datetime
# URL

def get_other_news_categories():
    categories_list = ['technology', 'sports', 'entertainment', 'politic', 'business', 'health']
    for i in range(len(categories_list)):

        if categories_list[i] == 'politic':
            response = requests.get(f"https://newsapi.org/v2/everything?q=politic%20OR%20president&language=en&sortBy=popularity&apiKey=4b3891226ba640f2923d70515226148b")
        else:
            response = requests.get(f"https://newsapi.org/v2/everything?q={categories_list[i]}&language=en&sortBy=popularity&apiKey=4b3891226ba640f2923d70515226148b")

        file_path = f'news_data/{categories_list[i]}_news.json'

        print("Start execution")
    
        if response.status_code == 200:
        # Parse the response JSON
            news = response.json()
            
            # Save the data to a JSON file
            with open(file_path, 'w', encoding="utf-8") as f:
                json.dump(news, f, ensure_ascii=False, indent=4)

            print(f"News articles saved to {categories_list[i]} file.")
        else:
            print(f"Failed to fetch news: {response.status_code}")
