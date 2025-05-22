from cog import BasePredictor, Input
from typing import Any
import requests
from PIL import Image
from io import BytesIO

class Predictor(BasePredictor):
    def setup(self):
        # Здесь можно загрузить вес модели, если они есть
        pass

    def predict(self, input_photo_url: str = Input(description="URL фото"), style: str = Input(description="Стиль")) -> Any:
        # Скачиваем изображение
        response = requests.get(input_photo_url)
        image = Image.open(BytesIO(response.content))

        # Здесь будет логика генерации по стилю (пока просто сохраняем)
        output_path = "/tmp/generated_output.jpg"
        image.save(output_path)

        return output_path
