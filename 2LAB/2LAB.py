# ЛАБОРАТОРНАЯ РАБОТА № 2. МНОГОАЛФАВИТНАЯ ОДНОКОНТУРНАЯ ПОДСТАНОВКА

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
            'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
            'Э', 'Ю', 'Я', ' ', '.', ',', ':', ';', '|', '/', '(', ')', '!', '?', '№', '^', '-',  '=', '_']
alphabet1 = ['ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
            'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
            'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '.', ',', ':',
            ';', '|', '/', '(', ')', '!', '?', '№', '^', '-',  '=', '_', 'а', 'б', 'в', 'г', 'д', 'е', 'ё']
alphabet2 = ['о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В',
             'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
             'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '.', ',', ':', ';', '|', '/', '(', ')', '!', '?', '№',
             '^', '-',  '=', '_', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н']
alphabet3 = ['х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
             'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
             'Ю', 'Я', ' ', '.', ',', ':', ';', '|', '/', '(', ')', '!', '?', '№', '^', '-',  '=', '_', 'а', 'б', 'в',
             'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф']

text = input("Введите сообщение: \n")
key = int(input("Введите ключ шифрования: "))

def encrypted(t):
    z = key
    ret = []
    for x in text:
        if x in alphabet:
            if (z % 3) == 0:
                id = alphabet.index(x)
                ret += alphabet1[id]
            elif (z % 3) == 1:
                id = alphabet.index(x)
                ret += alphabet2[id]
            elif (z % 3) == 2:
                id = alphabet.index(x)
                ret += alphabet3[id]
            z = z + 1
        else:
            ret += x
    sret = ''.join(ret)
    return sret

def decrypted(t):
    z = key
    y = key
    ret = []
    for x in entext:
        z = z + 1
    while y != z:
        for x in entext:
            if (y % 3) == 0:
                if x in alphabet1:
                    id = alphabet1.index(x)
                    ret += alphabet[id]
                    y = y + 1
            elif (y % 3) == 1:
                if x in alphabet2:
                    id = alphabet2.index(x)
                    ret += alphabet[id]
                    y = y + 1
            elif (y % 3) == 2:
                if x in alphabet3:
                    id = alphabet3.index(x)
                    ret += alphabet[id]
                    y = y + 1
            else:
                ret += x
        sret = ''.join(ret)
        return sret

entext = encrypted(text)
print("Зашифрованное сообщение:\n", entext)
detext = decrypted(entext)
print("Расшифрованное сообщение:\n", detext)

""" Вариант 28
Преобразование шифрования может быть симметричным или асимметричным относительно преобразования расшифрования.
"""