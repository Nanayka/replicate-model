from cog import BasePredictor, Input, Path
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
import uuid

class Predictor(BasePredictor):
    def setup(self):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16,
            revision="fp16",
        ).to("cuda" if torch.cuda.is_available() else "cpu")

    def predict(
        self,
        input_photo: Path = Input(description="Фотография пользователя"),
        style: str = Input(description="Стиль генерации", default="in the style of Hollywood glamour"),
    ) -> Path:
        prompt = f"portrait photo of the same person {style}"
        image = self.pipe(prompt=prompt).images[0]

        output_path = f"/tmp/output-{uuid.uuid4().hex[:8]}.png"
        image.save(output_path)
        return Path(output_path)
