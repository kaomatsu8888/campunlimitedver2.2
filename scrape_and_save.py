# SQLiteデータベースに接続
conn = sqlite3.connect('articles.db')
cursor = conn.cursor()

# データの取得
cursor.execute('SELECT title, content FROM articles')
articles = cursor.fetchall()

for article in articles:
    print("Title:", article[0])
    print("Content:", article[1])
    print("------")

conn.close()
