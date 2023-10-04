import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('camp_articles.db')
cursor = conn.cursor()

# articlesテーブルを作成（存在しない場合のみ）
cursor.execute('''
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY,
    title TEXT,
    link TEXT
)
''')
conn.commit()

# スクレイピング対象のURL
url = "https://camp-quests.com/"

# ページの内容を取得
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 記事のタイトルとリンクを取得
articles = []
article_elements = soup.find_all("a", href=True)
for article in article_elements:
    title = article.text.strip()
    link = article["href"]
    if title and link.startswith("https://camp-quests.com/"):
        articles.append((title, link))

# データベースに保存
conn = sqlite3.connect("camp_articles.db")
cursor = conn.cursor()

for title, link in articles:
    cursor.execute("INSERT INTO articles (title, link) VALUES (?, ?)", (title, link))

conn.commit()
conn.close()
