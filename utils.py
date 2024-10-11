import json
import requests

def call_llama(model, prompt, stream=False):
    url = "http://localhost:11434/api/generate"
    data = {
        "model" : model, 
        "prompt" : prompt, 
        "stream" : stream
    }

    json_data = json.dumps(data)
    response = requests.post(url, data = json_data, headers= {"content_type": "application/json"})

    if response.status_code == 200:
        return response.json()

    else:
        return f"Error: {response.status_code}"


if __name__ == "__main__":
    model = "llama3.2:1b"
    prompt = input("please enter your question: ")
    print(call_llama(model, prompt)["response"])
    