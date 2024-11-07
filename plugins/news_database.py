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

def insert_article(connection, article):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO articles (article_id, source_name, author, title, description, url, urlToImage, publishedAt, content)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            source_name=VALUES(source_name),
            author=VALUES(author),
            title=VALUES(title),
            description=VALUES(description),
            url=VALUES(url),
            urlToImage=VALUES(urlToImage),
            publishedAt=VALUES(publishedAt),
            content=VALUES(content)
    """, (
        article["source"]["article_id"],
        article["source"]["name"],
        article["author"],
        article["title"],
        article["description"], 
        article["url"],
        article["urlToImage"],
        article["publishedAt"],
        article["content"]
    ))
    connection.commit()

def main():
    with open('Automated-News-Collection/news_data/news.json', encoding='utf-8') as f:
        articles_data = json.load(f)["articles"]

    connection = connect_to_database()
    if connection:
        for article in articles_data:
            insert_article(connection, article)
        connection.close()

if __name__ == "__main__":
    main()
