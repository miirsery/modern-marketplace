# backend

## Клонируем реппозиторий:
```
git clone https://github.com/miirsery/electronic-store-V2.git
cd store
```

## Ставим виртуальное окружение и заходим в него для linux:
```
python -m venv venv
source venv/bin/activate
```
## Ставим виртуальное окружение и заходим в него для Windows:
```
python -m venv venv
source venv/Scripts/activate
```

## Устанавливаем библиотеки:
```
pip install -r requirements.txt
```

## Делаем миграции:
```
python manage.py makemigrations
python manage.py migrate
```

## Запускаем сервер:
```
python manage.py runserver
```

## Выход из виртуального окружения:
```
deactivate
```