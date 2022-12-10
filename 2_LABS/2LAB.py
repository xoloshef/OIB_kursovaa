print("Будем шифровать или расшифровывать? cif/decif")
cipher = input()
print("Введите, пожалуйста, ваше предложение: ")
text = input()

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
            'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
            'Э', 'Ю', 'Я']
alphabet1 = ['ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
             'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
             'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'А', 'Б', 'В', 'Г',
             'Д', 'Е', 'Ё']
alphabet2 = ['о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
             'з', 'и', 'й', 'к', 'л', 'м', 'н', 'ы', 'ь', 'э', 'ю', 'я', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
             'Ч', 'Ш', 'Щ', 'Ъ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'Ы', 'Ь',
             'Э', 'Ю', 'Я']
alphabet3 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
             'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '@', '%', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
             '{', '}', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '+', '*', '&',
             '$']
gamma = '' '.,:;`\|/()!?№^-=_'


def cryp(t):
    z = 0
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
        elif x.isalpha() == False:
            ret.append(gamma[(gamma.find(x) + z) % len(gamma)])
        else:
            ret += x
    sret = ''.join(ret)
    return sret


def encreep(t):
    z = 0
    y = 0
    ret = []
    for x in text:
        z = z + 1
    while y != z:
        for x in text:
            if (y % 3) == 0:
                if x in alphabet1:
                    id = alphabet1.index(x)
                    ret += alphabet[id]
                    y = y + 1
                elif x.isalpha() == False:
                    ret.append(gamma[(gamma.find(x) - y) % len(gamma)])
                    y = y + 1
            elif (y % 3) == 1:
                if x in alphabet2:
                    id = alphabet2.index(x)
                    ret += alphabet[id]
                    y = y + 1
                elif x.isalpha() == False:  #
                    ret.append(gamma[(gamma.find(x) - y) % len(gamma)])  #
                    y = y + 1  #
            elif (y % 3) == 2:
                if x in alphabet3:
                    id = alphabet3.index(x)
                    ret += alphabet[id]
                    y = y + 1
                elif x.isalpha() == False:
                    ret.append(gamma[(gamma.find(x) - y) % len(gamma)])
                    y = y + 1
            else:
                ret += x
        sret = ''.join(ret)
        return sret


if cipher == "cif":
    print(cryp(text))
elif cipher == "decif":
    print(encreep(text))
else:
    print("Прошу прощения, но, видимо, где-то ошибка. Надеюсь, вы правильно всё написали. Приношу извинения за сбой!")