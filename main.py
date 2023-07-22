alphabet_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
               'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

alphabet_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

step = int(input("Введите шаг: "))
lang = input("Выберете язык RU/EN: ").lower()
message = str(input('Введите сообщение для шифровки: ').lower())
result = ""

if lang == 'ru' or lang == "ру":

    for item in message:
        try:
            place = alphabet_ru.index(item)
            if place + step >= len(alphabet_ru):
                new_place = (place + step) % int(len(alphabet_ru))
                result += alphabet_ru[new_place]
            else:
                new_place = place + step
                result += alphabet_ru[new_place]
        except ValueError:
            result += item

        #result += alphabet_ru[new_place]

elif lang == "en" or lang == 'eng':

    for item in message:
        try:
            place = alphabet_en.index(item)
            if place + step > len(alphabet_en):
                new_place = int(place + step) % int(len(alphabet_en))
                result += alphabet_en[new_place]
            else:
                new_place = place + step
                result += alphabet_en[new_place]
        except ValueError:
            result += item

else:
    print("Ошибка ввода")



print(result)
