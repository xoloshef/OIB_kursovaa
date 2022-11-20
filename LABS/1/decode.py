import rsa
# -*- coding: utf-8 -*-

#Боб формирует публичный и секретный ключ

(bob_pub, bob_priv) = rsa.newkeys(512)
print(bob_pub, bob_priv)

#Алиса формирует сообщение Бобу и кодирует его в UTF8,
#поскольку RSA работает только с байтами
sourse_text = 'hello Bob!'
print('hello Bob!')
message = sourse_text.encode('utf8')
print(message)

#Алиса шифрует сообщение публичным ключом Боба
crypto = rsa.encrypt(message, bob_pub)
print('crypro - ', crypto)

#Боб расшифровывает сообщение своим секретным ключом
message = rsa.decrypt(crypto, bob_priv)
print(message.decode('utf8'))