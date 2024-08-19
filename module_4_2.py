def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
test_function() # - происходит вызов функции, выводит "Я в области видимости функции test_function"
#inner_function() - Тут будет ошибка, если вызвать вне функции test_function
