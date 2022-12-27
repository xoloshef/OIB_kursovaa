# ЛАБОРАТОРНАЯ РАБОТА № 1. ОДНОАЛФАВИТНАЯ ПОДСТАНОВКА

alphabet = " ():!_?<>.,-абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
izh = input("Введите сообщение: ")
key = int(input("Введите ключ шифрования: "))
encrypted = ""
decrypted = ""

for message in izh:
    position = alphabet.find(message)
    position1 = position + key
    encrypted = encrypted + alphabet[position1]
print("Зашифрованное сообщение: ", encrypted)

for message in encrypted:
    position = alphabet.find(message)
    position1 = position - key
    decrypted = decrypted + alphabet[position1]
print("Расшифрованное сообщение: ", decrypted)

"""
Существует два класса криптосистем: симметричные (одноключевые) и асимметричные (двухключевые).
"""