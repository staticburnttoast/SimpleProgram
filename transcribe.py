from openai import OpenAI
client = OpenAI(api_key="SET YOUR OWN OPENAI API KEY HERE!!") # Creating an OpenAI account gives you $5 of free credit!

audio_file = open("SET THIS AS THE PATH TO A .WAV FILE!!", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcription.text)