from gtts import gTTS
from playsound import playsound

audio = "example.mp3"
language = 'en'
clip = gTTS(text="Hello Vincent", lang=language, slow=False)

clip.save(audio)
playsound(audio)