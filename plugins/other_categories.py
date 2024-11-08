import requests
import json
from data_transformation import transform

categories_list = ['technology', 'sports', 'entertainment', 'politic', 'business', 'health']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

def get_other_news_categories():
    for i in range(len(categories_list)):

        if categories_list[i] == 'politic':
            response = requests.get(f"https://newsapi.org/v2/everything?q=politic%20OR%20president&language=en&sortBy=popularity&apiKey=4b3891226ba640f2923d70515226148b", headers=headers)
        else:
            response = requests.get(f"https://newsapi.org/v2/everything?q={categories_list[i]}&language=en&sortBy=popularity&apiKey=4b3891226ba640f2923d70515226148b", headers=headers)

        file_path = f'Automated-News-Collection/news_data/{categories_list[i]}_news.json'

        print("Start execution")
    
        if response.status_code == 200:
        # Parse the response JSON
            news = response.json()
            
            # Save the data to a JSON file
            with open(file_path, 'w', encoding="utf-8") as f:
                json.dump(news, f, ensure_ascii=False, indent=4)
            
            transform(file_path)
            print(f"News articles saved to {categories_list[i]} file and has been transformed.")
        else:
            print(f"Failed to fetch news: {response.status_code}")
