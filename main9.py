import torch
from diffusers import AutoPipelineForImage2Image
from diffusers.utils import load_image

pipeline = AutoPipelineForImage2Image.from_pretrained(
    "kandinsky-community/kandinsky-2-2-decoder", torch_dtype=torch.float32, use_safetensors=True
)

pipeline = pipeline.to("cpu")

init_image = load_image("cat.png")

prompt = "cat wizard, gandalf, lord of the rings, detailed, fantasy, cute, adorable, Pixar, Disney, 8k"

image = pipeline(prompt, image=init_image).images[0]

image.save("generated_image.jpg")