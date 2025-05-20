# Используем официальный образ Python 3.9
FROM python:3.9-slim

# Создаём рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из репозитория в рабочую директорию контейнера
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда запуска модели при старте контейнера
CMD ["python3", "predict.py"]
