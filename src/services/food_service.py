from transformers import pipeline
from PIL import Image
import io

classifier=pipeline(
    "image-classification",
    model="nateraw/food"
)

def detect_food(image_bytes):

    image = Image.open(
        io.BytesIO(image_bytes)
    )

    result = classifier(image)

    return result[:3]
    