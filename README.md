Активируйте среду.
Создайте .env файл с содержимым:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```
Запустите init_db.py:
```
python3 app/init_db.py
```
Потом запустите main.py:
```
python3 app/main.py
```