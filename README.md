# qa_python

Описание тестов

test_add_new_book_add_book_with_long_name - проверка на добавление книги со слишком длинным именем. Она не должна добавиться.

test_add_new_book_add_book_with_zero_name - проверка на добавление книги с пустым именем. Она не должна добавиться.

test_set_book_genre_add_genre_to_book - проверка на добавление жанра к книге

test_get_book_genre_get_genre_by_name - проверка на получение жанра по имени книги

test_get_books_with_specific_genre_get_books_with_correct_genre - проверка на получение книг по жанру

test_get_books_genre_return_correct_books_genre - проверка на получение списка всех книг с названием и жанром

test_get_books_for_children_check_comedy - проверка на получение книг, разрешенных детям жанров. В тесте комедии

test_add_book_in_favorites_add_book - проверка на добавление книг в избранное

test_add_book_in_favorites_add_book_not_in_books_genre - проверка на добавление книги, которой не в списке, в избранное. Не должна добавиться.

test_add_book_in_favorites_add_two_identical_books - проверка на добавление двух одинаковых книг в избранное. Добавиться только одна.

test_delete_book_from_favorites_delete_book - проверка на удаление книги из избранного

test_get_list_of_favorites_books_check_favorites - проверка получения книг из избранного