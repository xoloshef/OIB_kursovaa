alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
            'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ', ', '.', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё',
            'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',
            'Ы', 'Ь', 'Э', 'Ю', 'Я']
alphabet1 = ['з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
             'ы', 'ь', 'э', 'ю', 'я', ' ', ', ', '.', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
             'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
             'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж']
alphabet2 = ['п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ', ', '.', 'А', 'Б', 'В',
             'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
             'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
             'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о']
alphabet3 = ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', ', ', '.', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
             'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
             'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
             'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц']

text = input("Введите сообщение: \n")
key = int(input("Введите ключ шифрования: "))
"""
tш = tо + w mod (k-1)
tш - символ зашифрованного текста,
tо - символ исходного текста,
w - целое число в диапазоне 0 - (k-1),
k - число символов используемого алфавита. 69 
"""


def encrypted(t):
    z = 0
    k = 66
    ret = []
    for x in text:
        if x in alphabet:
            if (z % 3) == 0:
                id1 = alphabet.index(x)
                #print(alphabet[id1])
                id = id1 + key % (k - 1)
                #print(alphabet1[id])
                ret += alphabet1[id]
                #print('alphabet1')
                #print(ret)
            elif (z % 3) == 1:
                id1 = alphabet.index(x)
                #print(alphabet[id1])
                id = id1 + key % (k - 1)
                #print(alphabet2[id])
                ret += alphabet2[id]
                #print('alphabet2')
                #print(ret)
            elif (z % 3) == 2:
                id1 = alphabet.index(x)
                #print(alphabet[id1])
                id = id1 + key % (k - 1)
                #print(alphabet3[id])
                ret += alphabet3[id]
                #print('alphabet3')
                #print(ret)
            z = z + 1
        else:
            ret += x
    sret = ''.join(ret)
    return sret


def decrypted(t):
    z = 0
    y = 0
    k = 66
    ret = []
    for x in entext:
        z = z + 1
    while y != z:
        for x in entext:
            if (y % 3) == 0:
                if x in alphabet1:
                    """
                    id1 = alphabet.index(x)
                    #print(alphabet[id1])
                    id = id1 + key % (k - 1)
                    #print(alphabet1[id])
                    ret += alphabet1[id]
                    """
                    print('alphabet1')
                    #print(alphabet1[id])
                    id1 = alphabet1.index(x)
                    id = id1 - key % (k - 1)
                    print(alphabet[id])
                    ret += alphabet[id]
                    print(ret)

                    # id = alphabet1.index(x)
                    # ret += alphabet[id]
                    y = y + 1
            elif (y % 3) == 1:
                if x in alphabet2:
                    print('alphabet2')
                    #print(alphabet2[id])
                    id1 = alphabet2.index(x)
                    id = id1 - key % (k - 1)
                    print(alphabet[id])
                    ret += alphabet[id]
                    print(ret)

                    # id = alphabet2.index(x)
                    # ret += alphabet[id]
                    y = y + 1
            elif (y % 3) == 2:
                if x in alphabet3:
                    print('alphabet3')
                    #print(alphabet3[id])
                    id1 = alphabet3.index(x)
                    id = id1 - key % (k - 1)
                    print(alphabet[id])
                    ret += alphabet[id]
                    print(ret)

                    # id = alphabet3.index(x)
                    # ret += alphabet[id]
                    y = y + 1
            else:
                ret += x
        sret = ''.join(ret)
        return sret


entext = encrypted(text)
print("Зашифрованное сообщение:\n", entext)
detext = decrypted(entext)
print("Расшифрованное сообщение:\n", detext)

""" Вариант 28 gamma
При построении системы безопасности применяются политики защиты, основанные на требованиях, определяемых направлениями деятельности компании

При построении системы безопасности применяются политики защиты, основанные на требованиях, определяемых направлениями деятельности компании
"""