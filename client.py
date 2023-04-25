import locale
import subprocess

import chardet

print('Задание № 1')
''' Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных '''

my_list = ['разработка', 'сокет', 'декоратор']
print('\nв строковом формате:')
for elem in my_list:
    print(elem, type(elem))

my_list = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]
print('\nв формате Unicode:')
for elem in my_list:
    print(elem, type(elem))

print('\nЗадание № 2')
''' Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных. '''

my_list = [b'class', b'function', b'method']
for elem in my_list:
    print(f'{type(elem)} - {elem} - {len(elem)}')


print('\nЗадание № 3')
'''Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.'''

my_list = ['attribute', 'класс', 'функция', 'type']
for elem in my_list:
    elem_encode = elem.encode('ascii', errors='ignore')
    print(elem_encode)
    print(type(elem_encode))

print('\nЗадание № 4')
'''Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).'''

my_list = ['разработка', 'администрирование', 'protocol', 'standard']
for elem in my_list:
    elem_encode = elem.encode('ascii', errors='ignore')
    print(ascii(elem_encode), type(elem_encode))
    elem_decode = elem_encode.decode('ascii', errors='ignore')
    print(ascii(elem_decode), type(elem_decode))

print('\nЗадание № 5')
'''Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.'''

# args = ['ping', 'yandex.ru']
# ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in ya_ping.stdout:
#     result = chardet.detect(line)
#     print(result)
#     line = line.decode(result['encoding']).encode('utf-8')
#     print(line.decode('utf-8'))

print('\nЗадание № 6')
'''Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.'''
def_coding = locale.getpreferredencoding()
print(def_coding)
with open('text_file.txt', encoding='utf-8') as f:
    for elem in f:
        print(elem, end='')
