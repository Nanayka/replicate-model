mport os
from replicate import Client

api_token = os.getenv("REPLICATE_API_TOKEN")
if not api_token:
    raise ValueError("Установите REPLICATE_API_TOKEN")

client = Client(api_token=api_token)
model_name = "nanayka/nanayka-my-model"
model = client.models.get(model_name)

input_data = {
    "input_photo_url": "https://example.com/photo.jpg",
    "style": "hollywood",
}

prediction = model.predict(**input_data)
print(prediction)
