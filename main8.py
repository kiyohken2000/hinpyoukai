import torch
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline

model_id_or_path = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float32)
pipe = pipe.to("cpu")

init_image = Image.open("input_image.jpg").convert("RGB")
init_image

prompt = "被写体はそのままで背景だけ桜吹雪にする"

images = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images
images[0]

print('hello')

generated_image = images[0]
generated_image.save("generated_image.jpg")