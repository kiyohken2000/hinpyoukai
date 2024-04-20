import requests

API_URL = "https://api-inference.huggingface.co/models/Elizezen/Hameln-japanese-mistral-7B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print('test')
print(output)