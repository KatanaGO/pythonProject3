def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()


# Вызов функции test_function, который в свою очередь вызовет inner_function
test_function()

# Попытка вызвать inner_function вне функции test_function
try:
    inner_function()
except NameError as e:
    print("Ошибка:", e)
