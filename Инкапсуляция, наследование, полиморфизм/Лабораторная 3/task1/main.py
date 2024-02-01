class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"
    @property
    def name(self):
        print(self._name)
    @name.getter
    def name(self):
        return self._name
    @property
    def author(self):
        print(self._author)
    @author.getter
    def author(self):
        return self._author




class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        self.pages = self.proverka(pages)
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"
    def proverka (self,a):
        if not isinstance(a,int):
            raise TypeError("Некорректный тип")
        if a<0:
            raise ValueError("нет отрицательных книг")
        return a

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = self.proverka(duration)
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"
    def proverka (self,a):
        if not isinstance(a,float):
            raise TypeError("Некорректный тип")
        if a<0:
            raise ValueError("нет отрицательных книг")
        return a
if __name__ == "__main__":
    book= Book("Великое путешествие", "Неизвестный")
    print(book.__str__())
    print(book.__repr__())
    book.name
    book= PaperBook("Великое путешествие", "Неизвестный",20)
    book.author
    print(book.__str__())
    print(book.__repr__())
    book= AudioBook("Великое путешествие", "Неизвестный",50.2)
    print(book.__str__())
    print(book.__repr__())
    book.name

