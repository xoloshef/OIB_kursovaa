alphabet = " ():!_?<>.,-абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
izh = input("Введите сообщение: ")
key = 8
print("ключ шифрования - ", key)
encrypto = ""
decrypto = ""

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

