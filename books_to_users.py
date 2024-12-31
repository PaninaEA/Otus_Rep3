import json
from csv import DictReader

from files import CSV_FILE_PATH

from files import JSON_FILE_PATH, JSON_FILE_PATH_R


with open(CSV_FILE_PATH, newline="") as b:
    reader = DictReader(b)
    list_book = []
    order_list_book = ["Title", "Author", "Pages", "Genre"]
    for rows in reader:
        book = {key: rows[key] for key in order_list_book}
        list_book.append(book)


with open(JSON_FILE_PATH, "r") as u:
    users = json.load(u)
    list_user = []
    order_list = ["name", "gender", "address", "age"]
    for rows in users:
        user = {key: rows[key] for key in order_list}
        list_user.append(user)

k = len(list_user) - 1
i = 0
for rows in list_book:
    list_user[i].setdefault("books", []).append(rows)
    if i == k:
        i = 0
    else:
        i = i + 1

with open(JSON_FILE_PATH_R, "w") as r:
    r.write(json.dumps(list_user, indent=4))
