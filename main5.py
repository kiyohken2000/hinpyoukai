import requests

API_URL = "https://api-inference.huggingface.co/models/SG161222/Realistic_Vision_V1.4"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a horse",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image

# 生成された画像をファイルに保存
with open("generated_image.jpg", "wb") as f:
    f.write(image_bytes)

# 生成された画像を開く
image = Image.open("generated_image.jpg")
image.show()