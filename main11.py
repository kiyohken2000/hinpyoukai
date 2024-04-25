import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained(
    "damo-vilab/text-to-video-ms-1.7b", 
    torch_dtype=torch.float32,  # float32を使用
    device="cpu"  # CPUを使用するように指定
)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

prompt = "Spiderman is surfing"
video_frames = pipe(prompt, num_inference_steps=25).frames
export_to_video(video_frames, output_video_path="generated_video.mp4")