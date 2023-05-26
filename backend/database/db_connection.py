import mysql.connector

# 資料庫連接設定
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database_name',
    'raise_on_warnings': True
}

# 建立資料庫連接
cnx = mysql.connector.connect(**config)