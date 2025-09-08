# regHelp

Инструмент для создания retrieval-augmented чат-бота Telegram на базе GigaChat и локального векторного хранилища Weaviate.

## Ключевая идея

Проект позволяет загружать PDF/DOCX векторизованные документы в локальную базу Weaviate и отвечать на вопросы пользователей через Telegram-бота, комбинируя RAG (retrieval-augmented generation) с моделью GigaChat.

## Основные возможности

- Приём PDF и DOCX файлов через Telegram и автоматическая векторизация.
- Поисковый ретривер на базе Weaviate.
- Генерация ответов с использованием GigaChat.
- Поддержка нескольких эмбеддингов-моделей (All-MiniLM, BGE-M3, GigaChat Embeddings).

## Стек технологий

- Python 3.10+
- Telegram Bot API (python-telegram-bot / aiogram примеры)
- LangChain (интеграция с Weaviate и GigaChat)
- Weaviate (локальный векторный стор)
- sentence-transformers, BGEM3 (через FlagEmbedding), GigaChat embeddings
- dotenv для конфигурации

## Быстрый старт (локально)

1. Клонируйте репозиторий:

   git clone <repo>

2. Создайте виртуальное окружение и установите зависимости (пример для venv):

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

3. Создайте файл `.env` в корне и добавьте переменные (см. раздел ниже).

4. Запустите бота Telegram:

   python bot.py

Примечание: проект подразумевает, что локально запущен Weaviate. См. docs/build.md для инструкций по развёртыванию Weaviate и зависимостей.

## Переменные окружения

Обязательные:

- TELEGRAM_API_TOKEN — токен Telegram-бота.
- GIGACHAT_API_KEY — ключ API GigaChat.

Опциональные (в зависимости от конфигурации):

- PROVIDER_TOKEN — токен провайдера платежей для `aoigram_paybot_example.py`.

## Структура проекта

- `ai.py` — клиент GigaChat и построение RAG-цепочки.
- `bot.py` — основной Telegram-бот (python-telegram-bot), обработка файлов и вопросов.
- `aoigram_paybot_example.py` — пример реализации покупки через aiogram.
- `embeddings/` — адаптеры эмбеддингов: `all_mini_lm.py`, `bge_m3.py`, `giga_chat.py`, `get_embeddings_by_model.py`.
- `files/` — логика обработки файлов: `pdf_embedder.py`, `transfer_file_to_embeddings.py`, `embedder.py`.
- `input/system_prompt.txt` — системный промпт для RAG chain.
- `user_files/` — пример загруженных пользователем файлов.

## Запуск тестов

В этом репозитории нет набора unit-тестов по умолчанию; рекомендуется добавить pytest-based тесты для критичных модулей (embeddings, files, ai). В docs/testing.md приведены рекомендации.

## Важные нюансы и рекомендации

- Weaviate должен быть запущен локально и доступен приложению; проект использует `weaviate.connect_to_local()`.
- Для BGE-M3 требуется сторонняя библиотека `FlagEmbedding` и модель `BAAI/bge-m3`. Убедитесь в совместимости по версии Python и доступности GPU/CPU.
- При использовании GigaChat используйте корректный `GIGACHAT_API_KEY`; проверьте лимиты и настройки `max_tokens`.
- Удаление временных загруженных файлов реализовано в `files/transfer_file_to_embeddings.py`.

## Лицензия

Проект распространяется под лицензией MIT — см. `LICENSE`.
# regHelp