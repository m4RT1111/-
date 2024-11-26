# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44  # объем дискеты в Мб
pages = 100          # количество страниц
lines_per_page = 50  # число строк на странице
chars_per_line = 25  # количество символов в строке
bytes_per_char = 4   # объем одного символа в байтах

# Перевод объема дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Объем одной книги в байтах
book_size_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

# Количество книг, которое можно разместить на дискету
books_on_disk = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))