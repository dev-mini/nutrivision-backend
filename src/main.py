from fastapi import FastAPI, UploadFile
from services.food_service import detect_food

app = FastAPI()

@app.post("/analyze")
async def prediction(file: UploadFile):

    image_bytes = await file.read()

    foods = detect_food(image_bytes)

    return foods