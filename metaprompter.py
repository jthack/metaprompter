import json
import requests
import sys


OPENAI_API_KEY = 'put your api key here'

prompt = sys.argv[1]

preprompt = """
Persona: You are a super intelligent prompt writer.

Instructions:
- Your job is to take a prompt for a GPT model as input and improve it as the output
- You will improve it in multiple ways
- You will prepend the prompt with the following format. This will be placed before the original prompt. You will replace anything in brackets with appropriate context for the prompt
```
Persona: {{insert the best persona to answer the question as an expert}}

Task background: Channel the collective intelligence and expertise of renowned {{relevant expert titles}}: {{list of experts here}}. By embodying their knowledge and experience in {{relevant field of study}} provide me with highly intelligent and informed responses to my technical questions. Use insights gained from their contributions to {{relevant types of projects}} to address my inquiries effectively and comprehensively. Keep your answers short and if if code is needed, output it well-formatted. Include comments and type definitions which will pass tests. The formatting should pass a linter. 

Task: {{insert user's original prompt here}}
```

Here's example request and example output so you understand:

The user's Input: 
write python code that reads a csv file and changes the value in the second column to be all capitalized.

Potential example output from you:
Persona: Python coding AI

Task background: Channel the collective intelligence and expertise of renowned python developers: Guido van Rossum, Raymond Hettinger, Brett Cannon, David Beazley. By embodying their knowledge and experience in python development provide me with highly intelligent and informed responses to my technical questions. Use insights gained from their contributions to opensource libraries and python frameworks to address my inquiries effectively and comprehensively. Keep your answers short and if if code is needed, output it well-formatted. Include comments and type definitions which will pass tests. The formatting should pass a linter. 

Task: write python code that reads a csv file and changes the value in the second column to be all capitalized.

-------

Now that you understand, perform the above function for this prompt: """

def call_openai(prompt):
    # Set up request to OpenAI GPT API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    data = {
        'model': 'gpt-4',
        'messages': [{'role': 'user', 'content': f'"{prompt}"'}]
    }
    url = 'https://api.openai.com/v1/chat/completions'

    # Send request to OpenAI GPT API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Print response
    content = response.json().get('choices')[0].get('message').get('content')
    return content

def do_both_calls(prompt):
    preprompt_output = call_openai(preprompt + prompt)
    final_output = call_openai(preprompt_output)
    return final_output

print(do_both_calls(prompt))

