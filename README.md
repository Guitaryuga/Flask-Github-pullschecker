# Flask-Guthub-pullschecker
Веб-сервис на Flask, который позволяет проверить активносить и вовлеченность пользователя Github в проектах, размещенных в репозиториях на github.com. Введите имя пользователя и вы увидите отображение всех проектов, в которых принимает участие пользователь, и по каждому проекту:
- Название проекта
- Ссылку на него
- Количество звезд
- Ссылки на пулл-реквесты пользователя(если они есть), которые смерждили в этом проекте с количеством комментариев
- Ссылки на пулл-реквесты пользователя(если они есть), которые не смерджили в этом проекте, с количеством комментариев

![image](https://user-images.githubusercontent.com/74609399/113061559-e9f4a100-91ba-11eb-830d-71909108cccb.png)

### Установка
Для того, чтобы ознакомиться с функционалом:

1.Клонируйте репозиторий
```
git clone https://github.com/Guitaryuga/Flask-Guthub-pullschecker.git
```
2. Создайте и активируйте виртуальное окружение, затем установите зависимости:
```
pip install -r requirements.txt
```
3. Создайте файл .env и задайте в нем переменные окружения:
```
SECRET_KEY="YOUR_SECRET_KEY"
LOGIN_NAME='YOUR_GITHUB_LOGIN_NAME'
TOKEN='YOUR_TOKEN' (можно получить здесь: https://github.com/settings/tokens - 'Generate new token')
```
4.Для запуска используйте существующий run.bat(измените конфигурацию для запуска при необходимости) или другой необходмый вам способ
```
run
```
