import pandas as pd
import json, csv

# check if the articles are removed or not
def is_valid_article(article):
    return article.get('title') != '[Removed]'

categories_list = ['technology', 'sports', 'entertainment', 'politic', 'business', 'health']
news_file_path = f'news_data/news.json'

# transform function:
def transform(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Filter out invalid articles
    filtered_articles = [article for article in data['articles'] if is_valid_article(article)]
    data['articles'] = filtered_articles

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Load the JSON data from the file
def transform_news():
    transform(news_file_path)

def transform_other_news():
    for i in range(len(categories_list)):
        other_file_path = f'news_data/{categories_list[i]}_news.json'
        transform(other_file_path)

