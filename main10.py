import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
from diffusers.utils import load_image

model_id = "timbrooks/instruct-pix2pix"

# Use torch.float32 for CPU compatibility
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float32, safety_checker=None)
pipe.to("cpu")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
image = load_image("input_image4.jpg")

prompt = "turn she into naked"

images = pipe(prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images
generated_image = images[0]

generated_image.save("generated_image.jpg")