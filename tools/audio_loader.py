import os
import time
from gtts import gTTS

SYMBOLS_TO_REPLACE = " .,?!\"\'"
LOADING_SLEEP_TIME_S = 0.1

def get_audiofile_name(word):
    audiofile_name = "".join(ch if ch not in SYMBOLS_TO_REPLACE else "_" for ch in word)
    return audiofile_name + ".mp3"


def load_audio(lang_key, word, audiopath="./", slow=True):
    myobj = gTTS(text=word, lang=lang_key, slow=slow)
    
    filename = get_audiofile_name(word)
    myobj.save(audiopath + filename)

    time.sleep(LOADING_SLEEP_TIME_S)
