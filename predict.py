import os
import replicate

def main():
    api_token = os.getenv("REPLICATE_API_TOKEN")
    if not api_token:
        raise ValueError("Установите переменную окружения REPLICATE_API_TOKEN")
    
    client = replicate.Client(api_token=api_token)

    # Запуск модели через replicate.run()
    output = client.run(
        "nanayka/nanayka-my-model:latest",  # или нужная версия модели
        input={
            "input_photo_url": "https://example.com/photo.jpg",
            "style": "hollywood"
        }
    )
    
    print(output)

if __name__ == "__main__":
    main()
