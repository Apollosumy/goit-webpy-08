from models import Author, Quote

def search_by_name(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    return []

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

def main():
    print("Введіть команду у форматі: name:значення, tag:значення, tags:значення1,значення2 або exit.")
    while True:
        command = input(">>> ").strip()
        if command == "exit":
            print("Вихід з програми.")
            break

        if command.startswith("name:"):
            name = command.split(":", 1)[1].strip()
            results = search_by_name(name)
            for result in results:
                print(result.encode('utf-8').decode('utf-8'))

        elif command.startswith("tag:"):
            tag = command.split(":", 1)[1].strip()
            results = search_by_tag(tag)
            for result in results:
                print(result.encode('utf-8').decode('utf-8'))

        elif command.startswith("tags:"):
            tags = command.split(":", 1)[1].strip()
            results = search_by_tags(tags)
            for result in results:
                print(result.encode('utf-8').decode('utf-8'))

        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
