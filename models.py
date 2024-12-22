from mongoengine import Document, StringField, ListField, ReferenceField, connect

# Підключення до бази даних
from mongoengine import connect

connect(host="mongodb+srv://sumyultras88:Ghbdtn_123456@cluster0.4nl1k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


# Модель автора
class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# Модель цитати
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=2)  # Reference to Author
    quote = StringField(required=True)
