# VK Get Access Token
### Получить токен от страницы ВК теперь не проблема

<img src="https://github.com/jieggii/vk-get-access-token/blob/master/img/1.png"></img>

## Как это работает
* Программа имитирует получение access token'a приложением, после чего возвращает его.

## Установка
### Linux
```
~# sudo apt update
~# sudo apt install python3 python3-pip
~# git clone https://github.com/jieggii/vk-get-access-token.git
~# cd vk-get-access-token.git
~# pip3 install -r requirements.txt
```

### Windows
1. Скачайте Python 3 с <a href="https://python.org">официального сайта</a>
2. При установке поставьте галочку на пункте <b>pip</b>
3. Скачайте <a href="/archive/master.zip">архив с программой</a> и распакуйте его в удобное для вас место
4. Зажмите сочетание клавиш <b>WIN+R</b>, напишите <b>cmd</b> и нажмите <b>Enter</b>
5. Пропишите команду ```cd [path]```, где ```[path]``` - путь до папки, которую вы распаковали
6. Пропишите команду ```pip install -r requirements.txt```

## Запуск
### Использование
```
usage: vk-get-access-token.py [-h] [-l LOGIN] [-p PASSWORD] [-q]
                              [-f FILE_PATH] [-cl CLIENT_ID]
                              [-cs CLIENT_SECRET]

optional arguments:
  -h, --help            помощь по программе
  -l LOGIN, --login LOGIN
                       Ваш логин от VK
  -p PASSWORD, --password PASSWORD
                        Ваш пароль от VK
  -q, --quiet           Не выводить ваш токен в терминал (для безопасности), полезно когда вы используете сохранение токена в файл
  -f FILE_PATH, --file-path FILE_PATH
                        Сохранить токен в файл [file path]

VK app settings (optional):
  -cl CLIENT_ID, --client-id CLIENT_ID
                        VK app client id
  -cs CLIENT_SECRET, --client-secret CLIENT_SECRET
                        VK app secret
```

### Примеры команд
```
~# python3 vk-get-access-token.py --login +3563284545 --password helloworld123 --quiet --file-path my_access_token.txt
~# python vk-get-access-token.py
```

### License
* MIT
