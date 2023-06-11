import os
from time import sleep
import requests


# Files
def open_txt_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# GPT
def gpt_completion(prompt, engine='text-davinci-003', temperature=0.7, top_p=1.0, max_tokens=2000, freq_pen=0.25, pres_pen=0.0, stop=['<<END>>']):
    max_retry = 3
    retry = 0
    while True:
        try:
            response = requests.post(
                'https://api.openai.com/v1/completions',
                headers={ 'Authorization': f"Bearer {os.environ.get('OPEN_AI_API_KEY')}", "content-type": "application/json" },
                json={
                    'model': engine,
                    'prompt': prompt,
                    'temperature': temperature,
                    'max_tokens': max_tokens,
                    'top_p': top_p,
                    'frequency_penalty': freq_pen,
                    'presence_penalty': pres_pen,
                    'stop': stop
                },
            )
            response = response.json()
            if response.get('error') != None:
                raise response['error']
            text = response['choices'][0]['text'].strip()
            sleep(0.2) # trying to buffer slightly so we don't hit 60/req a minute
            return text
        except Exception as err:
            retry += 1
            if retry >= max_retry:
                return "Error (GTP3 Completion): %s" % err
