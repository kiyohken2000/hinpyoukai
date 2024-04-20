from gradio_client import Client
import os

HF_TOKEN = os.environ.get("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")
client = Client("https://cohereforai-c4ai-command-r-v01.hf.space/--replicas/lnnpd/", hf_token=HF_TOKEN)
result = client.predict(
		"こんにちは。あなたは誰ですか？",	# str  in 'Input' Textbox component
							api_name="/generate_response"
)
print(result)