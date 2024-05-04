from gradio_client import Client

client = Client("hysts/DeepDanbooru")
result = client.predict(
		"https://i.ibb.co/sWzNScJ/44b4e7c79251.jpg",	# filepath  in 'Input' Image component
		0.5,	# float (numeric value between 0 and 1) in 'Score threshold' Slider component
		api_name="/predict"
)
print('test')
print(result[-1])