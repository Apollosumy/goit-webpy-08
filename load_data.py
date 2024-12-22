import json
from models import Author, Quote

# Завантаження даних із файлів
with open('authors.json', 'r', encoding='utf-8') as authors_file:
    authors_data = json.load(authors_file)

with open('qoutes.json', 'r', encoding='utf-8') as quotes_file:
    quotes_data = json.load(quotes_file)

# Додавання авторів до бази
for author in authors_data:
    if not Author.objects(fullname=author['fullname']):
        Author(
            fullname=author['fullname'],
            born_date=author.get('born_date'),
            born_location=author.get('born_location'),
            description=author.get('description')
        ).save()

# Додавання цитат до бази
for quote in quotes_data:
    author = Author.objects(fullname=quote['author']).first()
    if author:
        if not Quote.objects(quote=quote['quote']):
            Quote(
                tags=quote['tags'],
                author=author,
                quote=quote['quote']
            ).save()
