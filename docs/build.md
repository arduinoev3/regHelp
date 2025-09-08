# Сборка и развёртывание (локально)

Эти шаги помогут вам подготовить окружение для запуска проекта локально.

1) Python окружение

   - Установите Python 3.10+.
   - Создайте виртуальное окружение и установите зависимости:

     python -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt

2) Weaviate (локально)

   - Рекомендуется запустить Weaviate при помощи Docker Compose. Пример `docker-compose` конфигурации:

     version: '3.4'
     services:
       weaviate:
         image: semitechnologies/weaviate:latest
         ports:
           - '8080:8080'
         environment:
           - QUERY_DEFAULTS_LIMIT=20
           - AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true
           - PERSISTENCE_DATA_PATH=/var/lib/weaviate

   - Запустите:

     docker compose up -d weaviate

   - Убедитесь, что Weaviate доступен на `http://localhost:8080`.

3) GigaChat

   - Получите API-ключ для GigaChat и поместите его в `.env` под именем `GIGACHAT_API_KEY`.

4) Telegram Bot

   - Создайте бота через BotFather и поместите токен в `.env` как `TELEGRAM_API_TOKEN`.

5) Запуск

   - Активируйте виртуальное окружение и запустите бота:

     source .venv/bin/activate
     python bot.py

6) Проверка встраивания файлов

   - Отправьте PDF в бота; файл будет загружен, разбит на чанки и сохранён в Weaviate через текущую реализацию в `files/pdf_embedder.py`.
