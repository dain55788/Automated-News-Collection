import json
import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="news_data"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_article(connection, article, category):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO articles (source_name, author, title, description, url, urlToImage, publishedAt, content, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
        article["source"]["name"],
        article.get("author"),
        article.get("title"),
        article.get("description"), 
        article.get("url"),
        article.get("urlToImage"),
        article.get("publishedAt"),
        article.get("content"),
        category
    ))
    connection.commit()

def load_articles(file_path, category):
    with open(file_path, encoding='utf-8') as f:
        articles_data = json.load(f)["articles"]

    connection = connect_to_database()
    if connection:
        for article in articles_data:
            insert_article(connection, article, category)
            
        connection.close()

def main():
    category_files = {
        "Automated-News-Collection/news_data/news.json": "top_news",
        "Automated-News-Collection/news_data/technology_news.json": "technology",
        "Automated-News-Collection/news_data/entertainment_news.json" : "entertainment",
        "Automated-News-Collection/news_data/business_news.json": "business",
        "Automated-News-Collection/news_data/sports_news.json": "sports",
        "Automated-News-Collection/news_data/politic_news.json" : "politic",
        "Automated-News-Collection/news_data/health_news.json" : "health"
    }

    for file_name, category in category_files.items():
        print(f"Processing {file_name} as {category}")
        load_articles(file_name, category)

if __name__ == "__main__":
    main()
