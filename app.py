import requests
import json
import gradio as gr

# url to display on browser
url="http://localhost:11434/api/generate"

# headers to tell the server we are sending JSON data
headers={

    'Content-Type':'application/json'
}

# keeping context
history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

# defining model and prompt details
    data={
        "model":"llama3",
        "prompt":final_prompt,
        "stream":False          # used to show that all data to be printed at once
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

# server checks
    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)

# UI 
interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch()
