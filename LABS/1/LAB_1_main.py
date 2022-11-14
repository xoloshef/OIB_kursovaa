print('выберите тип шифрования (s) - симметричное или (as) - асимметричное')
a = str(input('Напишите s или as'))
if a == 's':
    print('Выбранный тип шифрования - симметричный')

    IZHODNIK = 'Существует два класса криптосистем: симметричные (одноключевые) и асимметричные (двухключевые).'
    key = [28]

    print('Исходное сообщение: ', IZHODNIK)
    print('Ключ - ', key)

    text = []
    for __ in list(IZHODNIK):
        text.append(ord(__))  # ord() - представление слова, как числа
    print('после перевода текста в цифры: ', text)

    etext = []
    __key = 0
    for __ in range(0, len(text)):
        etext.append(text[__] + key[__key])
    if __key == len(key) - 1:
       __key = 0
    else:
        __key += 1
    print('Результат работы шифратора: ', etext)

    unetext = []
    __key = 0
    for __ in range(0, len(etext)):
        unetext.append(chr(etext[__] - key[__key]))
    if __key == len(key) - 1:
        __key = 0
    else:
        __key += 1
    print('Результат работы дешифратора: ', unetext)