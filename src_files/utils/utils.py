from PIL import Image
from io import BytesIO
import requests


# Helper functions
def get_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content)).convert('RGB')

    return image
