import os
import requests
from cog import BasePredictor, Input, Path
import replicate
from PIL import Image
from io import BytesIO

class Predictor(BasePredictor):
    def setup(self):
        # Не нужно загружать модель вручную — это делает Replicate
        pass

    def predict(
        self,
        input_photo_url: str = Input(description="Ссылка на изображение"),
        style: str = Input(description="Выбранный стиль")
    ) -> Path:
        # Загружаем изображение по ссылке
        response = requests.get(input_photo_url)
        image = Image.open(BytesIO(response.content))

        # Обрабатываем изображение как input в модель (пример — для SDXL)
        output = replicate.run(
            "stability-ai/sdxl:latest",
            input={
                "prompt": f"A {style} style po
