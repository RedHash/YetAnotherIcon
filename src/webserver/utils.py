import numpy as np
from io import BytesIO
from PIL import Image


def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))


async def preprocess_image(image):
    ##TODO Преобразование в тензор и прочее
    image_np = load_image_into_numpy_array(await image.read())  # H, W, C
    ##TODO прочее
    return image_np.tolist() # Для сериализации в json, подобрать более удобный формат


def postprocess_image(image):
    ##TODO Преобразование результата из triton в картинку
    raise NotImplementedError
