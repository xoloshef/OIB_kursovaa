#pip install pycryptodome

sourse_text = 'Существует два класса криптосистем: симметричные (одноключевые) и асимметричные (двухключевые).'
print("Выберете тип шифрования: s-симметричное или a-aсимметричное")
option = str(input('Напишите s или a\n'))

def symmetric_encrypto(sourse_text):
    print("Шифруемый текст: ", sourse_text)



def asymmetric_encrypto(sourse_text):
    print("Шифруемый текст: ", sourse_text)


if option == "s":
    symmetric_encrypto(sourse_text)
elif option == "a":
    asymmetric_encrypto(sourse_text)