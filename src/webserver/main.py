from fastapi import FastAPI, UploadFile, File, Request, Form
from fastapi.responses import JSONResponse
from utils import preprocess_image, postprocess_image
from network_clients import DefaultClient
import os

app = FastAPI()
ml_client = DefaultClient(os.getenv('FORWARD_URL'))


@app.post('/generate')
async def generate(prompt: str = Form(...), image: UploadFile = File(None)):
    image_attached = False
    if image is not None:
        image_attached = True
        image = await preprocess_image(image)
    result = await ml_client.post({'image_attached': image_attached,
                                   'prompt': prompt,
                                   'image': image})
    # result = postprocess_image(image)
    return result


@app.post('/test')
async def test_generate(request: Request):
    data = await request.json()
    return JSONResponse({'image_attached': data['image_attached'],
                         'prompt': data['prompt'],
                         'image': data['image']})
