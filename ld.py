#Задание
#Создайте список из чисел 3, 5, 7, 9 и 10.5
#Выведите содержимое списка на экран
#Добавьте в конец списка строку "Python"
#Выведите длину списка на экран



numbers = [3, 5, 7, 9, 10.5]
print(numbers)
numbers.append("Python")
print(len(numbers))
print(f'UPD list "Numbers":{numbers}')



#Задание
#Выведите на экран начальный элемент списка
#Выведите на экран последний элемент списка
#Напечатайте элементы списка со второго по четвертый включительно
#Удалите из списка строку "Python"

numbers = [3, 5, 7, 9, 10.5]
print(numbers)
numbers.append("Python")
print(len(numbers))
print(f'UPD list "Numbers":{numbers}')
print(numbers[0])
print(numbers[5]) # или
print(numbers[-1]) # или
print(numbers[1:5])
numbers.remove("Python")
print(numbers)


#Задание
#Создайте словарь:
#{"city": "Москва", "temperature": "20"}
#Выведите на экран значение ключа city
#Уменьшите значение "temperature" на 5
#Выведите на экран весь словарь

weather = {"city": "Москва", "temperature": "20"}
print(weather["city"])

weather["temperature"] = 15
print(weather)




#Задание
#Проверьте, есть ли в словаре ключ country
#Выведите значение по-умолчанию "Россия" для ключа country
#Добавьте в словарь элемент date со значением "27.05.2019"
#Выведите на экран длину словаря


weather = {"city": "Москва", "temperature": "20"}
print(weather["city"])

weather["temperature"] = 15
print(weather)
print(weather.get("country"))
weather["country"] = "Россия"
#weather.get("country", "Россия") Про значение по умолчанию не очень понятно ??
weather["date"] = "27.05.2019"
print(len(weather))
print(weather)