class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'книга "{self.name}"'

    def __repr__(self):
        return f'Book(id={self.id}, name="{self.name}", pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книга с запрашиваемым id не существует")


# Пример использования

# Создание экземпляров класса Book
book1 = Book(1, "Тестовая книга 1", 200)
book2 = Book(2, "Тестовая книга 2", 150)

# Создание экземпляра класса Library и добавление книг
library = Library([book1, book2])

# Получение следующего идентификатора книги
next_id = library.get_next_book_id()
print(f"Следующий идентификатор книги: {next_id}")

# Получение индекса книги по ее идентификатору
try:
    index = library.get_index_by_book_id(1)
    print(f"Индекс книги с id 1: {index}")
except ValueError as e:
    print(e)

# Попытка получить индекс несуществующей книги
try:
    index = library.get_index_by_book_id(3)
    print(f"Индекс книги с id 3: {index}")
except ValueError as e:
    print(e)