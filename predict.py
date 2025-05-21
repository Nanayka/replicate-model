import os
from replicate import Client

def main():
    api_token = os.getenv("REPLICATE_API_TOKEN")
    if not api_token:
        raise ValueError("Установите переменную окружения REPLICATE_API_TOKEN")
    client = Client(api_token=api_token)

    model = client.models.get("nanayka/nanayka-my-model")

    # Пример входных данных (замени на свои)
    input_data = {
        "input_photo_url": "https://example.com/photo.jpg",
        "style": "hollywood"
    }

    prediction = model.predict(**input_data)
    print(prediction)

if __name__ == "__main__":
    main()
