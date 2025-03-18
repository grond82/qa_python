import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'name',
        [
            '',
            'Это очень длинное название книги для проверки'
        ]
    )
    def test_add_new_book_add_book_with_long_and_zero_name(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Ветер в ивах', 'Мультфильмы'],
            ['Оно', 'Ужасы']
        ]
    )
    def test_set_book_genre_add_genre_to_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_get_book_genre_get_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Ветер в ивах')
        collector.set_book_genre('Ветер в ивах','Мультфильмы')
        assert collector.get_book_genre('Ветер в ивах') == 'Мультфильмы'

    def test_get_books_with_specific_genre_get_books_with_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ветер в ивах')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Оно')
        collector.set_book_genre('Ветер в ивах', 'Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Оно', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_return_correct_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ветер в ивах')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Оно')
        collector.set_book_genre('Ветер в ивах', 'Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_genre() == {'Ветер в ивах': 'Мультфильмы',
                                               'Гордость и предубеждение и зомби': 'Ужасы',
                                               'Оно': 'Ужасы'
                                              }

    def test_get_books_for_children_check_comedy(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.add_new_book('Сон в летнюю ночь')
        collector.add_new_book('Оно')
        collector.set_book_genre('12 стульев','Комедии')
        collector.set_book_genre('Сон в летнюю ночь', 'Комедии')
        collector.set_book_genre('Оно','Ужасы')
        assert collector.get_books_for_children() == ['12 стульев', 'Сон в летнюю ночь']

    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        #collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_book_in_favorites('12 стульев')
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_add_book_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_book_in_favorites('13 стульев')
        assert len(collector.favorites) == 0

    def test_add_book_in_favorites_add_two_identical_books(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_book_in_favorites('12 стульев')
        collector.add_book_in_favorites('12 стульев')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_book_in_favorites('12 стульев')
        collector.delete_book_from_favorites('12 стульев')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_check_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.add_new_book('Ветер в ивах')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.set_book_genre('Ветер в ивах', 'Мультфильмы')
        collector.add_book_in_favorites('12 стульев')
        assert collector.get_list_of_favorites_books() == ['12 стульев']