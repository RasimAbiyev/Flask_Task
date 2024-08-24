import requests
import pymysql

MOVIE = input("Enter the name of the film: ")
API_KEY = "5d9df2b8"

url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE}"
response = requests.get(url)
data = response.json()

if data['Response'] == 'True':
    title = data.get('Title', 'N/A')
    released = data.get('Released', 'N/A')
    genre = data.get('Genre', 'N/A')
    director = data.get('Director', 'N/A')

    print(f"Title: {title}")
    print(f"Released: {released}")
    print(f"Genre: {genre}")
    print(f"Director: {director}")

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345',
        db='kino_db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Movie_info (title, released, genre, director) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (title, released, genre, director))
            connection.commit()
            print("Film məlumatları uğurla saxlanıldı.")
    finally:
        connection.close()
else:
    print(f"Film '{MOVIE}' tapılmadı.")
