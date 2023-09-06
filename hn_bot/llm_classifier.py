import requests
import json

AGENTA_ENDPOINT = ""


def classify_post(title: str, interests: str) -> bool:

    url = AGENTA_ENDPOINT
    params = {
        "inputs": {
            "title": title,
            "interests": interests
        },
        "temperature": 0,
        "model": "gpt-3.5-turbo",
        "maximum_length": 100,
        "prompt_system": "You are an expert in classification. You answer only with True or False.",
        "prompt_human": "Classify whether this hackernews post is interesting for someone with the following interests: \n Hacker news post title: {title}\nInterests: {interests}",
        "stop_sequence": "\n",
        "top_p": 1,
        "frequence_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, json=params)

    data = response.json()
    return bool(data)
