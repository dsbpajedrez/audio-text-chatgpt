from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#custom functions imports
from functions.openai_requests import convert_audio_to_text

app = FastAPI()

#CORS -- origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]

#cors middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods = ['*'],
    allow_headers = ['*']

)

@app.get("/health")
async def cheackhelth():
    return {"message": "Heathy life!"}

@app.get("/post-audio-get/")
async def get_audio():
    #Get safed audio
    audio_input = open("voice.mp3", "+rb")

    #decode audio
    message_decode = convert_audio_to_text(audio_input)

    print(message_decode)
    return "done"


#post bot response
#note: Notplaying in browser when using post request
@app.post("/post-audio/")
async def post_audio(file: UploadFile= File(...)):
   open_audio = open("voice.mp3", "+rb")
   converted_audio = convert_audio_to_text(open_audio)
   print(converted_audio)
    