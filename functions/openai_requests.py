import openai
from decouple import config

#Retrieve enviremont variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Open ai - Whisper
#COnvert audio to text

def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1",audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return
