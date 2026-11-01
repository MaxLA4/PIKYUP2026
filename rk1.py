class Book:
    def __init__(self, id, title, price, store_id):
        self.id = id
        self.title = title
        self.price = price
        self.store_id = store_id


class Store:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookStore:
    def __init__(self, book_id, store_id):
        self.book_id = book_id
        self.store_id = store_id


stores = [
    Store(1, 'Книжный магазин «Читай-город»'),
    Store(2, 'Академкнига'),
    Store(3, 'Магазин «Дом книги»'),
    Store(4, 'Антикварный книжный магазин'),
    Store(5, 'Библио-Глобус'),
]

books = [
    Book(1, 'Анна Каренина', 450, 1),
    Book(2, 'Война и мир', 900, 1),
    Book(3, 'Алгоритмы', 1500, 2),
    Book(4, 'Python. Подробное руководство', 1200, 2),
    Book(5, 'Мастер и Маргарита', 500, 3),
    Book(6, 'Азбука', 300, 3),
    Book(7, 'Евгений Онегин', 350, 4),
    Book(8, 'Архипелаг ГУЛАГ', 800, 5),
]

books_stores = [
    BookStore(1, 1), BookStore(1, 3),
    BookStore(2, 1), BookStore(2, 4),
    BookStore(3, 2), BookStore(3, 5),
    BookStore(4, 2), BookStore(4, 1),
    BookStore(5, 3), BookStore(5, 5),
    BookStore(6, 3), BookStore(6, 2),
    BookStore(7, 4),
    BookStore(8, 5), BookStore(8, 1),
]


def main():
    one_to_many = [(b.title, b.price, s.name)
                   for s in stores
                   for b in books
                   if b.store_id == s.id]

    many_to_many_temp = [(s.name, bs.store_id, bs.book_id)
                         for s in stores
                         for bs in books_stores
                         if s.id == bs.store_id]

    many_to_many = [(b.title, b.price, store_name)
                    for store_name, store_id, book_id in many_to_many_temp
                    for b in books
                    if b.id == book_id]

    print('Задание Е1')
    res_1 = {}
    for s in stores:
        if 'магазин' in s.name.lower():
            res_1[s.name] = [x[0] for x in one_to_many if x[2] == s.name]
    for name in res_1:
        print(name, '-', res_1[name])

    print('\nЗадание Е2')
    res_2 = []
    for s in stores:
        prices = [x[1] for x in one_to_many if x[2] == s.name]
        if len(prices) > 0:
            avg = round(sum(prices) / len(prices), 2)
            res_2.append((s.name, avg))
    res_2 = sorted(res_2, key=lambda x: x[1])
    for item in res_2:
        print(item[0], '-', item[1])

    print('\nЗадание Е3')
    res_3 = {}
    for b in books:
        if b.title.startswith('А'):
            res_3[b.title] = [x[2] for x in many_to_many if x[0] == b.title]
    for title in res_3:
        print(title, '-', res_3[title])


if __name__ == '__main__':
    main()
