import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# DATA TRANSFORMATION PHASE
# check if the articles are removed or not
def is_valid_article(article):
    return (article.get('title') != '[Removed]' and article['source']['name'] != "Yahoo Entertainment")

categories_list = ['technology', 'sports', 'entertainment', 'politic', 'business', 'health']
news_file_path = f'Automated-News-Collection/news_data/news.json'

# fetch full content from a URL
def fetch_full_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            paragraphs = soup.find_all('p')
            full_content = ' '.join([para.get_text() for para in paragraphs])
            return full_content
        else:
            print(f"Failed to fetch content from {url}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# transform function:
def transform(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        data = json.load(file)
    
    # Filter out invalid articles which are removed
    filtered_articles = [article for article in data['articles'] if is_valid_article(article)]

    # Index the article IDs
    article_id = 1
    for article in filtered_articles:
        if "id" in article["source"]:
            del article["source"]["id"]
        article["source"]["article_id"] = article_id
        article_content = fetch_full_content(article['url'])
        article["content"] = article_content if article_content else "Content could not be fetched."
        article_id += 1
        
    data['articles'] = filtered_articles


    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

