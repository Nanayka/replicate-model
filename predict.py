from cog import BasePredictor, Input, Path
from PIL import Image
from typing import Any
import torch
from diffusers import StableDiffusionPipeline

class Predictor(BasePredictor):
    def setup(self):
        # Загружаем модель (можно указать свою модель или взять pretrained)
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1",
            torch_dtype=torch.float16
        ).to("cuda")

    def predict(
        self,
        input_photo: Path = Input(description="Фото пользователя"),
        style: str = Input(description="Желаемый стиль", default="in the style of Hollywood glamour")
    ) -> Path:
        # Загружаем изображение
        image = Image.open(input_photo).convert("RGB")

        # Преобразуем изображение в описание (в реальных проектах здесь должна быть модель для извлечения черт)
        # В этом примере мы просто вставляем "A photo of a woman" + стиль
        prompt = f"A photo of a woman {style}"

        # Генерация изображения
        output = self.pipe(prompt=prompt).images[0]

        # Сохраняем результат
        output_path = "/tmp/output.png"
        output.save(output_path)

        return Path(output_path)
