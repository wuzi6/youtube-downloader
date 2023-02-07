#Імпортуємо бібліотеки
from pytube import YouTube


yt = YouTube(input('Введіть посилання: '))

#Інформація про відео
print(f'Назва: {yt.title}')
print(f'Перегляди: {yt.views}')
print(f'Тривалість: {yt.length} секунд')

#Вибір якості відео
qual = input('Виберіть якість відео: min/max ')
if qual == 'min':
    ys = yt.streams.get_lowest_resolution()
else:
    ys = yt.streams.get_highest_resolution()

#Процес завантаження
print('Завантаження почалося...')
ys.download("") #Сюди потрібно вказати шлях, куди потрібно завантажити відео
print('Завантаження завершене')