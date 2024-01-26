BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id=id
        if not isinstance(id,int):
            raise TypeError("ID книги должен быть числовым значением")
        self.name = name
        if not isinstance(pages,int):
            raise TypeError("Количество страниц должно быть числительным")
        if pages<1:
            raise ValueError("Не может быть меньше 1 страницы в книге, иначе это обложка")
        self.pages=pages
    def __str__(self):
        return f'Книга "{self.name}"'
    def __repr__(self):
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"

# TODO написать класс Library
class Library:
    def __init__(self,books: list=None):
        self.books=books
        if books is None:
            self.id=0
        else:
            self.id=len(books)

    def get_next_book_id(self):
        next_book=self.id+1
        return next_book


    def get_index_by_book_id(self,index):
        for i,book in enumerate(self.books):
            if book.id==index:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
