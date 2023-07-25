import json
import random

def get_recent_messages():
    #Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role":"system",
        "content":"You are interviewing the user for a job as a retail assistant. Ask short questions that are relevant to the junior position. Your name is Rachel. The user is David. Keep your answer under 30 words"
    }

    messages =[]

    #Add a random element
    x = random.uniform(0,1)

    if x<=0.5:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include some dry humour"
    else:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include a rather challenging question"
