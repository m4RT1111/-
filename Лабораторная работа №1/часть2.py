# TODO Найдите количество книг, которое можно разместить на дискете
num1 = 1024
Vol_ = 1.44
count = 100
lines = 50
symbolsinline = 25
symb = 4
allsymb = symbolsinline * lines * count
book = (allsymb * symb) / num1**2
result = (Vol_) // (book)
print("Количество книг, помещающихся на дискету:", "{:.0f}".format(result))
